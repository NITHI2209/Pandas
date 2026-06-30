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
print(df.describe())