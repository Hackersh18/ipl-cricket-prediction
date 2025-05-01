from django.db import models

class Match(models.Model):
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()
    team1_win_ratio = models.FloatField()
    team2_win_ratio = models.FloatField()
    venue_avg_score = models.IntegerField()
    predicted_winner = models.CharField(max_length=50)

# Directory: backend/django_app/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Match
from .serializers import MatchSerializer
import joblib
import numpy as np

model = joblib.load('ml_models/model.pkl')

class PredictMatch(APIView):
    def post(self, request):
        data = request.data
        input_data = np.array([[
            data['team1_score'], data['team2_score'],
            data['team1_win_ratio'], data['team2_win_ratio'],
            data['venue_avg_score']
        ]])
        prediction = model.predict(input_data)
        winner = 'team1' if prediction[0] == 1 else 'team2'
        match = Match.objects.create(
            team1=data['team1'],
            team2=data['team2'],
            team1_score=data['team1_score'],
            team2_score=data['team2_score'],
            team1_win_ratio=data['team1_win_ratio'],
            team2_win_ratio=data['team2_win_ratio'],
            venue_avg_score=data['venue_avg_score'],
            predicted_winner=winner
        )
        return Response({"predicted_winner": winner})
