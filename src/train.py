# src/train.py

import argparse
import pandas as pd
import joblib
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from src.preprocess import clean_text
from src import config

def train(input_file, model_dir):
    df = pd.read_csv(input_file)
    df["text"] = df["text"].apply(clean_text)

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=5000)),
        ("clf", LogisticRegression(max_iter=200))
    ])

    pipeline.fit(df["text"], df["label"])

    # Save model
    joblib.dump(pipeline, config.MODEL_FILE)

    # Save labels
    labels = sorted(df["label"].unique().tolist())
    with open(config.LABELS_FILE, "w") as f:
        json.dump({"labels": labels}, f)

    print(f"✅ Model trained and saved to {config.MODEL_FILE}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=config.DATA_RAW)
    parser.add_argument("--model_dir", default=config.MODELS_DIR)
    args = parser.parse_args()

    train(args.input, args.model_dir)
