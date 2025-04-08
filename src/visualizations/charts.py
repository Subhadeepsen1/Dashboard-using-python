import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import pandas as pd

def create_income_expense_charts(data):
    """
    Generate charts and summary data for the dashboard.
    """
    charts = {}

    # Set a consistent style for the charts
    sns.set_theme(style="whitegrid")

    # Income vs Expense Bar Chart
    plt.figure(figsize=(12, 6))
    melted_data = data.melt(id_vars=['Category'], value_vars=['Expense', 'Income'], 
                            var_name='Type', value_name='Value')
    sns.barplot(x='Category', y='Value', data=melted_data, hue='Type', palette='viridis')
    plt.title('Income vs Expense by Category', fontsize=16, fontweight='bold')
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Amount', fontsize=12)
    plt.legend(title='Type', fontsize=10)
    plt.xticks(rotation=45, fontsize=6)
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    charts['income_expense'] = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.clf()

    # Income Trend Line Chart
    income_data = data.groupby('Date')['Income'].sum().reset_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Income', data=income_data, marker='o', color='blue')
    plt.title('Income Trend Over Time', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Income Amount', fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    charts['income_trend'] = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.clf()

    # Expense Distribution Pie Chart
    expense_data = data.groupby('Category')['Expense'].sum().reset_index()
    plt.figure(figsize=(16, 10))
    plt.pie(expense_data['Expense'], labels=expense_data['Category'], autopct='%1.1f%%', 
            startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Expense Distribution by Category', fontsize=16, fontweight='bold')
    plt.axis('equal')
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    charts['expense_distribution'] = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.clf()

    # Top 5 Expense Categories (Table)
    top_expenses = expense_data.sort_values(by='Expense', ascending=False).head(5)
    charts['top_expenses'] = top_expenses.to_html(index=False, classes='table table-striped')

    # Summary Data
    total_income = data['Income'].sum()
    total_expense = data['Expense'].sum()
    charts['summary'] = {
        'total_income': total_income,
        'total_expense': total_expense
    }

    return charts