import pandas as pd
import requests

# Function to Fetch Data from API
def fetch_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching data: {e}")
        return None

# API Endpoint (Replace with actual URL)
HISTORICAL_DATA_URL = "https://api.jsonserve.com/Uw5CrX"

# Fetch Historical Data
historical_data = fetch_data(HISTORICAL_DATA_URL)

if not historical_data:
    print("❌ No data received. Exiting...")
    exit()

print("✅ Data fetched successfully!")

# Convert JSON to DataFrame
try:
    if isinstance(historical_data, list):
        historical_df = pd.DataFrame.from_records(historical_data)
    else:
        historical_df = pd.json_normalize(historical_data)
except Exception as e:
    print(f"❌ Error processing data: {e}")
    exit()

# Print column names for debugging
print("📌 Available Columns in Data:")
print(historical_df.columns)

# Check 'questions' column structure
if "questions" in historical_df.columns:
    print("\n📊 Sample 'questions' Data:")
    print(historical_df["questions"].head())  # Print sample data

# Extract Scores if available
def extract_scores(row):
    """Extract scores from nested 'questions' column."""
    if isinstance(row, list) and len(row) > 0:
        total_score = 0
        for q in row:
            if "score" in q:  # Check if 'score' exists
                total_score += q["score"]
            elif "correct" in q and q["correct"]:  # Assign score for correct answers
                total_score += 4  # Assuming 4 marks per correct answer
        return total_score
    return 0

# Apply function to extract scores
historical_df["calculated_score"] = historical_df["questions"].apply(extract_scores)

# Handle Missing Data
historical_df.fillna(historical_df.mean(numeric_only=True), inplace=True)

# Rank Prediction Logic
def predict_rank(data):
    """Predict NEET Rank based on calculated scores."""
    avg_score = data["calculated_score"].mean()
    if avg_score > 650:
        return "Top 500"
    elif avg_score > 500:
        return "Top 5000"
    else:
        return "Above 5000"

# Predict Rank for User
predicted_rank = predict_rank(historical_df)
print(f"🎯 Predicted NEET Rank: {predicted_rank}")

print("✅ Processing complete!")
