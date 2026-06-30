import pandas as pd

print("=" * 60)
print("MODIFYING SERIES")
print("=" * 60)

# Creating a Series from a dictionary
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

s2 = pd.Series(fruit_protein, name="Protein")

print("Original Series:")
print(s2)

# ---------------------------------------------------
# Modifying a Value
# ---------------------------------------------------

print("\nUpdating the protein value of Mango from 0.8 to 2.8...\n")

s2["Mango"] = 2.8

print("Updated Series:")
print(s2)

# ---------------------------------------------------
# Verify the Updated Value
# ---------------------------------------------------

print("\nUpdated value of Mango:")
print(s2["Mango"])