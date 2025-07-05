# openai_fraud_analysis.py
import pandas as pd
import random

# Load the flagged fraud dataset
df = pd.read_csv('flagged_frauds.csv')

# Filter suspected frauds
suspicious = df[df['fraud_flag'] == -1]

# Define a simulated explanation generator
def simulate_fraud_analysis(transaction):
    amt = transaction['amount']
    location = transaction.get('location', 'Unknown')
    merchant = transaction.get('merchant_category', 'Unknown')

    reasons = []

    if amt > 5000:
        reasons.append("Unusually high transaction amount.")
    if merchant in ['Luxury Goods', 'Electronics', 'Travel']:
        reasons.append(f"High-risk merchant category: {merchant}.")
    if location in ['Kolkata', 'Delhi', 'Unknown']:
        reasons.append(f"Suspicious location: {location}.")

    if not reasons:
        reasons.append("Unusual pattern detected by model.")

    return " ".join(reasons)

# Apply simulated GPT analysis
suspicious['ai_analysis'] = suspicious.apply(simulate_fraud_analysis, axis=1)

# Save results
suspicious.to_csv('ai_flagged_frauds.csv', index=False)
print("✅ AI analysis complete. Saved as 'ai_flagged_frauds.csv'.")
