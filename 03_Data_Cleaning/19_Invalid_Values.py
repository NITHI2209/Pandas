import pandas as pd
import numpy as np

print("=" * 60)
print("HANDLING INVALID VALUES")
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

# Creating a Promoted Salary column
df["Promoted Salary"] = df["Salary"] + 5000

print("Original DataFrame:")
print(df)

# ---------------------------------------------------
# Introducing an Invalid Value (for demonstration)
# ---------------------------------------------------

print("\nIntroducing an invalid value...")

df.loc[2, "Promoted Salary"] = 705000

print("\nDataFrame with Invalid Value:")
print(df)

# ---------------------------------------------------
# Correcting Invalid Values using apply()
# ---------------------------------------------------

print("\nCorrecting invalid values...")

df["Promoted Salary"] = df["Promoted Salary"].apply(
    lambda x: x / 10 if pd.notna(x) and x > 650000 else x
)

print("\nCorrected DataFrame:")
print(df)

# ---------------------------------------------------
# Note
# ---------------------------------------------------

print("\nNote:")
print("apply() applies a function to every value in a column.")
print("Here, salaries greater than 650000 are treated as")
print("invalid and corrected by dividing them by 10.")