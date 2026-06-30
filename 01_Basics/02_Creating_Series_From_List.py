import pandas as pd

# Creating a Series
s = pd.Series([10, 20, 30, 40, 50])

print("Series:")
print(s)

print("\nType of data:")
print(s.dtype)

print("\nIdentifying values of the Series:")
print(s.values)

print("\nIndex:")
print(s.index)

print("\nAssigning name to the Series:")
s.name = "numbers"
print(s)
