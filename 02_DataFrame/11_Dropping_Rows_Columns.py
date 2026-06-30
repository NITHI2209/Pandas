import pandas as pd
import numpy as np

print("=" * 60)
print("DROPPING ROWS AND COLUMNS")
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

print("Original DataFrame:")
print(df)

# ---------------------------------------------------
# Dropping a Column (Without inplace)
# ---------------------------------------------------

print("\nDropping 'Age' column (without inplace):")
new_df = df.drop("Age", axis=1)
print(new_df)

print("\nOriginal DataFrame remains unchanged:")
print(df)

# ---------------------------------------------------
# Dropping a Column (With inplace=True)
# ---------------------------------------------------

print("\nDropping 'Age' column using inplace=True...")
df.drop("Age", axis=1, inplace=True)

print("\nUpdated Original DataFrame:")
print(df)