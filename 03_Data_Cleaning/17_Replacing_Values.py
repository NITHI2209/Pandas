import pandas as pd
import numpy as np

print("=" * 60)
print("REPLACING VALUES")
print("=" * 60)

# Creating a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Dept": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}

# Creating DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# ---------------------------------------------------
# Replacing Values
# ---------------------------------------------------

print("\nReplacing 'Charlie' with 'Rose'...\n")

updated_names = df["Name"].replace("Charlie", "Rose")

print(updated_names)

# ---------------------------------------------------
# Replacing Values in the Original DataFrame
# ---------------------------------------------------

print("\nUpdating the DataFrame using replace()...\n")

df["Name"] = df["Name"].replace("Charlie", "Rose")

print(df)

# ---------------------------------------------------
# Note
# ---------------------------------------------------

print("\nNote:")
print("replace() is used to replace one or more values")
print("in a Series or DataFrame.")