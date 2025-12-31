import joblib
import pandas as pd
from fastapi import FastAPI
from api.schemas import TripRequest

app = FastAPI(
   title="NYC Taxi Trip Duration Prediction API",
   description="Predict taxi trip duration using XGBoost model",
   version="1.0"
)

# Load trained model
model = joblib.load("models/xgboost_trip_duration.pkl")

@app.get("/")
def home():
   return {"message": "NYC Taxi Trip Duration Prediction API is running"}

@app.post("/predict")
def predict_trip_duration(request: TripRequest):
   input_data = pd.DataFrame([{
      "pickup_hour": request.pickup_hour,
      "pickup_weekday": request.pickup_weekday,
      "pickup_month": request.pickup_month,
      "is_weekend": request.is_weekend,
      "is_rush_hour": request.is_rush_hour,
      "passenger_count": request.passenger_count,
      "haversine_km": request.haversine_km,
      "manhattan_dist": request.manhattan_dist
   }])

   prediction = model.predict(input_data)[0]

   return {
      "predicted_trip_duration_seconds": round(float(prediction), 2)
   }
