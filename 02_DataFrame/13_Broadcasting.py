import pandas as pd
import numpy as np

print("=" * 60)
print("BROADCASTING IN PANDAS")
print("=" * 60)

# Creating a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}

# Creating the DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# ---------------------------------------------------
# Broadcasting
# ---------------------------------------------------

print("\nAdding ₹5000 to every employee's salary...\n")

df["Salary"] = df["Salary"] + 5000

print("Updated DataFrame:")
print(df)

# ---------------------------------------------------
# Note
# ---------------------------------------------------

print("\nNote:")
print("Broadcasting performs an operation on an entire column")
print("without using an explicit loop.")