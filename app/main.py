from fastapi import FastAPI
from app.routers import health

app = FastAPI(title="Freelance FastAPI Backend")

app.include_router(health.router)

@app.get("/")
def root():
    return {"status": "running"}
