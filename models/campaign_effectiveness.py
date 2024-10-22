import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.offline import plot

# Generating 30 campaign IDs
campaign_ids = np.arange(1, 31)

# Generating random data for clicks, conversions, and spend
np.random.seed(42)  # Ensuring reproducibility
clicks = np.random.randint(500, 5000, size=30)
conversions = np.random.randint(20, 500, size=30)
spend = np.random.randint(1000, 10000, size=30)

# Creating the DataFrame
campaign_data = pd.DataFrame({
    'campaign_id': campaign_ids,
    'clicks': clicks,
    'conversions': conversions,
    'spend': spend
})

# Calculating conversion rates and ROI
campaign_data['conversion_rate'] = campaign_data['conversions'] / campaign_data['clicks']
campaign_data['roi'] = (campaign_data['conversions'] * 100) / campaign_data['spend']

# Create subplots
fig = make_subplots(rows=4, cols=1, subplot_titles=('Campaign Conversion Rates', 'Campaign ROI', 'Clicks vs Conversions', 'Distribution of Clicks, Conversions, and Spend'))

# Add first plot (bar for conversion rates)
fig.add_trace(
    px.bar(campaign_data, x='campaign_id', y='conversion_rate').data[0],
    row=1, col=1
)

# Add second plot (line for ROI)
fig.add_trace(
    px.line(campaign_data, x='campaign_id', y='roi').data[0],
    row=2, col=1
)

# Add third plot (scatter for clicks vs conversions)
fig.add_trace(
    px.scatter(campaign_data, x='clicks', y='conversions', title='Clicks vs Conversions', labels={'clicks': 'Clicks', 'conversions': 'Conversions'}).data[0],
    row=3, col=1
)

# Add fourth plot (histogram for clicks, conversions, and spend)
fig.add_trace(
    px.histogram(campaign_data, x='clicks', title='Distribution of Clicks').data[0],
    row=4, col=1
)
fig.add_trace(
    px.histogram(campaign_data, x='conversions', title='Distribution of Conversions').data[0],
    row=4, col=1
)
fig.add_trace(
    px.histogram(campaign_data, x='spend', title='Distribution of Spend').data[0],
    row=4, col=1
)

# Update layout
fig.update_layout(height=1800, title_text="Campaign Effectiveness")

# Save the combined plot as an HTML file in the templates/ folder
plot(fig, filename='templates/campaign_effectiveness_graph.html')
