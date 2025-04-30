import pandas as pd
import random
from faker import Faker
from datetime import datetime
import os

# Initialize Faker
fake = Faker()

# Settings
num_transactions = 500  # You can change this as needed

# Possible transaction types and statuses
transaction_types = ['SendMoney', 'PayBill', 'BuyGoods', 'WithdrawCash', 'Deposit', 'AirtimeTopup']
transaction_statuses = ['Success', 'Failed']
locations = ['Nairobi', 'Mombasa', 'Kisumu', 'Eldoret', 'Nakuru', 'Thika', 'Meru', 'Kitale', 'Machakos', 'Nyeri']

# Generate fake transaction records
data = []
for i in range(1, num_transactions + 1):
    transaction = {
        'Transaction_ID': f'TX{i:04d}',
        'Timestamp': fake.date_time_between(start_date='-30d', end_date='now').strftime('%Y-%m-%d %H:%M:%S'),
        'Sender_ID': f'2547{random.randint(10000000, 99999999)}',
        'Receiver_ID': f'2547{random.randint(10000000, 99999999)}',
        'Amount': round(random.uniform(10, 70000), 2),
        'Transaction_Type': random.choice(transaction_types),
        'Status': random.choice(transaction_statuses),
        'Location': random.choice(locations)
    }
    data.append(transaction)

# Create a DataFrame
df = pd.DataFrame(data)

# Define path to save CSV
current_dir = os.path.dirname(os.path.abspath(__file__))  # path to src/
dataset_dir = os.path.join(current_dir, '..', 'datasets')
os.makedirs(dataset_dir, exist_ok=True)  # create ../dataset if it doesn't exist

csv_path = os.path.join(dataset_dir, 'mpesa_transactions.csv')

# Save to CSV
df.to_csv(csv_path, index=False)

print(f"✅ Dataset created successfully!")
