import pandas as pd

print("=" * 60)
print("CONDITIONAL FILTERING")
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

print("Protein Content (g per 100g):")
print(s2)

# ---------------------------------------------------
# Conditional Statement
# ---------------------------------------------------

print("\nChecking which fruits have protein greater than 1g:")
print(s2 > 1)

# ---------------------------------------------------
# Filtering Data
# ---------------------------------------------------

print("\nFruits with protein greater than 1g:")
print(s2[s2 > 1])