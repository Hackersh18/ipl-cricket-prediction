import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [winner, setWinner] = useState('');

  const predict = async () => {
    const res = await axios.post('http://localhost:8000/predict', {
      team1_score: 160,
      team2_score: 150,
      team1_win_ratio: 0.65,
      team2_win_ratio: 0.6,
      venue_avg_score: 155
    });
    setWinner(res.data.predicted_winner);
  };

  return (
    <div className="p-5">
      <h1>IPL Match Predictor</h1>
      <button onClick={predict}>Predict</button>
      <p>Predicted Winner: {winner}</p>
    </div>
  );
}

export default App;