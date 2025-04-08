from flask import Flask, render_template
from utils.data_processing import load_data
from visualizations.charts import create_income_expense_charts

app = Flask(__name__)

@app.route('/')
def index():
    # Load the dataset
    data = load_data('data/Income_expense_data.csv')
    
    # Generate charts
    charts = create_income_expense_charts(data)
    
    # Render the HTML template with the charts
    return render_template('index.html', charts=charts)

if __name__ == '__main__':
    app.run(debug=True)