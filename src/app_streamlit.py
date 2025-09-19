import streamlit as st
import joblib
from src.preprocess import clean_text

# Dummy username/password (replace later with DB/file if needed)
USER_CREDENTIALS = {"admin": "password123", "user": "test123"}

# Login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.logged_in = True
            st.success("Login successful ✅")
        else:
            st.error("Invalid username or password ❌")

else:
    # After login → show sentiment analysis page
    st.title("💬 Social Media Sentiment Analysis")
    model = joblib.load("models/model.joblib")

    text = st.text_area("Enter a social media post:")
    if st.button("Analyze"):
        if text.strip():
            cleaned = clean_text(text)

            # Prediction label
            pred = model.predict([cleaned])[0]

            # Prediction probabilities
            if hasattr(model, "predict_proba"):
                proba = model.predict_proba([cleaned])[0]
                positive_score = round(proba[1] * 100, 2)
                negative_score = round(proba[0] * 100, 2)

                st.write(f"**Prediction:** {pred}")
                st.write(f"✅ Positive: {positive_score}%")
                st.write(f"❌ Negative: {negative_score}%")

                # Optional: progress bar
                st.progress(int(positive_score))
            else:
                st.write(f"**Prediction:** {pred}")
