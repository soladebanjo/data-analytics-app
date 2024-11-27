import pandas as pd

def load_data(file_path):
    try:
        # Load CSV file
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

