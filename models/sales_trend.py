import pandas as pd
import plotly.express as px
from plotly.offline import plot

# Load the sales data
sales_data = pd.read_csv('data/sales_data.csv', parse_dates=['sale_date'])

# Group by sale date and sum total sales
sales_trend = sales_data.groupby('sale_date')['total_price'].sum().reset_index()

# Create a time series plot
fig = px.line(sales_trend, x='sale_date', y='total_price', title='Sales Trend Over Time', labels={'sale_date': 'Date', 'total_price': 'Total Sales'})

# Save the chart as an HTML file in the templates folder
plot(fig, filename='templates/sales_trend_graph.html')
