import pandas as pd

print("=" * 60)
print("CHANGING INDEX VALUES")
print("=" * 60)

# Creating a Series
s = pd.Series([10, 20, 30, 40, 50], name="numbers")

print("Original Series:")
print(s)

# ---------------------------------------------------
# Changing Index Labels
# ---------------------------------------------------

index = ["apple", "banana", "grapes", "orange", "strawberry"]
s.index = index

print("\nSeries after changing index labels:")
print(s)

# ---------------------------------------------------
# Changing the Series Name
# ---------------------------------------------------

s.name = "calories"

print("\nSeries after changing the name:")
print(s)

# ---------------------------------------------------
# Label-Based Indexing
# ---------------------------------------------------

print("\nAccessing a single value using label:")
print(s["grapes"])

print("\nAccessing multiple values using labels:")
print(s[["grapes", "apple"]])

# ---------------------------------------------------
# loc Indexing
# ---------------------------------------------------

print("\nUsing loc (Label-Based Indexing)")
print("Note: In loc indexing, both the start and stop labels are included.")

print("\nSingle label using loc:")
print(s.loc["grapes"])

print("\nMultiple labels using loc:")
print(s.loc[["apple", "banana"]])