# generate_ai_fraud_reasons.py

import pandas as pd

# Load your existing flagged frauds CSV
df = pd.read_csv('flagged_frauds.csv')

# Filter only fraud transactions
frauds = df[df['fraud_flag'] == -1].copy()

# Simulated AI explanation generator
def generate_reason(row):
    reasons = []
    if row['amount'] > 5000:
        reasons.append("⚠️ High transaction amount")
    if row['location'] in ['Delhi', 'Mumbai']:
        reasons.append("📍 High-risk location")
    if row['device_type'] in ['Mobile', 'Tablet']:
        reasons.append("📱 Less secure device type")
    if row['merchant_category'] in ['Travel', 'Luxury', 'Electronics']:
        reasons.append("🛒 Sensitive merchant category")
    if '23:' in str(row['time']) or '00:' in str(row['time']):
        reasons.append("🌙 Unusual transaction time")

    if not reasons:
        reasons.append("🔍 Anomaly detected by Isolation Forest")
    return "; ".join(reasons)

# Apply the explanation
frauds['ai_fraud_reason'] = frauds.apply(generate_reason, axis=1)

# Save to a new CSV
frauds.to_csv('ai_flagged_frauds.csv', index=False)
print("✅ ai_flagged_frauds.csv has been generated with AI fraud reasons.")
