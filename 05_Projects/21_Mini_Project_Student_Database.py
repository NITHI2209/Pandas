# ============================================================
# MINI PROJECT: EMPLOYEE ATTRITION RATE ANALYSIS USING PANDAS
# ============================================================

import pandas as pd
import numpy as np

# ------------------------------------------------------------
# CREATE DATASET
# ------------------------------------------------------------

data = {
    "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Age": [25, 30, 28, 35, np.nan, 40, 29, 32],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance", "IT", "HR"],
    "Salary": [30000, 50000, 45000, 60000, 32000, np.nan, 52000, 35000],
    "Attrition": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No"]
}

df = pd.DataFrame(data)

print("=" * 60)
print("EMPLOYEE ATTRITION DATASET")
print("=" * 60)
print(df)

# ------------------------------------------------------------
# BASIC DATA EXPLORATION
# ------------------------------------------------------------

print("\nFirst 5 Records")
print(df.head())

print("\nLast 5 Records")
print(df.tail())

print("\nDataset Information")
df.info()

print("\nShape of Dataset")
print(df.shape)

print("\nStatistical Summary")
print(df.describe())

# ------------------------------------------------------------
# HANDLING MISSING VALUES
# ------------------------------------------------------------

# Fill missing Age with mean
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill missing Salary with median
df["Salary"].fillna(df["Salary"].median(), inplace=True)

print("\nDataset After Handling Missing Values")
print(df)

# ------------------------------------------------------------
# CHECK DUPLICATES
# ------------------------------------------------------------

duplicates = df[df.duplicated()]

print("\nDuplicate Records")
print(duplicates)

# ------------------------------------------------------------
# ATTRITION ANALYSIS
# ------------------------------------------------------------

print("\nTotal Employees")
print(df["EmployeeID"].count())

print("\nAttrition Count")
print(df["Attrition"].value_counts())

print("\nAttrition by Department")
print(df.groupby("Department")["Attrition"].value_counts())

# ------------------------------------------------------------
# SALARY ANALYSIS
# ------------------------------------------------------------

print("\nAverage Salary")
print(df["Salary"].mean())

print("\nAverage Salary by Department")
print(df.groupby("Department")["Salary"].mean())

# ------------------------------------------------------------
# AGE ANALYSIS
# ------------------------------------------------------------

print("\nAverage Age")
print(df["Age"].mean())

print("\nAverage Age by Attrition")
print(df.groupby("Attrition")["Age"].mean())

# ------------------------------------------------------------
# ATTRITION RATE
# ------------------------------------------------------------

attrition_rate = (df["Attrition"] == "Yes").mean() * 100

print("\nOverall Attrition Rate")
print(f"{attrition_rate:.2f}%")