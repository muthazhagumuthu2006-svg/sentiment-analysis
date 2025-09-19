# 📌 Social Media Sentiment Analysis (ML)

A complete end-to-end project for sentiment classification of social media text (positive / negative / neutral) using **Machine Learning**.  

This project covers:
- ✅ Data preprocessing (cleaning, emoji/hashtag/URL handling)  
- ✅ Training ML pipeline (**TF-IDF + Logistic Regression**)  
- ✅ Model evaluation & reporting  
- ✅ Batch and real-time prediction  
- ✅ REST API with **FastAPI**  
- ✅ Demo UI with **Streamlit**  
- ✅ Example dataset included  

---

## 📂 Project Structure

```
sentiment-ml/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   └── sample_labeled.csv
│   └── processed/
├── models/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   ├── api.py
│   └── app_streamlit.py
├── scripts/
│   ├── serve_api.bat
│   ├── serve_api.sh
│   ├── streamlit_app.bat
│   └── streamlit_app.sh
└── tests/
    └── test_preprocess.py
```

---

## ⚙️ Installation

### 1. Clone or copy the repo
```bash
git clone <your-repo-url> sentiment-ml
cd sentiment-ml
```

### 2. Create virtual environment
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

⚠️ If Windows blocks activation, run PowerShell as Admin:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
Then re-activate.

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🏋️ Train the Model

Train with the provided sample dataset:

```bash
python -m src.train --input data/raw/sample_labeled.csv --model_dir models
```

This will create:
- `models/model.joblib` → trained pipeline  
- `models/labels.json` → labels used  

---

## 📊 Evaluate the Model

Check performance metrics:

```bash
python -m src.evaluate --input data/raw/sample_labeled.csv --model_dir models
```

Outputs precision, recall, F1, and confusion matrix.

---

## 🔮 Batch Predictions

Run predictions on a CSV file with a `text` column:

```bash
python -m src.predict --model_dir models --input data/raw/sample_labeled.csv --output data/processed/predictions.csv
```

Output CSV will include:
- `pred_label` → predicted sentiment  
- `pred_confidence` → confidence score  

---

## 🌐 REST API (FastAPI)

Run the API server:

```bash
# Windows
scripts/serve_api.bat

# macOS/Linux
bash scripts/serve_api.sh
```

Open in browser: 👉 http://127.0.0.1:8000/docs  
Use `/predict` endpoint to test.

Example request:
```json
{
  "text": "I love this product!"
}
```

Response:
```json
{
  "label": "positive",
  "confidence": 0.92
}
```

---

## 🖥️ Demo UI (Streamlit)

Launch interactive UI:

```bash
# Windows
scripts/streamlit_app.bat

# macOS/Linux
bash scripts/streamlit_app.sh
```

Then open 👉 http://localhost:8501  

---

## 📂 Data Format

The dataset should be a CSV with:
- `text` → social media post text  
- `label` → `positive`, `negative`, `neutral`  

Example (`data/raw/sample_labeled.csv`):
```csv
text,label
"I love this movie! Absolutely fantastic. 😍",positive
"Worst service ever. I'm never coming back.",negative
"It was okay, nothing special.",neutral
```

---

## 🛠️ Notes
- Baseline pipeline: **TF-IDF + Logistic Regression** (lightweight & deployable).  
- Handles emojis, hashtags, mentions, and URLs.  
- Extend with more data for higher accuracy.  
- Try **transformer models (BERT, RoBERTa)** for state-of-the-art performance.  
- Add multilingual datasets for multi-language support.  

---

## ✅ Quick Test

```bash
# Train
python -m src.train --input data/raw/sample_labeled.csv --model_dir models

# Predict
python -m src.predict --model_dir models --input data/raw/sample_labeled.csv --output data/processed/preds.csv

# Run API
uvicorn src.api:app --reload
# Test at http://127.0.0.1:8000/docs
```

---

## 📜 License
You can freely use and modify this project for personal, educational, or research purposes.
