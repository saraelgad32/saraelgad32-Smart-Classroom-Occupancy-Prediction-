import time
from functools import wraps
import logging
import csv
import os

logging.basicConfig(level=logging.INFO)

def log_step(func):
    """Decorator to log the progress of our ML pipeline."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"--- Starting: {func.__name__} ---")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        logging.info(f"--- Finished: {func.__name__} in {end - start:.4f}s ---")
        return result
    return wrapper
def log_prediction(func):
    """
    Advanced Decorator used in the API.
    Logs API inputs and outputs to a CSV for MLOps auditing.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Get the input data (usually the 'data' keyword argument in FastAPI)
        sensor_data = kwargs.get('data') or (args[0] if args else None)
        
        # 2. Run the actual prediction
        result = func(*args, **kwargs)
        
        # 3. Log to CSV file in the data folder
        log_file = "data/prediction_audit.csv"
        file_exists = os.path.isfile(log_file)
        
        try:
            with open(log_file, mode='a', newline='') as f:
                writer = csv.writer(f)
                # Add headers if the file is new
                if not file_exists:
                    writer.writerow(['timestamp', 'temp', 'humidity', 'light', 'co2', 'prediction'])
                
                if sensor_data:
                    writer.writerow([
                        time.strftime("%Y-%m-%d %H:%M:%S"),
                        sensor_data.Temperature,
                        sensor_data.Humidity,
                        sensor_data.Light,
                        sensor_data.CO2,
                        result['occupancy_prediction']
                    ])
        except Exception as e:
            logging.error(f"Failed to log to CSV: {e}")
            
        return result
    return wrapper