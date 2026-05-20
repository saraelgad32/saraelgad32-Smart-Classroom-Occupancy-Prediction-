import pandas as pd
from src.utils import log_step

@log_step
def load_data(path: str) -> pd.DataFrame:
    # In a real scenario, this would point to your CSV or SQL DB
    return pd.read_csv(path)

@log_step
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Pure function: removes nulls and selects features."""
    # Features usually include: Temperature, Humidity, Light, CO2
    relevant_columns = ['Temperature', 'Humidity', 'Light', 'CO2', 'Occupancy']
    return df[relevant_columns].dropna()

@log_step
def split_features_target(df: pd.DataFrame):
    X = df.drop('Occupancy', axis=1)
    y = df['Occupancy']
    return X, y