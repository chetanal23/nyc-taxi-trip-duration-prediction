from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

def evaluate_model(model, X_test, y_test):
   """
   Evaluate regression model performance
   """
   predictions = model.predict(X_test)

   rmse = mean_squared_error(y_test, predictions, squared=False)
   mae = mean_absolute_error(y_test, predictions)
   r2 = r2_score(y_test, predictions)

   print("Model Evaluation Metrics")
   print("-" * 30)
   print(f"RMSE : {rmse:.2f}")
   print(f"MAE  : {mae:.2f}")
   print(f"R2   : {r2:.4f}")

   return {
      "RMSE": rmse,
      "MAE": mae,
      "R2": r2
   }
