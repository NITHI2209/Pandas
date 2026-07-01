# ============================================
# PROJECT 25 : BANK LOAN ANALYSIS SYSTEM
# ============================================

import pandas as pd
import numpy as np 

# -------------------------------------------
# CREATE DATASET 
# -------------------------------------------

data = {
    "Customer_ID" : [
        101,102,103,104,105,106,107,
        108,109,110,111,112,113,114,115],

    "Name" : [
        "Arun","Priya","Rahul","Sneha","Kiran",
        "Anjali","Vijay","Meena","Rohit","Divya",
        "Suresh","Neha","Ajay","Pooja","Karthick"
    ],

    "Age" : [
        25,32,45,28,40,
        35,50,29,38,31,
        np.nan,27,41,36,30
    ],

    "city" : [
        "Chennai","Bangalore","Mumbai","Delhi","Hyderabad",
        "Chennai","Mumbai","Bangalore","Delhi","Hyderabad",
        "Chennai","Mumbai","Delhi","Bangalore","Chennai"
    ],

    "Occupation" : [
        "Engineer","Teacher","Business","Doctor","Engineer",
        "Banker","Business","Teacher","Engineer","Doctor",
        "Banker","Engineer","Business","Teacher","Doctor"
    ],

    "Monthly_Income" : [
        60000,45000,90000,80000,70000,
        50000,120000,47000,65000,85000,
        55000,np.nan,100000,48000,75000
    ],

    "Loan_Amount": [
        300000,200000,500000,450000,350000,
        250000,700000,220000,400000,480000,
        260000,330000,650000,240000,420000
    ],

    "Loan_Type": [
        "Home","Education","Business","Home","Car",
        "Education","Business","Car","Home","Home",
        "Education","Car","Business","Education","Home"
    ],

    "Credit_Score": [
        750,680,810,790,720,
        690,830,660,740,800,
        710,700,820,675,780
    ],

    "Loan_Status": [
        "Approved","Approved","Approved","Approved","Rejected",
        "Approved","Approved","Rejected","Approved","Approved",
        "Approved","Rejected","Approved","Approved","Approved"
    ]
}

df = pd.DataFrame(data)

print("=" * 70)
print("BANK LOAN ANALYSIS SYSTEM")
print("=" * 70)

# print(df)

print("\nFirst 5 Records")
print(df.head())

print("\nLast 5 Records")
print(df.tail())
    
print("\nShape of the Dataset")
print(df.shape)
print(df.shape[0]) # shows number of rows
print(df.shape[1]) # shows number of columns

print("\nColumn names")
print(df.columns)
print(df.columns[1])
print(df.columns.tolist()) #Python list instead of an Index

print("\nData Types")
print(df.dtypes)  #NaN is a floating-point value. To accommodate it, Pandas converts the whole column to float64.

print("\nDataset Information")
df.info()

print("\nMissing Values in Each Column")
print(df.isnull().sum())

print("\nStatistical Summary")
print(df.describe()) # works only on numerical data

print("\nCategorical Data summary")
print(df.describe(include=object)) #displays a statistical summary of all categorical (text/string) columns in the DataFrame, such as count, unique values, most frequent value (top), and its frequency (freq).

#Handling missing values
df["Age"]= df["Age"].fillna(df["Age"].mean())# Age values are usually more evenly distributed, so the mean is a reasonable estimate.
df["Monthly_Income"]=df["Monthly_Income"].fillna(df["Monthly_Income"].median()) # Income can have extreme values (outliers), so the median gives a better representation of a typical customer.

print("\nMissing Values in Each Column")
print(df.isnull().sum())

print("\nDuplicated Records")
print(df.duplicated().sum()) #Returns the number of duplicate rows.

print("\nDuplicate Rows")
print(df[df.duplicated()])   #Returns the actual duplicate rows.

# -------------------------------------------------------------
# FEATURE ENGINEERING
# -------------------------------------------------------------

#Feature Engineering is the process of creating new, meaningful variables (features) from existing data to improve analysis or machine learning models.
df["Annual_Income"] = df["Monthly_Income"] * 12
print("\nAnnual Income") #Banks usually compare the loan amount against the customer's annual income, not monthly income.
print(df[["Name", "Monthly_Income", "Annual_Income"]])

# Loan-to-Income Ratio
df["Loan_to_Income_Ratio"] = (df["Loan_Amount"] / df["Annual_Income"])
print("\nLoan-to-Income Ratio")
print(df[["Name", "Annual_Income", "Loan_Amount", "Loan_to_Income_Ratio"]])

# Risk Level based on Loan-to-Income Ratio
df["Risk_Level"] = np.where(
    df["Loan_to_Income_Ratio"] < 0.5 , "Low",
    np.where(
        df["Loan_to_Income_Ratio"] <= 1 , "Medium",
        "High"
    )
)
print("\nRisk Level")
print(df[["Name", "Loan_to_Income_Ratio", "Risk_Level"]])

# Loan Approval Recommendation
df["Loan_Recommendation"] = np.where(
    (df["Credit_Score"] >= 750) & (df["Risk_Level"] == "Low"),
    "Approved",
    np.where((df["Credit_Score"] >= 700) & (df["Risk_Level"] == "Medium"),
    "Review",
    "Rejected"
    )
)
print("\nLoan Recommendation")
print(df[["Name", "Credit_Score", "Risk_Level", "Loan_Recommendation"]])

# ----------------------------------------------------------------------
# BUSINESS ANALYSIS
# ----------------------------------------------------------------------

print("\nLoan Recommendation Summary")
print(df["Loan_Recommendation"].value_counts())

print("\nAverage Monthly Income by Occupation")
print(df.groupby("Occupation")["Monthly_Income"].mean())

print("\nAverage Credit Score by Loan Status")
print(df.groupby("Loan_Status")["Credit_Score"].mean())

print("\nTotal Loan Amount by City")
print(df.groupby("city")["Loan_Amount"].sum())

print("\nLoan Type Distribution")
print(df["Loan_Type"].value_counts())

print("\nAverage Loan Amount by Loan Type")
print(df.groupby("Loan_Type")["Loan_Amount"].mean())

print("\nAverage Age by Loan Status")
print(df.groupby("Loan_Status")["Age"].mean())

print("\nTop 5 customers by Loan Amount")
print(
    df.nlargest(5,"Loan_Amount")
    [["Name","Loan_Amount","Loan_Type"]]
)

print("\nCustomer with Highest Credit Score")

print(
    df.nlargest(1, "Credit_Score")
    [["Name", "Credit_Score", "Loan_Status"]]
)

print("\nCustomer with Lowest Credit Score")

print(
    df.nsmallest(1, "Credit_Score")
    [["Name", "Credit_Score", "Loan_Status"]]
)

