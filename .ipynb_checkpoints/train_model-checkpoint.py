import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Load the dataset [cite: 183, 218]
data = pd.read_csv("traffic_dataset.csv")

# 2. Feature selection (Time, Weather, Vehicle Density) [cite: 148, 149, 225]
X = data[['time', 'weather', 'vehicle_count']]
y = data['traffic_level']

# 3. Train-Test Split (80% Training, 20% Testing) [cite: 154, 186, 220]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and train Random Forest Classifier [cite: 191, 221]
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 5. Save the trained model as a .pkl file for deployment [cite: 189, 223, 226]
joblib.dump(model, "traffic_model.pkl")
print("Model trained and saved successfully as traffic_model.pkl")