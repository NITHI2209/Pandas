AND operator (&):
>>> [(s2>0.5) & (s2<2)]
[Avocado         False
Guava           False
Blackberries    False
Oranges          True
Banana           True
Apples          False
Kiwi             True
Pomegranate      True
Mango            True
Cherries         True
Name: Protein, dtype: bool]

>>> s2[(s2>0.5) & (s2<2)]
Oranges        0.9
Banana         1.1
Kiwi           1.1
Pomegranate    1.7
Mango          0.8
Cherries       1.0
Name: Protein, dtype: float64

OR operator(|):
>>> s2[(s2>0.5) | (s2<=2)]
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

NOT Operaotr(~):
>>> s2[~(s2>1)] # not greater than one
Oranges     0.9
Apples      0.3
Mango       0.8
Cherries    1.0
Name: Protein, dtype: float64
