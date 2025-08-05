
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib
import os

data_path = os.path.join("model_training", "data", "CareerMap- Mapping Tech Roles With Personality & Skills.csv")
artifacts_path = os.path.join("model_training", "artifacts")

os.makedirs(artifacts_path, exist_ok=True)

try:
    df = pd.read_csv(data_path)
except FileNotFoundError:
    print(f"Error: The dataset was not found at {data_path}")
    exit()


features = ['Openness', 'Conscientousness', 'Extraversion', 'Agreeableness', 'Emotional_Range', 'Conversation', 'Openness to Change', 'Hedonism', 'Self-enhancement', 'Self-transcendence']
target = 'Role'

if target not in df.columns or not all(f in df.columns for f in features):
    print("Error: The specified feature or target columns are not in the dataset.")
    # As a fallback, let's use the first 5 columns as features and the last column as the target
    features = df.columns[:5].tolist()
    target = df.columns[-1]
    print(f"Using fallback features: {features} and target: {target}")



le = LabelEncoder()
df[target] = le.fit_transform(df[target])


X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

joblib.dump(model, os.path.join(artifacts_path, "model.pkl"))
joblib.dump(le, os.path.join(artifacts_path, "label_encoder.pkl"))

print("Model training complete and artifacts saved.")
