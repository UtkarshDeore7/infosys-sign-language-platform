# Sign Language Learning & Assessment Platform

AI-powered sign language learning platform built during the Infosys Springboard Internship 2026.

## Project Overview

This platform helps users learn sign language through real-time gesture recognition, AI-driven feedback, and performance assessments using computer vision and deep learning.

## Tech Stack

**Backend:** Python, FastAPI, PostgreSQL, MongoDB  
**Frontend:** React.js, Next.js, Tailwind CSS (upcoming)  
**AI/ML:** MediaPipe, Random Forest, TensorFlow, OpenCV  
**Auth:** JWT, OAuth2  
**DevOps:** Docker, GitHub Actions  

## Project Structure

infosys-sign-language-platform/
├── backend/
│   └── app/
│       ├── ai/
│       │   ├── hand_tracking/        # MediaPipe hand detection
│       │   ├── gesture_recognition/  # Gesture classifier
│       │   ├── ml/
│       │   │   ├── inference/        # Pipeline, GestureEngine, SequenceBuilder
│       │   │   ├── preprocessing/    # Normalization
│       │   │   ├── training/         # Model training
│       │   │   └── evaluation/       # Metrics
│       │   └── utils/                # Camera, distance utils
│       ├── api/                      # Route handlers
│       ├── content/                  # Lesson service
│       ├── services/                 # Business logic
│       ├── schemas/                  # Pydantic models
│       ├── core/                     # Core utilities
│       └── utils/                    # Shared utilities
├── ml/
│   ├── datasets/                     # ASL Alphabet + WLASL
│   ├── models/                       # gesture_classifier.pkl
│   └── training/                     # CSV files + reports
├── preprocessing/                    # Normalization + split scripts
├── scripts/                          # Data exploration utilities
├── experiments/
│   └── experiment_001/               # Training run tracking
└── captures/                         # Saved landmark JSON files

## Milestones

| Milestone | Week | Status |
|-----------|------|--------|
| Project Setup + Auth + DB | 1-2 | ✅ Complete |
| Gesture Recognition Engine | 3-4 | ✅ Complete |
| AI Feedback + Learning Intelligence | 5-6 | ⬜ Upcoming |
| Certification + Deployment | 7-8 | ⬜ Upcoming |

## Model Performance

| Classifier | Accuracy | F1 Score | Training Time |
|-----------|---------|---------|--------------|
| Random Forest (100 trees) | 98.64% | 98.64% | 65s |
| KNN (k=5) | 98.58% | 98.58% | 0.13s |
| Decision Tree | 96.98% | 96.98% | 11s |

**Best Model:** Random Forest — 98.64% accuracy

## Inference Benchmark

| Metric | Value |
|--------|-------|
| Average Inference Time | 4.94 ms |
| Throughput | 202 predictions/sec |
| Memory Used | 0.32 MB |
| Model Size | 72 MB |
| Real-time Suitable | ✅ Yes (under 33ms) |

## Datasets

- **ASL Alphabet** — 87,000 images, 29 classes, 200x200px
- **WLASL** — 2,000 word-level signs, video format
- **Landmarks CSV** — 63,580 extracted samples (73% success rate)
- **Train/Val/Test** — 44,505 / 9,537 / 9,537 (stratified 70/15/15)

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

## AI Pipeline

Image/Frame → MediaPipe → 21 Landmarks → Validation →
Wrist-Relative Normalization → 63 Feature Vector →
Random Forest → Prediction + Confidence → Structured Response

## Future Pipeline (LSTM/GRU)

Webcam → Frame Buffer (20 frames) → Sequence (20×63) →
LSTM/GRU → Continuous Sign Recognition → Sentence Formation

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