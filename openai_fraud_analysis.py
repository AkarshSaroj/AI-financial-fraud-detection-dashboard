import os
import pandas as pd

# ----------------------
# GPT Setup
# ----------------------
try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    GPT_ENABLED = True if os.getenv("OPENAI_API_KEY") else False
except ImportError:
    GPT_ENABLED = False

# ----------------------
# Subscription check
# ----------------------
if GPT_ENABLED:
    try:
        # Make a lightweight test request to check subscription
        client.models.list()
        print("OpenAI subscription active. GPT enabled for High Risk transactions.")
    except Exception as e:
        GPT_ENABLED = False
        print("⚠️ OpenAI key exists but subscription not active. Using mock AI only.")
else:
    print("No OpenAI key found. Using mock AI only.")

print("Script started...")


# ----------------------
# Load dataset
# ----------------------
df = pd.read_csv("large_financial_transactions.csv").head(12)
print(f"Loaded {len(df)} transactions.")

# ----------------------
# Mock AI / Rule-based risk scoring
# ----------------------
def mock_ai_analysis(row):
    amount = row["amount"]
    device = row["device_type"]
    category = row["merchant_category"]

    risk_score = 0
    reasons = []

    if amount > 5000:
        risk_score += 90
        reasons.append("Very high amount")
    if amount > 3000 and category in ["Clothing", "Travel"]:
        risk_score += 70
        reasons.append("High value in non-essential category")
    if device in ["Mobile", "Tablet"] and amount > 2000:
        risk_score += 60
        reasons.append("Large transaction via mobile/tablet")
    if risk_score == 0:
        risk_score = 20
        reasons.append("Normal transaction")

    return pd.Series({
        "risk_score": min(risk_score, 100),
        "mock_ai_analysis": "; ".join(reasons)
    })

df[["risk_score", "mock_ai_analysis"]] = df.apply(mock_ai_analysis, axis=1)

# ----------------------
# Fraud flag
# ----------------------
def assign_fraud_flag(score):
    if score >= 70:
        return "High Risk"
    elif score >= 40:
        return "Medium Risk"
    else:
        return "Low Risk"

df["fraud_flag"] = df["risk_score"].apply(assign_fraud_flag)

# ----------------------
# GPT insights (High Risk only)
# ----------------------
import time

def gpt_fraud_analysis(row, max_retries=5, delay=2):
    """
    GPT analysis with automatic retry on rate limits (429 errors).
    row: transaction row
    max_retries: number of retry attempts
    delay: seconds to wait between retries
    """
    if not GPT_ENABLED or row["fraud_flag"] != "High Risk":
        return row["mock_ai_analysis"]

    prompt = f"""
    You are a financial fraud detection assistant.
    Transaction details:
    Transaction ID: {row['transaction_id']}
    Amount: {row['amount']}
    Location: {row['location']}
    Device Type: {row['device_type']}
    Merchant Category: {row['merchant_category']}
    Risk Score: {row['risk_score']}
    Mock AI Analysis: {row['mock_ai_analysis']}
    Provide a concise 1-2 sentence explanation if this transaction might be risky.
    """

    attempt = 0
    while attempt < max_retries:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=60
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            if "429" in str(e):
                print(f"Rate limit hit. Waiting {delay}s before retry ({attempt+1}/{max_retries})...")
                time.sleep(delay)
                attempt += 1
            else:
                return f"GPT Error: {e}"
    return "GPT Error: Max retries reached due to rate limits"

# Apply GPT insights efficiently
print("Applying GPT insights to High Risk transactions in batches...")

# Initialize ai_analysis column with mock AI first
df["ai_analysis"] = df["mock_ai_analysis"]

# if GPT_ENABLED:
#     high_risk = df[df['fraud_flag'] == 'High Risk']
#     chunk_size = 50  # number of transactions per batch

#     for i in range(0, len(high_risk), chunk_size):
#         chunk = high_risk.iloc[i:i+chunk_size]
#         print(f"Processing High Risk transactions {i+1} to {i+len(chunk)}...")
#         for idx, row in chunk.iterrows():
#             df.at[idx, "ai_analysis"] = gpt_fraud_analysis(row)

print("GPT batch processing completed.")
print("GPT batch processing skipped. Using mock AI only.")


# ----------------------
# Save output
# ----------------------
output_file = "fraud_analysis_output_with_gpt.csv"
df.to_csv(output_file, index=False)

print(f"--- Fraud Analysis Completed ---")
print(df.head(12))
print(f"\nResults saved to {output_file}")
