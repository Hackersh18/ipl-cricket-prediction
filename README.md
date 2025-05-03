# IPL Cricket Prediction System - Full Stack AI Solution
# Technologies: Python, Django, FastAPI, scikit-learn, PyTorch, React.js, PostgreSQL, Docker

# -----------------------------
# README.md
# -----------------------------

# IPL Cricket Match Prediction System

This is a full-stack AI system to predict IPL cricket match outcomes, built with an ensemble machine learning model, served via Django and FastAPI backends, a React.js frontend, and deployed using Docker.

## 🧠 Features
- Predict winning team using mock IPL data
- REST API with FastAPI and Django
- React frontend interface
- Dockerized for easy deployment

## 📁 Project Structure
```
ipl-cricket-prediction/
├── backend/
│   ├── django_app/
│   ├── fastapi_app/
│   └── requirements.txt
├── ml_models/
│   ├── train.py
│   └── model.pkl
├── data_pipeline/
│   └── scraper.py
├── frontend/
│   ├── package.json
│   └── src/
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone <your_repo_url>
cd ipl-cricket-prediction
```

### 2. Train the ML Model
```bash
python ml_models/train.py
```

### 3. Run FastAPI Backend
```bash
uvicorn backend.fastapi_app.main:app --reload
```

### 4. Run Django Backend
```bash
cd backend/django_app
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 5. Run React Frontend
```bash
cd frontend
npm install
npm run start
```

### 6. Run with Docker
```bash
docker-compose up --build
```

## 🔧 API Endpoints
### FastAPI
- POST `/predict` — returns predicted winner

### Django
- POST `/predict_django` — saves and returns prediction

## 📦 Tech Stack
- **ML Model**: Scikit-learn (Gradient Boosting)
- **Backend**: FastAPI + Django REST
- **Frontend**: React.js
- **Database**: PostgreSQL (via Django ORM)
- **Deployment**: Docker + docker-compose

## 📌 Notes
- This uses mock IPL data for demonstration.
- Extend with real data by modifying the `data_pipeline/scraper.py`
- Add Ollama LLM reasoning in `model_service.py` (optional)

## 🤝 Contributing
Fork the repo, create a branch, and submit a PR!

## 📫 Contact
For questions, reach out to the hiring team at [Artizence Systems LLP](https://artizence.com)

---

Now you’re ready to upload to GitHub! ✅
