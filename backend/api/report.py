from fastapi import APIRouter, Body
from datetime import datetime

router = APIRouter(tags=["Report"])

@router.post("/")
def generate_report(payload: dict = Body(...)):
    # payload: { patientId, modality, result, heatmapUrl?, history? }
    report = {
        "patientId": payload.get("patientId"),
        "modality": payload.get("modality"),
        "summary": f"AI detected: {payload['result']['label']} (confidence {payload['result']['confidence']:.2f})",
        "details": payload,
        "createdAt": datetime.utcnow().isoformat(),
        "language": payload.get("language", "en"),
    }
    return {"report": report}