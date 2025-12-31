import numpy as np

def haversine_distance(lat1, lon1, lat2, lon2):
   R = 6371  # Earth radius in km
   lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
   dlat = lat2 - lat1
   dlon = lon2 - lon1

   a = np.sin(dlat / 2) ** 2 + \
      np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2

   c = 2 * np.arcsin(np.sqrt(a))
   return R * c


def manhattan_distance(lat1, lon1, lat2, lon2):
   return abs(lat1 - lat2) + abs(lon1 - lon2)
