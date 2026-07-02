import pandas as pd
import numpy as np

print("=" * 70)
print("HOSPITAL PATIENT ANALYSIS SYSTEM")
print("=" * 70)

# ---------------------------------------------
# CREATE DATASET
# ---------------------------------------------

data = {
    "Patient_ID": [
        101,102,103,104,105,106,107,108,109,110,
        111,112,113,114,115,116,117,118,119,120
    ],

    "Patient_Name": [
        "Arun","Priya","Rahul","Sneha","Kiran",
        "Anjali","Vijay","Meena","Rohit","Divya",
        "Suresh","Neha","Ajay","Pooja","Karthick",
        "Deepa","Manoj","Lakshmi","Harish","Nisha"
    ],

    "Age": [
        25,34,52,29,47,
        38,61,30,44,36,
        np.nan,28,55,41,33,
        50,27,46,39,31
    ],

    "Gender": [
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female"
    ],
    
    "City": [
        "Chennai","Bangalore","Mumbai","Delhi","Hyderabad",
        "Chennai","Mumbai","Bangalore","Delhi","Hyderabad",
        "Chennai","Mumbai","Delhi","Bangalore","Chennai",
        "Hyderabad","Mumbai","Delhi","Chennai","Bangalore"
    ],
    
    "Department": [
        "Cardiology","Neurology","Orthopedics","General Medicine","Pediatrics",
        "Cardiology","Neurology","Orthopedics","General Medicine","Pediatrics",
        "Cardiology","Neurology","Orthopedics","General Medicine","Pediatrics",
        "Cardiology","Neurology","Orthopedics","General Medicine","Pediatrics"
    ],

    "Disease": [
        "Heart Disease","Stroke","Fracture","Fever","Asthma",
        "Hypertension","Migraine","Arthritis","Diabetes","Pneumonia",
        "Heart Disease","Stroke","Fracture","Fever","Asthma",
        "Hypertension","Migraine","Arthritis","Diabetes","Pneumonia"
    ],

    "Doctor": [
        "Dr. Sharma","Dr. Mehta","Dr. Reddy","Dr. Kumar","Dr. Patel",
        "Dr. Sharma","Dr. Mehta","Dr. Reddy","Dr. Kumar","Dr. Patel",
        "Dr. Sharma","Dr. Mehta","Dr. Reddy","Dr. Kumar","Dr. Patel",
        "Dr. Sharma","Dr. Mehta","Dr. Reddy","Dr. Kumar","Dr. Patel"
    ],

        "Admission_Date": pd.to_datetime([
        "2025-01-05","2025-01-08","2025-01-10","2025-01-12","2025-01-15",
        "2025-01-18","2025-01-20","2025-01-22","2025-01-25","2025-01-28",
        "2025-02-01","2025-02-03","2025-02-06","2025-02-09","2025-02-12",
        "2025-02-15","2025-02-18","2025-02-20","2025-02-23","2025-02-25"
    ]),

    "Discharge_Date": pd.to_datetime([
        "2025-01-10","2025-01-12","2025-01-15","2025-01-14","2025-01-20",
        "2025-01-22","2025-01-24","2025-01-27","2025-01-30","2025-02-01",
        "2025-02-05","2025-02-06","2025-02-11","2025-02-13","2025-02-16",
        "2025-02-19","2025-02-21","2025-02-24","2025-02-27","2025-03-01"
    ]),

    "Treatment_Cost": [
        50000,75000,40000,15000,30000,
        55000,80000,45000,35000,60000,
        52000,70000,42000,18000,32000,
        58000,68000,47000,38000,62000
    ],

    "Insurance": [
        "Yes","No","Yes","Yes","No",
        "Yes","Yes","No","Yes","No",
        "Yes","No","Yes","Yes","No",
        "Yes","Yes","No","Yes","No"
    ],

    "Patient_Status": [
        "Recovered","Recovered","Recovered","Recovered","Under Treatment",
        "Recovered","Recovered","Recovered","Recovered","Under Treatment",
        "Recovered","Recovered","Recovered","Recovered","Recovered",
        "Recovered","Recovered","Under Treatment","Recovered","Recovered"
    ]
}

df = pd.DataFrame(data)
print(df)

# ---------------------------------------------
# BASIC DATA EXPLORATION
# ---------------------------------------------

print("\nFirst 5 Records")
print(df.head())

print("\nLast 5 Records")
print(df.tail())

print("\nShape of the Dataset")
print(df.shape)
print("Number of Rows :", df.shape[0])
print("Number of Columns :", df.shape[1])

print("\nColumn Names")
print(df.columns)
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nDataset Information")
df.info()

print("\nMissing Values")
print(df.isnull().sum())

print("\nStatistical Summary")
print(df.describe())

print("\nCategorical Summary")
print(df.describe(include="object"))

# ---------------------------------------------
# DATA CLEANING
# ---------------------------------------------

# Fill missing Age with Mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nNumber of Duplicate Records")
print(df.duplicated().sum())

print("\nDuplicate Records")
print(df[df.duplicated()])

# ---------------------------------------------
# Feature 1: Hospital Stay (Days)
# ---------------------------------------------
df["Hospital_Stay_Days"] = (df["Discharge_Date"] - df["Admission_Date"]).dt.days 
#The subtraction produces a timedelta object (a duration). The .dt.days accessor extracts just the number of days as an integer.
print("\nHospital Stay (Days)")
print(df[[
    "Patient_Name",
    "Admission_Date",
    "Discharge_Date",
    "Hospital_Stay_Days"
]])

# ---------------------------------------------
# Feature 2: Age Group
# ---------------------------------------------
df["Age_Group"] = np.where(
    df["Age"] < 18, "Child",
    np.where(
        df["Age"] <= 35 ,"Young Adult",
    np.where(
        df["Age"] <= 50, "Adult",
        "Senior Citizen"
        )
    )
)
print("\nAge Group")
print(df[["Patient_Name", "Age", "Age_Group"]])

# ---------------------------------------------
# Feature 3: Cost Category
# ---------------------------------------------

df["Cost_Category"] = np.where(
    df["Treatment_Cost"] < 30000 , "Low",
    np.where (
        df["Treatment_Cost"] <= 60000 ,"Medium",
        "High "
    )

)

print("\nCost Category")
print(df[[
    "Patient_Name",
    "Treatment_Cost",
    "Cost_Category"
]])

# ---------------------------------------------
# Feature 4: Cost Per Day
# ---------------------------------------------

df["Cost_Per_Day"] = (
    df["Treatment_Cost"] / df["Hospital_Stay_Days"]
)

print("\nCost Per Day")
print(df[[
    "Patient_Name",
    "Treatment_Cost",
    "Hospital_Stay_Days",
    "Cost_Per_Day"
]])

# ---------------------------------------------
# Feature 5: Insurance Status
# ---------------------------------------------

df["Insurance_Status"] = np.where(
    df["Insurance"] == "Yes",
    "Insured",
    "Not Insured"
)

print("\nInsurance Status")
print(df[[
    "Patient_Name",
    "Insurance",
    "Insurance_Status"
]])

# ---------------------------------------------
# Business Analysis 1: Total Number of Patients
# ---------------------------------------------

print("\nTotal Number of Patients")
print(df["Patient_ID"].count())

# ---------------------------------------------
# Business Analysis 2: Department-wise Patient Count
# ---------------------------------------------
print("\nDepartment-Wise Patient Count")
print(df["Department"].value_counts())

# ---------------------------------------------
# Business Analysis 3: Most Common Disease
# ---------------------------------------------

print("\nDisease Frequency")
print(df["Disease"].value_counts())

# ---------------------------------------------
# Business Analysis 4: Average Treatment Cost
# ---------------------------------------------

print("\nAverage Treatment Cost")
print(df["Treatment_Cost"].mean())

# ---------------------------------------------
# Business Analysis 5: Average Hospital Stay
# ---------------------------------------------

print("\nAverage Hospital Stay")
print(df["Hospital_Stay_Days"].mean())

# ---------------------------------------------
# Business Analysis 6: Highest Treatment Cost
# ---------------------------------------------

print("\nPatient with Highest Treatment Cost")

highest_cost = df[df["Treatment_Cost"] == df["Treatment_Cost"].max()]

print(highest_cost[[
    "Patient_Name",
    "Department",
    "Disease",
    "Treatment_Cost"
]])

# ---------------------------------------------
# Business Analysis 7: Patient with Lowest Treatment Cost
# ---------------------------------------------

print("\nPatient with Lowest Treatment Cost")

lowest_cost = df[df["Treatment_Cost"] == df["Treatment_Cost"].min()]

print(lowest_cost[[
    "Patient_Name",
    "Department",
    "Disease",
    "Treatment_Cost"
]])

# ---------------------------------------------
# Business Analysis 9: Average Hospital Stay by Department
# ---------------------------------------------

print("\nAverage Hospital Stay by Department")

print(df.groupby("Department")["Hospital_Stay_Days"].mean())

# ---------------------------------------------
# Business Analysis 10: Insurance Coverage Summary
# ---------------------------------------------

print("\nInsurance Coverage Summary")

print(df["Insurance_Status"].value_counts())

# ---------------------------------------------
# Business Analysis 11: Gender-wise Patient Count
# ---------------------------------------------

print("\nGender-wise Patient Count")

print(df["Gender"].value_counts())

# ---------------------------------------------
# Business Analysis 12: Top 5 Most Expensive Treatments
# ---------------------------------------------

print("\nTop 5 Most Expensive Treatments")

print(
    df.nlargest(5, "Treatment_Cost")[[
        "Patient_Name",
        "Department",
        "Disease",
        "Treatment_Cost"
    ]]
)

