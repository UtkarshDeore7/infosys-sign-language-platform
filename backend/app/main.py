from fastapi import FastAPI

app = FastAPI(
    title="Sign Language Learning & Assessment Platform",
    description="AI-powered sign language learning platform",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Sign Language Platform API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}