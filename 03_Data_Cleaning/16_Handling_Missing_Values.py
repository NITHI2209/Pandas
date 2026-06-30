import pandas as pd
import numpy as np

print("=" * 60)
print("HANDLING MISSING VALUES")
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

# Adding a new column
df["Promoted Salary"] = df["Salary"] * 10

print("Original DataFrame:")
print(df)

# ---------------------------------------------------
# dropna()
# ---------------------------------------------------

print("\n" + "=" * 60)
print("1. dropna()")
print("=" * 60)

print("\nRows containing NO missing values:")
print(df.dropna())

print("\ndropna(how='any'):")
print(df.dropna(how="any"))

print("\ndropna(how='all'):")
print(df.dropna(how="all"))

# ---------------------------------------------------
# fillna()
# ---------------------------------------------------

print("\n" + "=" * 60)
print("2. fillna()")
print("=" * 60)

print("\nReplacing missing values with 0:")
print(df.fillna(0))

print("\nReplacing missing values with Age mean:")
print(df.fillna(df["Age"].mean()))

print("\nReplacing missing Salary with Salary median:")
print(df["Salary"].fillna(df["Salary"].median()))

# ---------------------------------------------------
# Forward Fill
# ---------------------------------------------------

print("\n" + "=" * 60)
print("3. Forward Fill (ffill)")
print("=" * 60)

print("\nAge column after forward fill:")
print(df["Age"].ffill())

# ---------------------------------------------------
# Backward Fill
# ---------------------------------------------------

print("\n" + "=" * 60)
print("4. Backward Fill (bfill)")
print("=" * 60)

print("\nAge column after backward fill:")
print(df["Age"].bfill())

# ---------------------------------------------------
# Notes
# ---------------------------------------------------

print("\n" + "=" * 60)
print("NOTES")
print("=" * 60)

print("""
1. dropna()  -> Removes rows containing missing values.

2. fillna()  -> Replaces missing values with a specified value.

3. ffill()   -> Uses the previous valid value to fill missing data.
                (Doesn't fill the first value if it's missing.)

4. bfill()   -> Uses the next valid value to fill missing data.
                (Doesn't fill the last value if it's missing.)
""")