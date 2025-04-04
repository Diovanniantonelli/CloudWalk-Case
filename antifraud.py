import pandas as pd

# Load dataset from Excel
df = pd.read_excel('C:/Users/Usuario/Desktop/Anti-Fraude System/Database/Transactions.xlsx')

# Convert the transaction_date column to datetime
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Sort data by user and transaction date
df = df.sort_values(by=['user_id', 'transaction_date'])

# Calculate time difference between current and previous transaction of each user
df['prev_time'] = df.groupby('user_id')['transaction_date'].shift()
df['time_diff_sec'] = (df['transaction_date'] - df['prev_time']).dt.total_seconds()

# Define antifraud logic
known_fraud_users = {10378, 16781}
high_value_threshold = 3000

def antifraud_rule(row):
    if row['user_id'] in known_fraud_users:
        return 'Previous chargeback'
    elif row['transaction_amount'] > high_value_threshold:
        return 'High transaction value'
    elif pd.notnull(row['time_diff_sec']) and row['time_diff_sec'] < 60:
        return 'High velocity'
    else:
        return 'Approved'

# Apply antifraud logic
df['antifraud_decision'] = df.apply(antifraud_rule, axis=1)

# ✅ Convert boolean values to string format "True"/"False"
df['has_cbk'] = df['has_cbk'].apply(lambda x: 'True' if x is True else 'False')

# Export to a new Excel file
output_path = 'C:/Users/Usuario/Desktop/Anti-Fraude System/Database/Transactions_with_flags.xlsx'
df.to_excel(output_path, index=False)

print("✅ File saved successfully at:", output_path)
