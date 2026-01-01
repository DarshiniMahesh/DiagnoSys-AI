from fastapi import APIRouter, Query

router = APIRouter(tags=["History"])

@router.get("/")
def get_history(patientId: str = Query(...)):
    # Replace with DB query (Postgres/Mongo)
    return {"patientId": patientId, "records": []}