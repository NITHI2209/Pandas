import pandas as pd
import numpy as np

print("=" * 60)
print("JOINS AND MERGES IN PANDAS")
print("=" * 60)

# ---------------------------------------------------
# Employee Data
# ---------------------------------------------------

employee_data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Dept": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}

df = pd.DataFrame(employee_data)

df["Promoted Salary"] = df["Salary"] + 5000

print("Employee DataFrame:")
print(df)

# ---------------------------------------------------
# Department Data
# ---------------------------------------------------

department_info = {
    "Dept": ["HR", "IT", "Finance"],
    "Location": ["New York", "San Francisco", "Chicago"],
    "Manager": ["Laura", "Steve", "Nina"]
}

df2 = pd.DataFrame(department_info)

print("\nDepartment DataFrame:")
print(df2)

# ===================================================
# CONCATENATION
# ===================================================

print("\n" + "=" * 60)
print("1. CONCAT (axis=0)")
print("=" * 60)

print(pd.concat([df, df2]))

print("\n" + "=" * 60)
print("2. CONCAT (axis=1)")
print("=" * 60)

print(pd.concat([df, df2], axis=1))

# ===================================================
# MERGE
# ===================================================

print("\n" + "=" * 60)
print("3. MERGE")
print("=" * 60)

print(pd.merge(df, df2, on="Dept"))

# ===================================================
# INNER JOIN
# ===================================================

print("\n" + "=" * 60)
print("4. INNER JOIN")
print("=" * 60)

print(pd.merge(df, df2, on="Dept", how="inner"))

# ===================================================
# LEFT JOIN
# ===================================================

print("\n" + "=" * 60)
print("5. LEFT JOIN")
print("=" * 60)

print(pd.merge(df, df2, on="Dept", how="left"))

# ===================================================
# RIGHT JOIN
# ===================================================

print("\n" + "=" * 60)
print("6. RIGHT JOIN")
print("=" * 60)

print(pd.merge(df, df2, on="Dept", how="right"))

# ===================================================
# OUTER JOIN
# ===================================================

print("\n" + "=" * 60)
print("7. OUTER JOIN")
print("=" * 60)

print(pd.merge(df, df2, on="Dept", how="outer"))

# ===================================================
# NOTES
# ===================================================

print("\n" + "=" * 60)
print("NOTES")
print("=" * 60)

print("""
concat(axis=0)
    Combines DataFrames vertically (adds rows).

concat(axis=1)
    Combines DataFrames horizontally (adds columns).

merge()
    Combines DataFrames using a common column.

INNER JOIN
    Returns only matching records.

LEFT JOIN
    Returns all rows from the left DataFrame.

RIGHT JOIN
    Returns all rows from the right DataFrame.

OUTER JOIN
    Returns all rows from both DataFrames.
""")