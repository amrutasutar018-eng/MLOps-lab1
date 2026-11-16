from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello MLOps Lab 1 - Amruta"}

@app.get("/health")
def health():
    return {"status": "ok"}
