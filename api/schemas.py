from pydantic import BaseModel

class TripRequest(BaseModel):
   pickup_hour: int
   pickup_weekday: int
   pickup_month: int
   is_weekend: int
   is_rush_hour: int
   passenger_count: int
   haversine_km: float
   manhattan_dist: float