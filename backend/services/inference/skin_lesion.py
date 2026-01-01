import torch
from torchvision import transforms
from PIL import Image

class SkinLesionModel:
    def __init__(self, model_path: str):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = torch.jit.load(model_path, map_location=self.device) if model_path.endswith(".jit") \
            else torch.load(model_path, map_location=self.device)
        self.model.eval()
        self.model.to(self.device)
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225]),
        ])
        self.classes = ["benign", "melanoma", "bcc", "akiec", "df", "nv", "vasc"]

    def predict(self, image_bytes: bytes):
        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        tensor = self.transform(image).unsqueeze(0).to(self.device)
        with torch.no_grad():
            logits = self.model(tensor)
            probs = torch.softmax(logits, dim=1).squeeze().cpu().numpy()
        idx = int(probs.argmax())
        return {"label": self.classes[idx], "confidence": float(probs[idx]), "probs": probs.tolist()}