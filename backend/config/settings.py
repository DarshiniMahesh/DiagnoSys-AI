class Settings:
    API_TITLE = "MediScan AI Backend"
    ALLOWED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]

    # Storage
    USE_S3 = False
    S3_BUCKET = "mediscan-bucket"
    S3_REGION = "ap-south-1"

    # Databases
    POSTGRES_URL = "postgresql://user:password@localhost:5432/mediscan"
    MONGO_URL = "mongodb://localhost:27017"
    MONGO_DB = "mediscan"

    # Models
    MODEL_PATHS = {
        "chest_xray": "models/chest_xray/best_model.pt",
        "skin_lesion": "models/skin_lesion/best_model.pt",
        "diabetic_retinopathy": "models/diabetic_retinopathy/best_model.pt",
    }

settings = Settings()