# src/api.py

from fastapi import FastAPI
import joblib
from pydantic import BaseModel
from src.preprocess import clean_text
from src import config

app = FastAPI(title="Social Media Sentiment API")

# Load model
model = joblib.load(config.MODEL_FILE)

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(item: InputText):
    cleaned = clean_text(item.text)
    pred = model.predict([cleaned])[0]
    prob = model.predict_proba([cleaned]).max()
    return {"label": pred, "confidence": float(prob)}
