from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.config.settings import settings
from backend.services.inference.skin_lesion import SkinLesionModel
from backend.services.inference.chest_xray import ChestXRayModel  # implement similarly
from backend.services.inference.diabetic_retinopathy import DRModel  # implement similarly

router = APIRouter(tags=["Analyze"])

# Lazy singletons
_models = {"skin_lesion": None, "chest_xray": None, "diabetic_retinopathy": None}

def get_model(modality: str):
    if modality not in _models:
        raise HTTPException(status_code=400, detail="Unsupported modality")
    if _models[modality] is None:
        path = settings.MODEL_PATHS[modality]
        if modality == "skin_lesion":
            _models[modality] = SkinLesionModel(path)
        elif modality == "chest_xray":
            _models[modality] = ChestXRayModel(path)
        else:
            _models[modality] = DRModel(path)
    return _models[modality]

@router.post("/{modality}")
async def analyze(modality: str, file: UploadFile = File(...)):
    try:
        content = await file.read()
        model = get_model(modality)
        result = model.predict(content)
        return {"modality": modality, "filename": file.filename, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")