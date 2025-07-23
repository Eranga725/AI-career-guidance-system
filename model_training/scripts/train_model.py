
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Define paths
data_path = os.path.join("model_training", "data", "CareerMap- Mapping Tech Roles With Personality & Skills.csv")
artifacts_path = os.path.join("model_training", "artifacts")

# Create artifacts directory if it doesn't exist
os.makedirs(artifacts_path, exist_ok=True)

# Load the dataset
try:
    df = pd.read_csv(data_path)
except FileNotFoundError:
    print(f"Error: The dataset was not found at {data_path}")
    exit()

# For simplicity, let's assume the target variable is 'Role' and features are the personality traits.
# You should adjust these based on your actual dataset columns.
features = ['Openness', 'Conscientousness', 'Extraversion', 'Agreeableness', 'Emotional_Range', 'Conversation', 'Openness to Change', 'Hedonism', 'Self-enhancement', 'Self-transcendence']
target = 'Role'

# Check if required columns exist
if target not in df.columns or not all(f in df.columns for f in features):
    print("Error: The specified feature or target columns are not in the dataset.")
    # As a fallback, let's use the first 5 columns as features and the last column as the target
    features = df.columns[:5].tolist()
    target = df.columns[-1]
    print(f"Using fallback features: {features} and target: {target}")


# Preprocessing
# Encoding the target variable
le = LabelEncoder()
df[target] = le.fit_transform(df[target])

# Splitting the data
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

# Save the model and label encoder
joblib.dump(model, os.path.join(artifacts_path, "model.pkl"))
joblib.dump(le, os.path.join(artifacts_path, "label_encoder.pkl"))

print("Model training complete and artifacts saved.")
