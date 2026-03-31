import streamlit as st
import pandas as pd
import joblib

try:
    model = joblib.load("model/full_model.pkl")
except FileNotFoundError:
    st.error("Model not found. Please train the model first by running main.ipynb.")
    st.stop()

st.title("🏠 House Price Prediction")

# Inputs
longitude = st.number_input("Longitude")
latitude = st.number_input("Latitude")
housing_median_age = st.number_input("Housing Median Age", min_value=0)
total_rooms = st.number_input("Total Rooms", min_value=0)
total_bedrooms = st.number_input("Total Bedrooms", min_value=0)
population = st.number_input("Population", min_value=0)
households = st.number_input("Households", min_value=1)
median_income = st.number_input("Median Income")

ocean_proximity = st.selectbox(
    "Ocean Proximity",
    ["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"]
)

# Feature engineering
rooms_per_household = total_rooms / households
bedrooms_per_room = total_bedrooms / total_rooms if total_rooms != 0 else 0
population_per_household = population / households

# DataFrame
input_data = pd.DataFrame({
    "longitude": [longitude],
    "latitude": [latitude],
    "housing_median_age": [housing_median_age],
    "total_rooms": [total_rooms],
    "total_bedrooms": [total_bedrooms],
    "population": [population],
    "households": [households],
    "median_income": [median_income],
    "ocean_proximity": [ocean_proximity],
    "rooms_per_household": [rooms_per_household],
    "bedrooms_per_room": [bedrooms_per_room],
    "population_per_household": [population_per_household]
})

    
# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: {prediction[0]:,.2f}")