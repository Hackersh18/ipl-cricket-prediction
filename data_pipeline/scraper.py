import pandas as pd

# Simulate scrape
def scrape_mock_data():
    return pd.DataFrame({
        'team1_score': [150],
        'team2_score': [145],
        'team1_win_ratio': [0.6],
        'team2_win_ratio': [0.5],
        'venue_avg_score': [155]
    })
