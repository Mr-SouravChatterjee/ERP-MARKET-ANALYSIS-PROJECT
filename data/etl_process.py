from sqlalchemy import create_engine
import pandas as pd

# MySQL connection 
db_url = 'mysql://root:sour123@127.0.0.1:3306/erp_system'  
engine = create_engine(db_url)

# Load data from the ERP system (tables: sales, customers, inventory)
sales_data = pd.read_sql('SELECT * FROM sales', engine)
customer_data = pd.read_sql('SELECT * FROM customers', engine)
inventory_data = pd.read_sql('SELECT * FROM inventory', engine)

# Save to CSV
sales_data.to_csv('data/sales_data.csv', index=False)

# Merge the data into one consolidated dataset
merged_data = pd.merge(sales_data, customer_data, on='customer_id')
merged_data = pd.merge(merged_data, inventory_data, on='product_id')

# Save the final dataset as a CSV file
merged_data.to_csv('data/consolidated_data.csv', index=False)

# Check output
print(merged_data.head())

# Remove duplicate values
merged_data = merged_data.drop_duplicates()

# Drop rows with missing values 
merged_data = merged_data.dropna()

# Convert categorical variables (e.g., gender) to numeric values
merged_data['gender'] = merged_data['gender'].map({'Male': 1, 'Female': 0})

# Save the cleaned data
merged_data.to_csv('data/cleaned_data.csv', index=False)
