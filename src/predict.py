# src/predict.py

import argparse
import pandas as pd
import joblib
from src.preprocess import clean_text
from src import config

def predict(input_file, model_dir, output_file):
    df = pd.read_csv(input_file)
    df["text"] = df["text"].apply(clean_text)

    model = joblib.load(config.MODEL_FILE)
    preds = model.predict(df["text"])
    probs = model.predict_proba(df["text"]).max(axis=1)

    df["pred_label"] = preds
    df["pred_confidence"] = probs

    df.to_csv(output_file, index=False)
    print(f"✅ Predictions saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=config.DATA_RAW)
    parser.add_argument("--model_dir", default=config.MODELS_DIR)
    parser.add_argument("--output", default=f"{config.DATA_PROCESSED}/predictions.csv")
    args = parser.parse_args()

    predict(args.input, args.model_dir, args.output)
