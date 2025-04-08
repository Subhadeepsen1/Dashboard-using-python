import pandas as pd

def load_data(filepath):
    """
    Load and preprocess the dataset.
    """
    try:
        # Load the dataset
        data = pd.read_csv(filepath)
        
        # Rename columns for easier use
        data = data.rename(columns={
            'REF_DATE': 'Date',
            'Household expenditures, summary-level categories': 'Category',
            'Expense': 'Expense',
            'Income': 'Income'
        })
        
        # Filter relevant columns
        data = data[['Date', 'Category', 'Expense', 'Income']]
        
        # Convert Date to datetime format
        data['Date'] = pd.to_datetime(data['Date'], format='%Y')
        
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()