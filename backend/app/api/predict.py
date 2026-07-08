from fastapi import APIRouter
from services.gesture_service import GestureService
from schemas.prediction import PredictionResponse

router = APIRouter()
gesture_service = GestureService()

@router.post("/predict", response_model=PredictionResponse)
def predict():
    result = gesture_service.predict()
    return result