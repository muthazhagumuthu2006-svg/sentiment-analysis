# src/config.py

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_RAW = os.path.join(BASE_DIR, "data", "raw", "sample_labeled.csv")
DATA_PROCESSED = os.path.join(BASE_DIR, "data", "processed")
MODELS_DIR = os.path.join(BASE_DIR, "models")

MODEL_FILE = os.path.join(MODELS_DIR, "model.joblib")
LABELS_FILE = os.path.join(MODELS_DIR, "labels.json")
