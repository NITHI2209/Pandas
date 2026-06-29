Indexing:
>>> s[0]
np.int64(10)

>>> s[0:2]
0    10
1    20
Name: numbers, dtype: int64

Indexing using "iloc" function:
iloc- location based indexing - through index value it identify the location
>>> s.iloc[3]
np.int64(40)
>>> s.iloc[[1,2,4]]
1    20
2    30
4    50
Name: numbers, dtype: int64

