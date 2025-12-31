import joblib
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, r2_score

def train_model(X, y):
   X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=42
   )

   model = XGBRegressor(
      n_estimators=300,
      max_depth=8,
      learning_rate=0.05,
      subsample=0.8,
      colsample_bytree=0.8,
      objective='reg:squarederror',
      n_jobs=-1
   )

   model.fit(X_train, y_train)

   preds = model.predict(X_test)

   rmse = rmse = root_mean_squared_error(y_test, preds)
   r2 = r2_score(y_test, preds)

   print(f"RMSE: {rmse:.2f}")
   print(f"R2 Score: {r2:.4f}")

   joblib.dump(model, "models/xgboost_trip_duration.pkl")

   return model