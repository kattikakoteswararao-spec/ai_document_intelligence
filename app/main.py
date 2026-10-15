from fastapi import FastAPI

from app.routers. documents import router as documents_router

app = FastAPI(
    title="AI Document Intelligence Pipeline",
    description="API for processing and analyzing documents",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "AI Document Intelligence Pipeline is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

app.include_router(documents_router)