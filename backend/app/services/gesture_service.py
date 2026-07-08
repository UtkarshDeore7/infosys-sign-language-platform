import time

class GestureService:
    def __init__(self):
        # HandTracker will be initialized when real model is ready
        self.tracker = None

    def predict(self, image_bytes: bytes = None):
        start_time = time.time()

        # Stub — real classifier replaces this in Week 3
        prediction = "A"
        confidence = 0.95

        processing_time = round(time.time() - start_time, 4)

        return {
            "prediction": prediction,
            "confidence": confidence,
            "processing_time": processing_time
        }