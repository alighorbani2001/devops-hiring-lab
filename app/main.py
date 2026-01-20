from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DevOps Hiring Lab - FastAPI"}

@app.get("/health")
def health():
    return {"status": "ok"}

