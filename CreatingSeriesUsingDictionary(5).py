>>> fruit_protein = {
... "Avocado":2.0,
... "Guava" : 2.6,
... "Blackberries" : 2.0,
... "Oranges": 0.9,
... "Banana":1.1,
... "Apples":0.3,
... "Kiwi":1.1,
... "Pomegranate":1.7,
... "Mango":0.8,
... "Cherries":1.0
... }
>>> s2 = pd.Series(fruit_protein,name = "Protein")
>>> print(s2)
Avocado         2.0
Guava           2.6
Blackberries    2.0
Oranges         0.9
Banana          1.1
Apples          0.3
Kiwi            1.1
Pomegranate     1.7
Mango           0.8
Cherries        1.0
Name: Protein, dtype: float64
