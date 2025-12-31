import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])

    # Remove outliers based on EDA
    df = df[(df['trip_duration'] > 60) & (df['trip_duration'] < 20000)]
    df = df[df['passenger_count'] > 0]

    # NYC geographical bounds
    df = df[
        (df['pickup_latitude'].between(40.5, 41.0)) &
        (df['pickup_longitude'].between(-74.3, -73.6)) &
        (df['dropoff_latitude'].between(40.5, 41.0)) &
        (df['dropoff_longitude'].between(-74.3, -73.6))
    ]

    return df
