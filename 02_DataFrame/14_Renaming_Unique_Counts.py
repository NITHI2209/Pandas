import pandas as pd
import numpy as np

print("=" * 60)
print("RENAMING, UNIQUE VALUES & VALUE COUNTS")
print("=" * 60)

# Creating a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [55000, 65000, 75000, 67000, np.nan, 55000]
}

# Creating the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# ---------------------------------------------------
# Renaming a Column
# ---------------------------------------------------

print("\nRenaming 'Department' to 'Dept'...\n")

df.rename(columns={"Department": "Dept"}, inplace=True)

print("Updated DataFrame:")
print(df)

# ---------------------------------------------------
# Unique Values
# ---------------------------------------------------

print("\nUnique Values in 'Dept':")
print(df["Dept"].unique())

print("\nUnique Values in 'Salary':")
print(df["Salary"].unique())

# ---------------------------------------------------
# Value Counts
# ---------------------------------------------------

print("\nCount of Employees in Each Department:")
print(df["Dept"].value_counts())