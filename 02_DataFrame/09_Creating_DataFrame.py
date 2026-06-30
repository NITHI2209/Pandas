import pandas as pd
import numpy as np

print("=" * 60)
print("CREATING A DATAFRAME")
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
# Display First Rows
# ---------------------------------------------------

print("\nFirst 2 Rows (head):")
print(df.head(2))

# ---------------------------------------------------
# Display Last Rows
# ---------------------------------------------------

print("\nLast 3 Rows (tail):")
print(df.tail(3))