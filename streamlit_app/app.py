import streamlit as st
import requests

st.set_page_config(page_title="NYC Taxi Trip Duration", layout="centered")

st.title("🚕 NYC Taxi Trip Duration Predictor")
st.write("Predict taxi trip duration using ML (XGBoost)")

API_URL = "http://localhost:8000/predict"

pickup_hour = st.slider("Pickup Hour", 0, 23, 9)
pickup_weekday = st.selectbox("Pickup Weekday (0=Mon)", list(range(7)))
pickup_month = st.selectbox("Pickup Month", list(range(1, 13)))
is_weekend = st.selectbox("Is Weekend", [0, 1])
is_rush_hour = st.selectbox("Is Rush Hour", [0, 1])
passenger_count = st.slider("Passenger Count", 1, 6, 1)
haversine_km = st.number_input("Haversine Distance (km)", value=3.5)
manhattan_dist = st.number_input("Manhattan Distance", value=0.02)

if st.button("Predict Trip Duration"):
   payload = {
      "pickup_hour": pickup_hour,
      "pickup_weekday": pickup_weekday,
      "pickup_month": pickup_month,
      "is_weekend": is_weekend,
      "is_rush_hour": is_rush_hour,
      "passenger_count": passenger_count,
      "haversine_km": haversine_km,
      "manhattan_dist": manhattan_dist
   }

   response = requests.post(API_URL, json=payload)

   if response.status_code == 200:
      prediction = response.json()["predicted_trip_duration_seconds"]
      st.success(f"Estimated Trip Duration: **{prediction} seconds**")
   else:
      st.error("API error. Make sure FastAPI is running.")
