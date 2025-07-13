# load_model_and_predict.py

import pandas as pd
import joblib

# Load the trained Isolation Forest model
model = joblib.load('isolation_forest_model.pkl')
print("✅ Isolation Forest model loaded successfully.")

# Load transaction data
df = pd.read_csv('large_financial_transactions.csv')

# Check and clean columns
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

# Validate presence of 'amount' column
if 'amount' not in df.columns:
    raise ValueError("❌ 'amount' column not found in the dataset.")

# Predict fraud flags using the model
df['fraud_flag'] = model.predict(df[['amount']])

# Save results
df.to_csv('refreshed_flagged_frauds.csv', index=False)
print("📁 Results saved to 'refreshed_flagged_frauds.csv'.")

# Show sample results
print("\n🔍 Sample flagged transactions:")
print(df[df['fraud_flag'] == -1].head())
