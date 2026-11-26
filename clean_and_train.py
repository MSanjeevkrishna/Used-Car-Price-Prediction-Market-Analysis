import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# 1. LOAD DATASET
raw_data_path = os.path.join('..', 'data', 'Used_Car_Dataset.csv')
df = pd.read_csv(raw_data_path)

# 2. CLEAN TEXT COLUMNS INTO NUMBERS
# Clean AskPrice (remove '₹', ',', and extra spaces)
df['AskPrice_clean'] = (
    df['AskPrice']
    .astype(str)
    .str.replace('₹', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.strip()
)
df['AskPrice_clean'] = pd.to_numeric(df['AskPrice_clean'], errors='coerce')

# Clean kmDriven (remove 'km', ',', and extra spaces)
df['kmDriven_clean'] = (
    df['kmDriven']
    .astype(str)
    .str.replace('km', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.strip()
)
df['kmDriven_clean'] = pd.to_numeric(df['kmDriven_clean'], errors='coerce')

# Remove rows where price or km is missing
df_clean = df.dropna(subset=['AskPrice_clean', 'kmDriven_clean']).copy()

# 3. SELECT FEATURES & PREPARE DATA
features = ['Year', 'Age', 'Engine_Capacity_CC', 'Seating_Capacity', 'kmDriven_clean', 'Transmission', 'FuelType', 'Owner']
X = df_clean[features].copy()
y = df_clean['AskPrice_clean']

# Fill missing numerical values
X['Engine_Capacity_CC'] = X['Engine_Capacity_CC'].fillna(X['Engine_Capacity_CC'].median())
X['Seating_Capacity'] = X['Seating_Capacity'].fillna(X['Seating_Capacity'].mode()[0])
X['Age'] = X['Age'].fillna(2026 - X['Year'])

# Convert text categories to 0s and 1s (One-Hot Encoding)
X_encoded = pd.get_dummies(X, columns=['Transmission', 'FuelType', 'Owner'], drop_first=True)

# 4. TRAIN / TEST SPLIT & MODEL TRAINING
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model performance
y_pred = model.predict(X_test)
print("Model Evaluation Metrics:")
print(f"R² Score: {r2_score(y_test, y_pred):.2f}")
print(f"Mean Absolute Error: ₹{mean_absolute_error(y_test, y_pred):,.2f}")

# 5. GENERATE PREDICTIONS & EXPORT FOR POWER BI
df_clean['Predicted_AskPrice'] = model.predict(X_encoded)

# Save processed dataset into data folder
output_path = os.path.join('..', 'data', 'processed_car_data.csv')
df_clean.to_csv(output_path, index=False)
print(f"Success! Processed data saved to {output_path}")