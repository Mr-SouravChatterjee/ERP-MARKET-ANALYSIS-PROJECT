from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.offline import plot

# Load cleaned dataset
data = pd.read_csv('data/cleaned_data.csv')

# Select relevant features
X = data[['quantity_sold', 'total_price']]

# Normalize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(X)

# Apply K-Means clustering with 4 clusters
kmeans = KMeans(n_clusters=4)
data['customer_segment'] = kmeans.fit_predict(scaled_features)

# Matplotlib Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['quantity_sold'], y=data['total_price'], hue=data['customer_segment'], palette='viridis')
plt.title('Customer Segments')
plt.show()

# Plotly scatter plot for interactive segments visualization
fig = px.scatter(data, x='quantity_sold', y='total_price', color='customer_segment', title='Customer Segmentation')

# Additional Visualizations
# 1. Bar chart for the number of customers in each segment
segment_counts = data['customer_segment'].value_counts().reset_index()
segment_counts.columns = ['customer_segment', 'count']

fig_bar = px.bar(segment_counts, x='customer_segment', y='count', title='Number of Customers in Each Segment', labels={'count': 'Number of Customers', 'customer_segment': 'Segment'})

# 2. Box plot for the distribution of total price in each segment
fig_box = px.box(data, x='customer_segment', y='total_price', title='Distribution of Total Price in Each Segment', labels={'total_price': 'Total Price', 'customer_segment': 'Segment'})

# 3. Heatmap to show correlations
correlation = data[['quantity_sold', 'total_price', 'customer_segment']].corr()
fig_heatmap = px.imshow(correlation, text_auto=True, title='Correlation Heatmap')

# Combine all plots into a single HTML file
combined_fig = make_subplots(rows=4, cols=1, subplot_titles=('Customer Segmentation', 'Number of Customers in Each Segment', 'Distribution of Total Price in Each Segment', 'Correlation Heatmap'))

combined_fig.add_trace(fig.data[0], row=1, col=1)
combined_fig.add_trace(fig_bar.data[0], row=2, col=1)
combined_fig.add_trace(fig_box.data[0], row=3, col=1)
combined_fig.add_trace(fig_heatmap.data[0], row=4, col=1)

combined_fig.update_layout(height=1600, title_text="Customer Segmentation Analysis")

# Save the combined Plotly graph as an HTML file
plot(combined_fig, filename='templates/customer_segmentation_graph.html')

# Save the result
data.to_csv('data/customer_segments.csv', index=False)
