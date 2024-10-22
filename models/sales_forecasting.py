import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import plot
import plotly.express as px

# Load sales data
data = pd.read_csv('data/sales_data.csv', parse_dates=['sale_date'], index_col='sale_date')

# Remove duplicate index labels
data = data[~data.index.duplicated(keep='first')]

# Set daily frequency if dates have gaps
data = data.asfreq('D')

# Create and fit ARIMA model
model = ARIMA(data['total_price'], order=(5, 1, 0)) 
model_fit = model.fit()

# Forecast for the next 30 days
forecast = model_fit.forecast(steps=30)

# Generate future dates for the forecast (next 30 days)
forecast_index = pd.date_range(start=data.index[-1] + pd.Timedelta(days=1), periods=30, freq='D')

# Create Plotly figure
fig = make_subplots(rows=4, cols=1, subplot_titles=('Sales Forecasting', 'Total Price Distribution', 'Box Plot of Total Price', ''))

# Add Actual Sales and Predicted Sales plots
fig.add_trace(go.Scatter(x=data.index, y=data['total_price'], mode='lines', name='Actual Sales'), row=1, col=1)
fig.add_trace(go.Scatter(x=forecast_index, y=forecast, mode='lines', name='Predicted Sales', line=dict(color='red')), row=1, col=1)

# Add Histogram for Total Price Distribution
fig.add_trace(px.histogram(data, x='total_price').data[0], row=2, col=1)

# Add Box Plot for Total Price Distribution
fig.add_trace(px.box(data, y='total_price', title='Box Plot of Total Price').data[0], row=3, col=1)

# Update layout
fig.update_layout(height=1800, title_text="Sales Forecasting Analysis", xaxis_title='Date', yaxis_title='Total Price')

# Save the combined plot as an HTML file in the templates/ folder
plot(fig, filename='templates/sales_forecasting_graph.html')
