from utils import load_data

def run_analysis():
    # Load the CSV file using utility function
    data = load_data('data/sample.csv')
    
    if data is None:
        return {'error': 'File not found'}
    
    try:
        # Perform analysis (e.g., calculate mean)
        mean_value = data['value'].mean()
        return {'mean': mean_value}
    except KeyError:
        # Handle missing column
        return {'error': 'Column "value" not found in the dataset'}
