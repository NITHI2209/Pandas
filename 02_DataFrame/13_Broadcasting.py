>>> df["Salary"] = df["Salary"] + 5000
>>> print(df)
      Name Department   Salary
0    Alice         HR  55000.0
1      Bob         IT  65000.0
2  Charlie    Finance  75000.0
3    David         IT  67000.0
4      Eve         HR      NaN
5    Alice         HR  55000.0

NOTE: Broadcasting is performing the operations with any diff shapes without looping 
