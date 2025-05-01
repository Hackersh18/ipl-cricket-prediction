import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# Mock dataset
np.random.seed(42)
data = pd.DataFrame({
    'team1_score': np.random.randint(100, 200, 100),
    'team2_score': np.random.randint(100, 200, 100),
    'team1_win_ratio': np.random.rand(100),
    'team2_win_ratio': np.random.rand(100),
    'venue_avg_score': np.random.randint(130, 180, 100),
    'winner': np.random.randint(0, 2, 100)  # 0: team2, 1: team1
})

X = data.drop('winner', axis=1)
y = data['winner']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GradientBoostingClassifier()
model.fit(X_train, y_train)

# Save model
os.makedirs('ml_models', exist_ok=True)
joblib.dump(model, 'ml_models/model.pkl')

# Evaluate
preds = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))