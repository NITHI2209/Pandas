import pandas as pd
import numpy as np

print("=" * 60)
print("HANDLING DUPLICATE VALUES")
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
df["Promoted Salary"] = df["Salary"] + 5000

print("Original DataFrame:")
print(df)

# ---------------------------------------------------
# Finding Duplicate Rows (Default)
# ---------------------------------------------------

print("\nDuplicate Rows (Default - keep='first'):")
df_dup = df[df.duplicated()]
print(df_dup)

# ---------------------------------------------------
# keep='last'
# ---------------------------------------------------

print("\nDuplicate Rows (keep='last'):")
df_dup = df[df.duplicated(keep="last")]
print(df_dup)

# ---------------------------------------------------
# keep='first'
# ---------------------------------------------------

print("\nDuplicate Rows (keep='first'):")
df_dup = df[df.duplicated(keep="first")]
print(df_dup)

# ---------------------------------------------------
# Notes
# ---------------------------------------------------

print("\n" + "=" * 60)
print("NOTES")
print("=" * 60)

print("""
duplicated()
    Returns duplicate rows.

keep='first'
    Keeps the first occurrence and marks the remaining rows as duplicates.

keep='last'
    Keeps the last occurrence and marks the previous rows as duplicates.

keep=False
    Marks all duplicate rows.
""")