import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("🚗 CarDekho Used Car Price Predictor")

year = st.number_input("Year", min_value=1990, max_value=2026, step=1)
kms_driven = st.number_input("Kms Driven", min_value=0)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
# Removed 'present_price' and 'owner' as they are not in the dataset

fuel_map = {"Petrol":0, "Diesel":1, "CNG":2}
seller_map = {"Dealer":0, "Individual":1}
trans_map = {"Manual":0, "Automatic":1}

inputs = np.array([[year,kms_driven,
                    fuel_map[fuel_type], seller_map[seller_type],
                    trans_map[transmission]]])

if st.button("Predict Price"):
    prediction = model.predict(inputs)[0]
    st.success(f"Estimated Selling Price: ₹{prediction:.2f} lakhs")
