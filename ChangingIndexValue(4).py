>>> index = ["apple","banana","grapes","orange","strawberry"]
>>> s.index = index
>>> print(s)
apple         10
banana        20
grapes        30
orange        40
strawberry    50
Name: numbers, dtype: int64
>>> s.name = "calories"
>>> print(s)
apple         10
banana        20
grapes        30
orange        40
strawberry    50
Name: calories, dtype: int64

Indexing:
>>> s["grapes"]
np.int64(30)
>>> s[["grapes","apple"]]
grapes    30
apple     10
Name: calories, dtype: int64

Indexing using function "loc" - label based indexing 
NOTE: In label based indexing start value as well as stop value both are included in the output
>>> s.loc["grapes"]
np.int64(30)
