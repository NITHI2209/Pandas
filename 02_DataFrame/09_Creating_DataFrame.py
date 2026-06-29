>>> import pandas as pd
>>> import numpy as np
>>> data = {
... "Name":["Alice","Bob","Charlie","David","Eve","Alice"],
... "Age":[25,30,35,np.nan,29,25],
... "Department":["HR","IT","Finance","IT","HR","HR"],
... "Salary":[50000,60000,70000,62000,np.nan,50000]
... }
>>> df = pd.DataFrame(data)
>>> print(df)
      Name   Age Department   Salary
0    Alice  25.0         HR  50000.0
1      Bob  30.0         IT  60000.0
2  Charlie  35.0    Finance  70000.0
3    David   NaN         IT  62000.0
4      Eve  29.0         HR      NaN
5    Alice  25.0         HR  50000.0

>>> df.head(2)  #shows first 2 values
    Name   Age Department   Salary
0  Alice  25.0         HR  50000.0
1    Bob  30.0         IT  60000.0
>>> df.tail(3) #shows last 3 values
    Name   Age Department   Salary
3  David   NaN         IT  62000.0
4    Eve  29.0         HR      NaN
5  Alice  25.0         HR  50000.0
