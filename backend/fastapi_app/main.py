from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load('ml_models/model.pkl')

class MatchInput(BaseModel):
    team1_score: int
    team2_score: int
    team1_win_ratio: float
    team2_win_ratio: float
    venue_avg_score: int

@app.post("/predict")
def predict(data: MatchInput):
    input_data = np.array([[
        data.team1_score, data.team2_score, 
        data.team1_win_ratio, data.team2_win_ratio, 
        data.venue_avg_score
    ]])
    prediction = model.predict(input_data)
    return {"predicted_winner": "team1" if prediction[0] == 1 else "team2"}