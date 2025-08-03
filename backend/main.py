from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class Personality(BaseModel):
    openness: float
    conscientiousness: float
    extraversion: float
    agreeableness: float
    emotional_range: float
    conversation: float
    openness_to_change: float
    hedonism: float
    self_enhancement: float
    self_transcendence: float

artifacts_path = os.path.join("model_training", "artifacts")
model_path = os.path.join(artifacts_path, "model.pkl")
label_encoder_path = os.path.join(artifacts_path, "label_encoder.pkl")


model = joblib.load(model_path)
le = joblib.load(label_encoder_path)

@app.post("/predict")
def predict(personality: Personality):
    input_data = pd.DataFrame([personality.dict()])

    for col in input_data.columns:
        input_data[col] = input_data[col] / 100.0

    input_data = input_data[['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'emotional_range', 'conversation', 'openness_to_change', 'hedonism', 'self_enhancement', 'self_transcendence']]

    input_data.columns = ['Openness', 'Conscientousness', 'Extraversion', 'Agreeableness', 'Emotional_Range', 'Conversation', 'Openness to Change', 'Hedonism', 'Self-enhancement', 'Self-transcendence']


    probabilities = model.predict_proba(input_data)[0]


    top_4_indices = probabilities.argsort()[-4:][::-1]


    top_4_probabilities = probabilities[top_4_indices]


    top_4_roles = le.inverse_transform(top_4_indices)


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