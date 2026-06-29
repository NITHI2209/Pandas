>>> import pandas as pd
>>> s = pd.Series([10,20,30,40,50])
>>> print(s)
0    10
1    20
2    30
3    40
4    50
dtype: int64

Type of data:
>>> s.dtype
dtype('int64')
  
Identifying values of the series:
>>> s.values
array([10, 20, 30, 40, 50])

Index:
>>> s.index
RangeIndex(start=0, stop=5, step=1)

Assinging name to the column:
>>> s.name = "numbers"
>>> print(s)
0    10
1    20
2    30
3    40
4    50
Name: numbers, dtype: int64
