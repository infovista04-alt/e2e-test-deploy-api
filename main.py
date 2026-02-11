from fastapi import FastAPI
app = FastAPI(title="E2E Test API")

@app.get("/")
def root():
    return {"message": "E2E Test Deployment", "status": "live", "timestamp": "2026-02-11T14:51:01.020991+00:00"}

@app.get("/health")
def health():
    return {"status": "healthy"}
