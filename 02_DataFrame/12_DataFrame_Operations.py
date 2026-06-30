import pandas as pd
import numpy as np

print("=" * 60)
print("DATAFRAME OPERATIONS")
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

# Dropping the Age column
df.drop("Age", axis=1, inplace=True)

print("DataFrame:")
print(df)

# ---------------------------------------------------
# Shape
# ---------------------------------------------------

print("\nShape of the DataFrame:")
print(df.shape)

# ---------------------------------------------------
# Information
# ---------------------------------------------------

print("\nDataFrame Information:")
df.info()

# ---------------------------------------------------
# Statistical Summary
# ---------------------------------------------------

print("\nStatistical Summary (describe):")
print(df.describe())