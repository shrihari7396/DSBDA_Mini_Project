# ==========================================
# 📧 SPAM SMS DETECTION - BEAUTIFUL UI APP
# WITH ANIMATIONS + PKL MODEL
# ==========================================

import streamlit as st
import re
import string
import joblib
import time

# ---------------------------
# 1. PAGE CONFIGURATION
# ---------------------------
st.set_page_config(
    page_title="Spam SMS Detector",
    page_icon="📧",
    layout="centered"
)

# ---------------------------
# 2. LOAD MODEL
# ---------------------------
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ---------------------------
# 3. CLEAN TEXT FUNCTION
# ---------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# ---------------------------
# 4. HEADER UI (ANIMATED TITLE)
# ---------------------------
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>📧 Spam SMS Detector</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align: center; color: gray;'>AI-powered message classification using Machine Learning</h4>",
    unsafe_allow_html=True
)

st.write("---")

# ---------------------------
# 5. SIDEBAR INFO
# ---------------------------
st.sidebar.title("ℹ About Project")
st.sidebar.write("""
✔ Machine Learning (Naive Bayes)  
✔ NLP Text Processing  
✔ Streamlit UI  
✔ Kaggle Dataset  

Built for academic mini project.
""")

# ---------------------------
# 6. INPUT UI
# ---------------------------
st.markdown("### ✍ Enter your message below:")

user_input = st.text_area("", height=120)

# ---------------------------
# 7. PREDICTION BUTTON
# ---------------------------
if st.button("🚀 Predict Now"):

    if user_input.strip() == "":
        st.warning("⚠ Please enter a message first!")

    else:
        # LOADING ANIMATION
        with st.spinner("🔍 Analyzing message..."):
            time.sleep(1.5)

        cleaned = clean_text(user_input)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]

        st.write("---")

        # ---------------------------
        # RESULT UI CARD
        # ---------------------------
        if prediction == "spam":

            st.markdown(
                """
                <div style="
                    padding:20px;
                    border-radius:10px;
                    background-color:#ffebee;
                    border:2px solid red;
                    text-align:center;">
                    <h2 style="color:red;">🚫 SPAM DETECTED</h2>
                    <p>This message looks like a spam or scam attempt.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.image(
                "https://cdn-icons-png.flaticon.com/512/564/564619.png",
                width=120
            )

        else:

            st.markdown(
                """
                <div style="
                    padding:20px;
                    border-radius:10px;
                    background-color:#e8f5e9;
                    border:2px solid green;
                    text-align:center;">
                    <h2 style="color:green;">✅ SAFE MESSAGE</h2>
                    <p>This message is normal and not spam.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.image(
                "https://cdn-icons-png.flaticon.com/512/190/190411.png",
                width=120
            )

            # 🎉 SUCCESS ANIMATION
            st.balloons()

# ---------------------------
# 8. FOOTER
# ---------------------------
st.write("---")
st.markdown(
    "<p style='text-align:center;color:gray;'>Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)