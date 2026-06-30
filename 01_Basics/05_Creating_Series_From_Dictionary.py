import pandas as pd

print("=" * 60)
print("CREATING SERIES FROM A DICTIONARY")
print("=" * 60)

# Creating a dictionary
fruit_protein = {
    "Avocado": 2.0,
    "Guava": 2.6,
    "Blackberries": 2.0,
    "Oranges": 0.9,
    "Banana": 1.1,
    "Apples": 0.3,
    "Kiwi": 1.1,
    "Pomegranate": 1.7,
    "Mango": 0.8,
    "Cherries": 1.0
}

# Creating a Series from the dictionary
s2 = pd.Series(fruit_protein, name="Protein")

print("\nSeries created from Dictionary:")
print(s2)

# Display additional information
print("\nData Type:")
print(s2.dtype)

print("\nNumber of Fruits:")
print(len(s2))

print("\nIndex Labels:")
print(s2.index)

print("\nValues:")
print(s2.values)
