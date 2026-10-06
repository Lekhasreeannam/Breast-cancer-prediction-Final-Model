import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Load Model, Scaler and Features
# -----------------------------
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

with open("features.pkl", "rb") as file:
    feature_names = pickle.load(file)

# -----------------------------
# Page Title
# -----------------------------
st.set_page_config(page_title="Breast Cancer Prediction", page_icon="🩺")

st.title("🩺 Breast Cancer Prediction")
st.write("Enter the feature values below to predict whether the tumor is **Benign** or **Malignant**.")

st.divider()

# -----------------------------
# User Inputs
# -----------------------------
input_data = {}

for feature in feature_names:
    input_data[feature] = st.number_input(feature, value=0.0)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):

    input_df = pd.DataFrame([input_data])

    # Scale Input
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)

    
    st.subheader("Prediction")

    if prediction[0] == 1:
        st.error("🔴 Malignant Tumor")
    else:
        st.success("🟢 Benign Tumor")

    