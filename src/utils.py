import pandas as pd

def load_csv(filepath):
    """
    Load a CSV file into a pandas DataFrame.
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

def calculate_statistics(data, column_name):
    """
    Calculate basic statistics for a given column in a DataFrame.
    """
    if column_name not in data.columns:
        print(f"Column '{column_name}' not found in data.")
        return None

    stats = {
        "mean": data[column_name].mean(),
        "median": data[column_name].median(),
        "std_dev": data[column_name].std(),
    }
    return stats
