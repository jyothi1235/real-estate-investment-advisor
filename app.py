import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load models
reg = joblib.load("reg_model.pkl")
clf = joblib.load("clf_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

st.title("🏠 Real Estate Investment Advisor")

# User Inputs
sqft = st.number_input("Size (SqFt)", min_value=100)
price = st.number_input("Current Price (Lakhs)", min_value=1)
schools = st.number_input("Nearby Schools", min_value=0)
amenities = st.number_input("Amenities Count", min_value=0)

if st.button("Predict"):

    # 🔹 Create empty dataframe with ALL features
    input_df = pd.DataFrame(columns=features)
    input_df.loc[0] = 0

    # 🔹 Fill only known features
    input_df["Size_in_SqFt"] = sqft
    input_df["Price_in_Lakhs"] = price
    input_df["Nearby_Schools"] = schools
    input_df["Amenities_Count"] = amenities

    # 🔹 Feature engineering (same as training)
    input_df["Price_per_SqFt"] = (price * 100000) / (sqft + 1)
    input_df["Age_of_Property"] = 2026 - 2015  # default assumption
    input_df["School_Score"] = schools / (sqft + 1)

    # 🔹 Scale
    input_scaled = scaler.transform(input_df)

    # 🔹 Predictions
    future_price = reg.predict(input_scaled)
    investment = clf.predict(input_scaled)

    # 🔹 Output
    st.subheader("Results")
    st.write(f"💰 Estimated Price after 5 Years: {future_price[0]:.2f} Lakhs")

    if investment[0] == 1:
        st.success("✅ Good Investment")
    else:
        st.error("❌ Not a Good Investment")