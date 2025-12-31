from src.utils import haversine_distance, manhattan_distance

def create_features(df):
    df['pickup_hour'] = df['pickup_datetime'].dt.hour
    df['pickup_weekday'] = df['pickup_datetime'].dt.weekday
    df['pickup_month'] = df['pickup_datetime'].dt.month

    df['is_weekend'] = df['pickup_weekday'].isin([5, 6]).astype(int)
    df['is_rush_hour'] = df['pickup_hour'].isin([7,8,9,16,17,18,19]).astype(int)

    df['haversine_km'] = haversine_distance(
        df['pickup_latitude'], df['pickup_longitude'],
        df['dropoff_latitude'], df['dropoff_longitude']
    )

    df['manhattan_dist'] = manhattan_distance(
        df['pickup_latitude'], df['pickup_longitude'],
        df['dropoff_latitude'], df['dropoff_longitude']
    )

    features = [
        'pickup_hour', 'pickup_weekday', 'pickup_month',
        'is_weekend', 'is_rush_hour',
        'passenger_count', 'haversine_km', 'manhattan_dist'
    ]

    return df[features], df['trip_duration']
