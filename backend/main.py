from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config.settings import settings
from backend.api.analyze import router as analyze_router
from backend.api.report import router as report_router
from backend.api.history import router as history_router
from backend.api.triage import router as triage_router

app = FastAPI(title=settings.API_TITLE)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router, prefix="/api/analyze")
app.include_router(report_router, prefix="/api/report")
app.include_router(history_router, prefix="/api/history")
app.include_router(triage_router, prefix="/api/triage")

@app.get("/")
def root():
    return {"message": "MediScan AI Backend is running"}