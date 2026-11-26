# 🚗 Used Car Price Prediction & Market Analysis

## 📌 Project Overview
This project delivers an end-to-end Machine Learning and Business Intelligence solution to predict used car asking prices and analyze market dynamics. It integrates data preprocessing, predictive modeling, and an interactive Power BI dashboard.

---

## 📊 Dashboard Preview & Key Insights

![Dashboard Screenshot](./dashboard/Used_Car_Price_Analysis.png)

### Core Findings
* 🏎️ **Actual vs. Predicted:** Predictions are close to actual average prices for brands such as BMW, Volvo and Jaguar, with larger gaps for some luxury brands (e.g., Lamborghini, Maserati). The chart includes training data, so use the test-set metrics below to judge accuracy.
* ⛽ **Fuel Type:** Diesel vehicles have the highest average asking price (about ₹14.2 Lakhs).
* 📅 **Manufacturing Year:** The average asking price rises with newer models, from about ₹7.6 Lakhs (2015) to about ₹22 Lakhs (2023).

---

## 🛠️ Tech Stack & Structure
* 🐍 **Python:** Data cleaning and model training (`scripts/clean_and_train.py`)
* 📊 **Power BI:** Interactive dashboard (`dashboard/Used_Car_Price_Analysis.pbix`)
* 📁 **Data:** Raw and engineered datasets stored in `data/`

```text
Used-Car-Price-Prediction-Market-Analysis/
├── dashboard/
│   ├── Used_Car_Price_Analysis.pbix   # Interactive Power BI Report
│   ├── Used_Car_Price_Analysis.pdf    # Static PDF Export
│   └── Used_Car_Price_Analysis.png    # Dashboard Image
├── data/
│   ├── Used_Car_Dataset.csv           # Raw Dataset
│   └── processed_car_data.csv         # Cleaned Dataset with Predictions
├── scripts/
│   └── clean_and_train.py             # Python Cleaning & ML Pipeline
└── README.md                          # Project Documentation
```

---

## 🤖 Machine Learning Model & Pipeline

### 🛠️ Pipeline Details
* 🧼 **Data Cleaning:** Removed currency symbols (`₹`), distance units (`km`), and commas from target and feature columns (`AskPrice_clean`, `kmDriven_clean`).
* 🩹 **Imputation:** Handled missing values using median strategy for numerical features (`Engine_Capacity_CC`) and mode for discrete categories (`Seating_Capacity`).
* ⚙️ **Categorical Encoding:** Applied One-Hot Encoding to categorical variables (`Transmission`, `FuelType`, `Owner`).
* 🌲 **Algorithm Selection:** Trained a **Random Forest Regressor** (`n_estimators=100`, `random_state=42`) using an 80/20 train-test split.

### 📈 Performance Metrics
* 🎯 **$R²$ Score:** `0.62` — The Random Forest model explains 62% of the variance in used car asking prices.
* 📉 **Mean Absolute Error (MAE):** `₹320,210.66` — On average, model predictions deviate from actual asking prices by approximately ₹3.20 Lakhs.

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MSanjeevkrishna/Used-Car-Price-Prediction-Market-Analysis.git
   cd Used-Car-Price-Prediction-Market-Analysis
   ```

2. **Install the libraries:**
   ```bash
   pip install pandas numpy scikit-learn
   ```

3. **Run the data and training pipeline:**
   ```bash
   cd scripts
   python clean_and_train.py
   ```

4. **Explore the dashboard:**
   * Open `dashboard/Used_Car_Price_Analysis.pbix` in **Power BI Desktop**.
