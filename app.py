import streamlit as st
import joblib
import numpy as np

# Load model and label encoder
model = joblib.load("crop_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Page config
st.set_page_config(page_title="🌾 Crop Recommender", layout="centered")

# New solid cream background + green text
st.markdown("""
    <style>
    .stApp {
        background-color: #pink;
        font-family: 'Arial';
    }
    .title-text {
        color: #white;
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle-text {
        color: #white;
        text-align: center;
        font-size: 20px;
        margin-bottom: 30px;
    }
    .result-box {
        background-color: #588157;
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    label, .stNumberInput > div {
        color: #1b4332;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown('<div class="title-text">🌱 Smart Crop Recommendation</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Find the best crop based on your soil and weather conditions 🌧️☀️</div>', unsafe_allow_html=True)

# Input panel
with st.expander("📋 Fill Your Field Details"):
    N = st.number_input("🧪 Nitrogen (N)", min_value=0, max_value=140, step=1)
    P = st.number_input("🧪 Phosphorus (P)", min_value=0, max_value=145, step=1)
    K = st.number_input("🧪 Potassium (K)", min_value=0, max_value=205, step=1)
    temperature = st.number_input("🌡️ Temperature (°C)", min_value=10.0, max_value=50.0, step=0.1)
    humidity = st.number_input("💧 Humidity (%)", min_value=10.0, max_value=100.0, step=0.1)
    ph = st.number_input("🧪 Soil pH", min_value=3.5, max_value=9.5, step=0.1)
    rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=20.0, max_value=300.0, step=0.1)

# Prediction
if st.button("🚀 Recommend My Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    crop = label_encoder.inverse_transform(prediction)[0]

    st.markdown(f'<div class="result-box">✅ Recommended Crop: <span style="color: #ffd60a;">{crop}</span></div>', unsafe_allow_html=True)
