# ============================================================
# MINI PROJECT: LOGISTICS DELIVERY PERFORMANCE ANALYSIS
# ============================================================

import pandas as pd

# ------------------------------------------------------------
# CREATE DATASET
# ------------------------------------------------------------

data = {
    "Shipment_ID": [201, 202, 203, 204, 205, 206, 207, 208],
    "Origin": ["Chennai", "Delhi", "Mumbai", "Chennai", "Delhi", "Mumbai", "Chennai", "Delhi"],
    "Destination": ["Bangalore", "Jaipur", "Pune", "Hyderabad", "Lucknow", "Nagpur", "Coimbatore", "Agra"],
    "Distance_km": [350, 280, 150, 500, 420, 300, 200, 250],
    "Dispatch_Date": pd.to_datetime([
        "2024-01-01", "2024-01-03", "2024-01-05", "2024-01-07",
        "2024-01-09", "2024-01-11", "2024-01-13", "2024-01-15"
    ]),
    "Delivery_Date": pd.to_datetime([
        "2024-01-03", "2024-01-05", "2024-01-06", "2024-01-10",
        "2024-01-13", "2024-01-13", "2024-01-15", "2024-01-18"
    ]),
    "Transport_Mode": ["Truck", "Air", "Truck", "Ship", "Air", "Truck", "Truck", "Ship"],
    "Cost": [15000, 25000, 8000, 20000, 27000, 12000, 9000, 18000]
}

df = pd.DataFrame(data)

print("=" * 70)
print("LOGISTICS DELIVERY PERFORMANCE ANALYSIS")
print("=" * 70)

print("\nDataset")
print(df)

# ------------------------------------------------------------
# CALCULATE DELIVERY TIME
# ------------------------------------------------------------

df["Delivery_Time_Days"] = (
    df["Delivery_Date"] - df["Dispatch_Date"]
).dt.days

print("\nDataset with Delivery Time")
print(df)

# ------------------------------------------------------------
# IDENTIFY LATE DELIVERIES
# ------------------------------------------------------------

df["Late_Delivery"] = df["Delivery_Time_Days"] > 3

print("\nDataset with Late Delivery Status")
print(df)

# ------------------------------------------------------------
# BASIC EXPLORATION
# ------------------------------------------------------------

print("\nDataset Information")
df.info()

print("\nStatistical Summary")
print(df.describe())

# ------------------------------------------------------------
# DELIVERY TIME ANALYSIS
# ------------------------------------------------------------

print("\nAverage Delivery Time (Days)")
print(df["Delivery_Time_Days"].mean())

# ------------------------------------------------------------
# PERFORMANCE BY TRANSPORT MODE
# ------------------------------------------------------------

print("\nAverage Delivery Time by Transport Mode")
print(df.groupby("Transport_Mode")["Delivery_Time_Days"].mean())

# ------------------------------------------------------------
# COST ANALYSIS
# ------------------------------------------------------------

print("\nAverage Transportation Cost by Transport Mode")
print(df.groupby("Transport_Mode")["Cost"].mean())

# ------------------------------------------------------------
# LATE DELIVERY PERCENTAGE
# ------------------------------------------------------------

late_percentage = df["Late_Delivery"].mean() * 100

print("\nLate Delivery Percentage")
print(f"{late_percentage:.2f}%")

# ------------------------------------------------------------
# REGION WITH MOST SHIPMENTS
# ------------------------------------------------------------

print("\nNumber of Shipments by Origin")
print(df["Origin"].value_counts())

print("\nOrigin with Highest Number of Shipments")
print(df["Origin"].value_counts().idxmax())