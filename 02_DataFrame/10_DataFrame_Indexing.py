import pandas as pd
import numpy as np

print("=" * 60)
print("DATAFRAME INDEXING")
print("=" * 60)

# Creating a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}

# Creating the DataFrame
df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# ---------------------------------------------------
# iloc - Position Based Indexing
# ---------------------------------------------------

print("\nRows 1 to 2 using iloc:")
print(df.iloc[1:3])

print("\nRows 1 to 2 and first 2 columns using iloc:")
print(df.iloc[1:3, :2])

# ---------------------------------------------------
# loc - Label Based Indexing
# ---------------------------------------------------

print("\nUsing loc to select Age and Department (Rows 1 to 2):")
print(df.loc[1:2, ["Age", "Department"]])

# ---------------------------------------------------
# Selecting Multiple Columns
# ---------------------------------------------------

print("\nSelecting Age and Department columns:")
print(df[["Age", "Department"]])