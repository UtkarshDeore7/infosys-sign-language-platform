# Sign Language Learning & Assessment Platform

AI-powered sign language learning platform built during the Infosys Springboard Internship 2026.

## Project Overview

This platform helps users learn sign language through real-time gesture recognition, AI-driven feedback, and performance assessments using computer vision and deep learning.

## Tech Stack

**Backend:** Python, FastAPI, PostgreSQL, MongoDB  
**Frontend:** React.js, Next.js, Tailwind CSS  
**AI/ML:** MediaPipe, TensorFlow, OpenCV, CNN/LSTM  
**Auth:** JWT, OAuth2  
**DevOps:** Docker, GitHub Actions  

## Project Structure

infosys-sign-language-platform/
├── backend/
│   └── app/
│       ├── ai/
│       │   ├── hand_tracking/     # MediaPipe hand tracking
│       │   ├── gesture_recognition/
│       │   └── utils/             # Camera, distance utils
│       ├── api/                   # Route handlers
│       ├── content/               # Lesson service
│       ├── services/              # Business logic
│       ├── schemas/               # Pydantic models
│       ├── core/                  # Core utilities
│       ├── utils/                 # Shared utilities
│       ├── auth.py                # JWT authentication
│       ├── database.py            # DB connection
│       ├── models.py              # SQLAlchemy models
│       └── main.py                # FastAPI app
├── frontend/                      # React/Next.js (upcoming)
├── ml/
│   ├── datasets/                  # ASL Alphabet + WLASL
│   ├── models/                    # Trained model files
│   └── training/                  # Extracted landmarks + reports
├── scripts/                       # Dataset processing scripts
└── captures/                      # Saved landmark JSON files

## Milestones

| Milestone | Week | Status |
|-----------|------|--------|
| Project Setup + Auth + DB | 1-2 | ✅ Complete |
| Gesture Recognition Engine | 3-4 | 🔄 In Progress |
| AI Feedback + Learning Intelligence | 5-6 | ⬜ Upcoming |
| Certification + Deployment | 7-8 | ⬜ Upcoming |

## Datasets

- **ASL Alphabet** — 87,000 images, 29 classes, 200x200px
- **WLASL** — 2,000 word-level signs, video format
- **Landmarks CSV** — 63,580 extracted samples (73% success rate)

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/health | Backend health check |
| POST | /api/auth/register | User registration |
| POST | /api/auth/login | User login (JWT) |
| POST | /api/profile/create | Create learner profile |
| GET | /api/profile/me | Get learner profile |
| GET | /api/lessons | Get all lessons |
| GET | /api/lessons/{id} | Get lesson details |
| POST | /api/sessions/start/{id} | Start practice session |
| PUT | /api/sessions/end/{id} | End practice session |
| GET | /api/sessions/{id} | Get session details |
| POST | /api/predict | Gesture prediction |
| POST | /api/preprocess | Run dataset preprocessing |

## Setup

```bash
# Clone repo
git clone https://github.com/UtkarshDeore7/infosys-sign-language-platform.git
cd infosys-sign-language-platform

# Setup backend
cd backend
py -3.11 -m venv venv
venv\Scripts\activate
pip install -r app/requirements.txt

# Run server
cd app
uvicorn main:app --reload

# Test API docs
# Open http://127.0.0.1:8000/docs
```

## Mentor

Dikshita Ma'am — Data Scientist, Infosys Springboard 2026