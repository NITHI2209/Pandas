import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

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

    "City" : [
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



plt.figure(figsize=(6, 4))

sns.countplot(
    data=df,
    x="Loan_Status"
)

plt.title("Loan Status Distribution")
plt.xlabel("Loan Status")
plt.ylabel("Number of Customers")

plt.show()
# Refer figure loan_status_distribution.png



plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Occupation",
    y="Monthly_Income"
)

plt.title("Average Monthly Income by Occupation")
plt.xlabel("Occupation")
plt.ylabel("Average Monthly Income")

plt.show()
# Refer figure average_monthly_income_by_occupation.png

plt.figure(figsize=(7,5))

sns.countplot(
    data=df,
    x="Loan_Type"
)

plt.title("Loan Type Distribution")
plt.xlabel("Loan Type")
plt.ylabel("Number of Customers")

plt.show()
# Refer figure loan_type_distribution

plt.figure(figsize=(8,5))

sns.barplot(
    data=df,
    x="City",
    y="Loan_Amount",
    estimator=sum
)

plt.title("Total Loan Amount by City")
plt.xlabel("City")
plt.ylabel("Total Loan Amount")

plt.show()
# Refer Figure total_loan_amount_city


plt.figure(figsize=(7,5))

sns.histplot(
    data=df,
    x="Credit_Score",
    bins=8
)

plt.title("Credit Score Distribution")
plt.xlabel("Credit Score")
plt.ylabel("Count")

plt.show() 
# Refer figure credit_score_distribution

plt.figure(figsize=(7,5))

sns.histplot(
    data=df,
    x="Monthly_Income",
    bins=8
)

plt.title("Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Count")

plt.show()
# Refer figure monthly_income_distribution.png

plt.figure(figsize=(7,5))

sns.histplot(
    data=df,
    x="Loan_Amount",
    bins=8
)

plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Count")

plt.show()
# Refer figure loan_amount_distribution

plt.figure(figsize=(6,5))

sns.boxplot(
    data=df,
    x="Loan_Status",
    y="Credit_Score"
)

plt.title("Credit Score by Loan Status")
plt.xlabel("Loan Status")
plt.ylabel("Credit Score")

plt.show()
# Refer figure credit_score_by_loan_status

plt.figure(figsize=(7,5))

sns.scatterplot(
    data=df,
    x="Credit_Score",
    y="Loan_Amount"
)

plt.title("Loan Amount vs Credit Score")
plt.xlabel("Credit Score")
plt.ylabel("Loan Amount")

plt.show()
#Refer figure  loan_amount_vs_credit_score

plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include=["number"])

sns.heatmap(
    numeric_df.corr(),
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()
#Refer figure correlation_heatmap