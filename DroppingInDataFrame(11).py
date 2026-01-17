>>> df.drop("Age",axis =1 ) 
      Name Department   Salary
0    Alice         HR  50000.0
1      Bob         IT  60000.0
2  Charlie    Finance  70000.0
3    David         IT  62000.0
4      Eve         HR      NaN
5    Alice         HR  50000.0

>>> df.drop("Age",axis = 1, inplace = True) # inplace - the data is deleted in original dataframe if inplace is true
>>> print(df)
      Name Department   Salary
0    Alice         HR  50000.0
1      Bob         IT  60000.0
2  Charlie    Finance  70000.0
3    David         IT  62000.0
4      Eve         HR      NaN
5    Alice         HR  50000.0
