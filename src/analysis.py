from src.utils import load_csv, calculate_statistics

def run_analysis():
    # Load data using the utility function
    data = load_csv('data/sample.csv')
    if data is None:
        return {"error": "Failed to load data"}

    # Perform statistical analysis
    stats = calculate_statistics(data, 'value')
    if stats is None:
        return {"error": "Failed to calculate statistics"}

    return stats
