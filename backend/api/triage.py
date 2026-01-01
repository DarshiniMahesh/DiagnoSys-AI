from fastapi import APIRouter, Body

router = APIRouter(tags=["Triage"])

@router.post("/")
def triage(payload: dict = Body(...)):
    # Example rule-based triage
    confidence = payload["result"]["confidence"]
    label = payload["result"]["label"]
    severity = "urgent" if label in ["melanoma", "pneumonia"] and confidence > 0.85 else "routine"
    return {"severity": severity, "score": confidence}