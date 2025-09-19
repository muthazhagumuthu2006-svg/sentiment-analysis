# src/evaluate.py

import argparse
import pandas as pd
import joblib
from sklearn.metrics import classification_report
from src.preprocess import clean_text
from src import config

def evaluate(input_file, model_dir):
    df = pd.read_csv(input_file)
    df["text"] = df["text"].apply(clean_text)

    model = joblib.load(config.MODEL_FILE)
    y_pred = model.predict(df["text"])

    print("📊 Classification Report:")
    print(classification_report(df["label"], y_pred))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=config.DATA_RAW)
    parser.add_argument("--model_dir", default=config.MODELS_DIR)
    args = parser.parse_args()

    evaluate(args.input, args.model_dir)
