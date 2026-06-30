import pandas as pd

print("=" * 60)
print("SERIES INDEXING")
print("=" * 60)

# Creating a Series
s = pd.Series([10, 20, 30, 40, 50], name="numbers")

print("Series:")
print(s)

# ----------------- Basic Indexing -----------------
print("\nBasic Indexing:")

print("\nFirst Element (s[0]):")
print(s[0])

print("\nSlicing (s[0:2]):")
print(s[0:2])

# ----------------- iloc Indexing -----------------
print("\nIndexing using iloc:")
print("iloc - Location based indexing (access values using index positions)")

print("\nElement at index 3:")
print(s.iloc[3])

print("\nElements at index positions 1, 2, and 4:")
print(s.iloc[[1, 2, 4]])
