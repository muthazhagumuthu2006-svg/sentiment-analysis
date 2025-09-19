# src/preprocess.py

import re
import emoji

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    # Remove mentions and hashtags
    text = re.sub(r"[@#]\w+", "", text)
    # Convert emojis to text
    text = emoji.demojize(text, delimiters=(" ", " "))
    # Remove non-alphanumeric except punctuation
    text = re.sub(r"[^a-zA-Z0-9\s.,!?']", " ", text)
    # Normalize spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text
