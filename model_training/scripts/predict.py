
import joblib
import pandas as pd
import os
import argparse

artifacts_path = os.path.join("model_training", "artifacts")
model_path = os.path.join(artifacts_path, "model.pkl")
label_encoder_path = os.path.join(artifacts_path, "label_encoder.pkl")

model = joblib.load(model_path)
le = joblib.load(label_encoder_path)

parser = argparse.ArgumentParser(description="Predict career role based on personality traits.")

parser.add_argument("--openness", type=int, required=True, help="Openness score")
parser.add_argument("--conscientiousness", type=int, required=True, help="Conscientiousness score")
parser.add_argument("--extraversion", type=int, required=True, help="Extraversion score")
parser.add_argument("--agreeableness", type=int, required=True, help="Agreeableness score")
parser.add_argument("--emotional-range", type=int, required=True, help="Emotional Range score")
parser.add_argument("--conversation", type=int, required=True, help="Conversation score")
parser.add_argument("--openness-to-change", type=int, required=True, help="Openness to Change score")
parser.add_argument("--hedonism", type=int, required=True, help="Hedonism score")
parser.add_argument("--self-enhancement", type=int, required=True, help="Self-enhancement score")
parser.add_argument("--self-transcendence", type=int, required=True, help="Self-transcendence score")

args = parser.parse_args()

input_data = pd.DataFrame({
    'Openness': [args.openness],
    'Conscientousness': [args.conscientiousness],
    'Extraversion': [args.extraversion],
    'Agreeableness': [args.agreeableness],
    'Emotional_Range': [args.emotional_range],
    'Conversation': [args.conversation],
    'Openness to Change': [args.openness_to_change],
    'Hedonism': [args.hedonism],
    'Self-enhancement': [args.self_enhancement],
    'Self-transcendence': [args.self_transcendence]
})

prediction = model.predict(input_data)
predicted_role = le.inverse_transform(prediction)

print(f"Predicted Career Role: {predicted_role[0]}")
