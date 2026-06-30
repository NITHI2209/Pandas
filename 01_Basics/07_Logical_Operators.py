import pandas as pd

print("=" * 60)
print("LOGICAL OPERATORS")
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
# AND Operator (&)
# ---------------------------------------------------

print("\nAND Operator (&)")
print("Condition: Protein > 0.5 AND Protein < 2")

print("\nBoolean Result:")
print((s2 > 0.5) & (s2 < 2))

print("\nFiltered Result:")
print(s2[(s2 > 0.5) & (s2 < 2)])

# ---------------------------------------------------
# OR Operator (|)
# ---------------------------------------------------

print("\nOR Operator (|)")
print("Condition: Protein > 0.5 OR Protein <= 2")

print("\nFiltered Result:")
print(s2[(s2 > 0.5) | (s2 <= 2)])

# ---------------------------------------------------
# NOT Operator (~)
# ---------------------------------------------------

print("\nNOT Operator (~)")
print("Condition: NOT (Protein > 1)")

print("\nFiltered Result:")
print(s2[~(s2 > 1)])