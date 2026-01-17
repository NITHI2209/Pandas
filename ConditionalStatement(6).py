Conditional statement:

>>> s2>1 # gives in bool value
Avocado          True
Guava            True
Blackberries     True
Oranges         False
Banana           True
Apples          False
Kiwi             True
Pomegranate      True
Mango           False
Cherries        False
Name: Protein, dtype: bool

only gives the protein which satisifies the condition
>>> s2[s2>1]
Avocado         2.0
Guava           2.6
Blackberries    2.0
Banana          1.1
Kiwi            1.1
Pomegranate     1.7
Name: Protein, dtype: float64
