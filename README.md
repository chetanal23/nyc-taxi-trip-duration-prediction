# 🚕 NYC Taxi Trip Duration Prediction
End-to-End Machine Learning Project 

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EB5B2D?style=for-the-badge&logo=xgboost&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

An end-to-end **Machine Learning Regression System** to predict taxi trip duration using real-world NYC taxi data.  
The project follows **industry-grade ML engineering practices**, including modular code, FastAPI inference, Dockerization, and a Streamlit UI.

---

## 🎯 Problem Statement

Ride-hailing platforms like **Uber and Ola** need to estimate how long a driver will be occupied with a trip in order to optimize:

- Driver dispatching
- Passenger wait time
- Fleet utilization
- Overall operational efficiency

The goal of this project is to **predict the taxi trip duration (in seconds)** using historical trip data.

---

## 📊 Dataset Information

- **Source**: NYC Taxi Trip Duration Dataset
- **Size**: ~729,000 rows × 11 columns
- **Target Variable**: `trip_duration`

Key features include:
- Pickup & drop-off locations (latitude, longitude)
- Pickup datetime
- Passenger count
- Vendor information

---

## 🔍 Exploratory Data Analysis (EDA)

EDA was performed to:
- Identify and remove outliers
- Analyze trip duration distribution
- Understand time-based traffic patterns
- Validate geographical bounds of NYC

Key insights from EDA:
- Extremely short and very long trips were treated as outliers
- Rush-hour trips tend to have longer durations
- Distance is the most important factor affecting trip duration

---

## 🛠️ Feature Engineering

The following features were engineered based on EDA insights:

### Time-Based Features
- Pickup hour
- Day of week
- Month
- Weekend indicator
- Rush-hour indicator

### Distance-Based Features
- Haversine distance (great-circle distance)
- Manhattan distance approximation

---

## 🤖 Model Used

- **XGBoost Regressor**

### Why XGBoost?
- Handles non-linear relationships effectively
- Performs exceptionally well on structured/tabular data
- Widely used in industry and Kaggle competitions

### 📈 Model Performance

- **RMSE:** ≈ 351 seconds (~5.8 minutes)  
- **R² Score:** ≈ 0.72  

---

## 🧱 Project Structure
```text
nyc-taxi-trip-duration/
│
├── api/
│   ├── app.py
│   │   └── FastAPI application for model inference
│   └── schemas.py
│       └── Pydantic schema for request validation
│
├── data/
│   ├── raw/
│   │   └── nyc_taxi_trip_duration.csv   # Raw dataset (ignored in GitHub)
│   └── processed/
│       └── processed_data.csv           # Cleaned & feature-engineered data
│
├── notebooks/
│   └── NYC_Taxi_Trip_Duration_EDA.ipynb
│       └── Exploratory Data Analysis and insights
│
├── src/
│   ├── __init__.py
│   │   └── Marks src as a Python package
│   ├── utils.py
│   │   └── Distance calculation utilities (Haversine, Manhattan)
│   ├── data_preprocessing.py
│   │   └── Data loading and outlier removal
│   ├── feature_engineering.py
│   │   └── Feature creation based on EDA insights
│   ├── model_training.py
│   │   └── XGBoost model training and saving
│   └── model_evaluation.py
│       └── Model evaluation metrics (RMSE, MAE, R²)
│
├── streamlit_app/
│   └── app.py
│       └── Streamlit UI consuming FastAPI predictions
│
├── models/
│   └── xgboost_trip_duration.pkl
│       └── Trained model (generated after training)
│
├── Dockerfile
│   └── Docker configuration for FastAPI service
│
├── .dockerignore
│   └── Files excluded from Docker image
│
├── .gitignore
│   └── Prevents pushing data, models, and cache files
│
├── main.py
│   └── Entry point for training pipeline
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
    └── Project documentation
```
---

## 🏗️ System Architecture

User → Streamlit UI → FastAPI → XGBoost Model → Prediction Output

## 🚀 How to Run

1.  Clone the repository:
   ```bash
   git clone  https://github.com/chetanal23/nyc-taxi-trip-duration.git
   cd nyc-taxi-trip-duration
   ```
2. Create Virtual Environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```
3.  Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Place Dataset
   ```bash
   data/raw/nyc_taxi_trip_duration.csv
   ```
5. Train the Model
   ```bash
   python main.py
   ```
This generates:
* models/xgboost_trip_duration.pkl
* data/processed/processed_data.csv
 🌐 Run FastAPI Inference Server:
 ```
 uvicorn api.app:app --reload
 ```
Open Swagger UI: http://127.0.0.1:8000/docs
 🎨 Run Streamlit UI:
 ```bash
 streamlit run streamlit_app/app.py
 ```
The Streamlit app sends requests to FastAPI and displays predictions interactively.
 🐳 Run Using Docker (Optional):
 ```bash
 docker build -t nyc-taxi-api .
 docker run -p 8000:8000 nyc-taxi-api
 ```
Access: http://localhost:8000/docs

---

## 📌 Tech Stack
* **Python**
* **Pandas & NumPy:** Data Manipulation
* **Scikit-Learn:** Evaluation Metrics
* **XGBoost:** Gradient Boosting Model
* **FastAPI:** Model Serving
* **Streamlit:** Interactive Dashboard
* **Docker:** Containerization

----

## 📜 License
This project is licensed under the MIT License.

---

Built as a portfolio-grade, industry-ready project to demonstrate real-world machine learning system design and deployment.
