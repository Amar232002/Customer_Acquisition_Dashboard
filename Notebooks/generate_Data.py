import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

print("Starting data generation...")

# Set random seed
np.random.seed(42)
random.seed(42)

# Number of customers
n = 10000

# Generate customer data
customer_ids = [f'CUST{str(i).zfill(5)}' for i in range(1, n+1)]
names = [f'Customer {i}' for i in range(1, n+1)]
emails = [f'customer{i}@email.com' for i in range(1, n+1)]
phones = [f'98{random.randint(10000000, 99999999)}' for _ in range(n)]
ages = np.random.randint(18, 70, n)
genders = np.random.choice(['Male', 'Female'], n)

# Generate dates
acq_dates = []
last_purchase_dates = []
for i in range(n):
    acq_date = datetime.now() - timedelta(days=random.randint(30, 730))
    last_purchase = datetime.now() - timedelta(days=random.randint(1, 180))
    acq_dates.append(acq_date.strftime('%Y-%m-%d'))
    last_purchase_dates.append(last_purchase.strftime('%Y-%m-%d'))

# Generate purchase data
purchase_counts = np.random.randint(1, 50, n)
total_spent = np.round(np.random.uniform(100, 10000, n), 2)
categories = np.random.choice(['Electronics', 'Fashion', 'Home', 'Books', 'Sports'], n)
channels = np.random.choice(['Email', 'Social Media', 'Organic', 'Referral', 'Paid Ads'], n)
cities = np.random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Pune'], n)
ratings = np.round(np.random.uniform(1, 5, n), 1)

# Create DataFrame
df = pd.DataFrame({
    'customer_id': customer_ids,
    'customer_name': names,
    'email': emails,
    'phone': phones,
    'age': ages,
    'gender': genders,
    'acquisition_date': acq_dates,
    'last_purchase_date': last_purchase_dates,
    'purchase_count': purchase_counts,
    'total_spent': total_spent,
    'product_category': categories,
    'acquisition_channel': channels,
    'city': cities,
    'customer_rating': ratings
})

# Save file
print("Saving file...")
df.to_csv('customer_data.csv', index=False)

print(f"SUCCESS! Generated {n} customer records")
print(f"File saved: customer_data.csv")
print("\nFirst 5 rows:")
print(df.head())