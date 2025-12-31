import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.data_preprocessing import load_and_clean_data
from src.feature_engineering import create_features
from src.model_training import train_model

RAW_DATA_PATH = "data/raw/nyc_taxi_trip_duration.csv"
PROCESSED_PATH = "data/processed/processed_data.csv"

os.makedirs("data/processed", exist_ok=True)

df = load_and_clean_data(RAW_DATA_PATH)
X, y = create_features(df)

# Save processed data
processed_df = X.copy()
processed_df["trip_duration"] = y
processed_df.to_csv(PROCESSED_PATH, index=False)

train_model(X, y)
