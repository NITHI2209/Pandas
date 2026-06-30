import pandas as pd
import numpy as np

print("=" * 60)
print("ADDING A NEW COLUMN")
print("=" * 60)

# Creating a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Dept": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}

# Creating the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# ---------------------------------------------------
# Adding a New Column
# ---------------------------------------------------

print("\nAdding a new column: 'Promoted Salary'...\n")

df["Promoted Salary"] = df["Salary"] * 10

print("Updated DataFrame:")
print(df)

# ---------------------------------------------------
# Explanation
# ---------------------------------------------------

print("\nNote:")
print("A new column can be created by assigning values")
print("to a new column name.")
print("Here, 'Promoted Salary' is calculated by")
print("multiplying the 'Salary' column by 10.")