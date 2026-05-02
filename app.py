import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("models/house_model.pkl")

st.set_page_config(page_title="House Price Predictor", layout="centered")

st.title("🏠 House Price Prediction System")

st.write("Enter house details to predict price")

# Inputs
area = st.slider("Area (sq ft)", 500, 5000, 2000)
bedrooms = st.slider("Bedrooms", 1, 5, 3)
bathrooms = st.slider("Bathrooms", 1, 4, 2)
age = st.slider("Age of House", 0, 30, 5)
parking = st.selectbox("Parking Available", [0, 1])

# Prediction
if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms, age, parking]])
    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated Price: ₹ {int(prediction):,}")