# fraud_detection_model.py
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load the large transaction dataset
df = pd.read_csv('large_financial_transactions.csv')

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

# Check if 'amount' column exists
if 'amount' not in df.columns:
    raise ValueError("Expected column 'amount' not found in dataset.")

# Drop rows with missing values in 'amount'
df.dropna(subset=['amount'], inplace=True)

# Initialize and train the Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
df['fraud_flag'] = model.fit_predict(df[['amount']])

# Save the results
df.to_csv('flagged_frauds.csv', index=False)
print(f"✅ Fraud detection complete. {len(df)} transactions processed.")
print("📁 Results saved to 'flagged_frauds.csv'.")

# Save the trained model
joblib.dump(model, 'isolation_forest_model.pkl')
print("🧠 Model saved to 'isolation_forest_model.pkl'.")
