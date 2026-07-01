from fastapi import FastAPI
from database import engine
import models
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sign Language Learning & Assessment Platform",
    description="AI-powered sign language learning platform",
    version="0.1.0"
)

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Sign Language Platform API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}