
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI()

# Define the input data model
class Personality(BaseModel):
    openness: int
    conscientiousness: int
    extraversion: int
    agreeableness: int
    emotional_range: int
    conversation: int
    openness_to_change: int
    hedonism: int
    self_enhancement: int
    self_transcendence: int

# Define paths
artifacts_path = os.path.join("model_training", "artifacts")
model_path = os.path.join(artifacts_path, "model.pkl")
label_encoder_path = os.path.join(artifacts_path, "label_encoder.pkl")

# Load the model and label encoder
model = joblib.load(model_path)
le = joblib.load(label_encoder_path)

@app.post("/predict")
def predict(personality: Personality):
    input_data = pd.DataFrame([personality.dict()])
    input_data = input_data[['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'emotional_range', 'conversation', 'openness_to_change', 'hedonism', 'self_enhancement', 'self_transcendence']]
    # Rename columns to match the training data
    input_data.columns = ['Openness', 'Conscientousness', 'Extraversion', 'Agreeableness', 'Emotional_Range', 'Conversation', 'Openness to Change', 'Hedonism', 'Self-enhancement', 'Self-transcendence']

    # Get prediction probabilities
    probabilities = model.predict_proba(input_data)[0]
    
    # Get the indices of the top 4 predictions
    top_4_indices = probabilities.argsort()[-4:][::-1]
    
    # Get the corresponding probabilities
    top_4_probabilities = probabilities[top_4_indices]
    
    # Decode the predictions
    top_4_roles = le.inverse_transform(top_4_indices)
    
    # Create the response
    response = {
        "predicted_role": {
            "role": top_4_roles[0],
            "percentage": round(top_4_probabilities[0] * 100, 2)
        },
        "alternative_roles": [
            {
                "role": top_4_roles[i],
                "percentage": round(top_4_probabilities[i] * 100, 2)
            } for i in range(1, 4)
        ]
    }
    
    return response

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Career Guidance API"}
