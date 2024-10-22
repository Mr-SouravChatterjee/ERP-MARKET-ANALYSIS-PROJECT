import pandas as pd
import plotly.express as px
from plotly.offline import plot

# Load the sales data
sales_data = pd.read_csv('data/sales_data.csv')

# Group by product and sum the quantity sold
top_products = sales_data.groupby('product_id')['quantity_sold'].sum().nlargest(5).reset_index()

# Create a bar chart for top 5 products by quantity sold
fig = px.bar(top_products, x='product_id', y='quantity_sold', title='Top 5 Best-Selling Products', labels={'product_id': 'Product ID', 'quantity_sold': 'Quantity Sold'})

# Save the chart as an HTML file in the templates folder
plot(fig, filename='templates/top_selling_products_graph.html')
