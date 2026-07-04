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
│       │   ├── hand_tracking/    # MediaPipe hand tracking
│       │   ├── gesture_recognition/  # Gesture classifier
│       │   └── utils/            # Camera, distance utils
│       ├── auth.py               # JWT authentication
│       ├── models.py             # Database models
│       ├── routes.py             # API endpoints
│       └── main.py               # FastAPI app
├── frontend/                     # React/Next.js (upcoming)
├── ml/
│   ├── datasets/                 # ASL Alphabet + WLASL
│   └── models/                   # Trained model files
├── scripts/                      # Dataset exploration scripts
└── captures/                     # Saved landmark JSON files

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

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/register | User registration |
| POST | /api/auth/login | User login (JWT) |
| POST | /api/profile/create | Create learner profile |
| GET | /api/profile/me | Get learner profile |

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
```

## Mentor

Dikshita Ma'am — Data Scientist, Infosys Springboard 2026