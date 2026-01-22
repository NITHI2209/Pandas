>>> import pandas as pd
>>> import numpy as np
#DATA SET
>>> data = {
... "EmployeeID" : [101,102,103,104,105,106,107,108],
... "Age" : [25,30,28,35,np.nan,40,29,32],
... "Department" :["HR","IT","Finance","IT","HR","Finance","IT","HR"],
... "Salary" : [30000,50000,45000,60000,32000,np.nan,52000,35000],
... "Attrition" : ["Yes","No","No","Yes","No","No","Yes","No"]
... }
>>> df = pd.DataFrame(data)
>>> print(df)
   EmployeeID   Age Department   Salary Attrition
0         101  25.0         HR  30000.0       Yes
1         102  30.0         IT  50000.0        No
2         103  28.0    Finance  45000.0        No
3         104  35.0         IT  60000.0       Yes
4         105   NaN         HR  32000.0        No
5         106  40.0    Finance      NaN        No
6         107  29.0         IT  52000.0       Yes
7         108  32.0         HR  35000.0        No

#BASIC DATA EXPLORATION 
>>> df.head()
   EmployeeID   Age Department   Salary Attrition
0         101  25.0         HR  30000.0       Yes
1         102  30.0         IT  50000.0        No
2         103  28.0    Finance  45000.0        No
3         104  35.0         IT  60000.0       Yes
4         105   NaN         HR  32000.0        No
  
>>> df.tail()
   EmployeeID   Age Department   Salary Attrition
3         104  35.0         IT  60000.0       Yes
4         105   NaN         HR  32000.0        No
5         106  40.0    Finance      NaN        No
6         107  29.0         IT  52000.0       Yes
7         108  32.0         HR  35000.0        No
  
>>> df.info
<bound method DataFrame.info of    EmployeeID   Age Department   Salary Attrition
0         101  25.0         HR  30000.0       Yes
1         102  30.0         IT  50000.0        No
2         103  28.0    Finance  45000.0        No
3         104  35.0         IT  60000.0       Yes
4         105   NaN         HR  32000.0        No
5         106  40.0    Finance      NaN        No
6         107  29.0         IT  52000.0       Yes
7         108  32.0         HR  35000.0        No>

>>> df.shape
(8, 5)

>>> df.describe()
       EmployeeID        Age        Salary
count     8.00000   7.000000      7.000000
mean    104.50000  31.285714  43428.571429
std       2.44949   4.956958  11370.387605
min     101.00000  25.000000  30000.000000
25%     102.75000  28.500000  33500.000000
50%     104.50000  30.000000  45000.000000
75%     106.25000  33.500000  51000.000000
max     108.00000  40.000000  60000.000000

#HANDLING MISSING VALUES
>>> df.fillna(df["Age"].mean())
   EmployeeID        Age Department        Salary Attrition
0         101  25.000000         HR  30000.000000       Yes
1         102  30.000000         IT  50000.000000        No
2         103  28.000000    Finance  45000.000000        No
3         104  35.000000         IT  60000.000000       Yes
4         105  31.285714         HR  32000.000000        No
5         106  40.000000    Finance     31.285714        No
6         107  29.000000         IT  52000.000000       Yes
7         108  32.000000         HR  35000.000000        No

>>> df["Salary"].fillna(df["Salary"].median())
0    30000.0
1    50000.0
2    45000.0
3    60000.0
4    32000.0
5    45000.0
6    52000.0
7    35000.0
Name: Salary, dtype: float64

CHECK FOR DUPLICATES
>>> df_dup = df[df.duplicated()]
>>> print(df_dup)
Empty DataFrame
Columns: [EmployeeID, Age, Department, Salary, Attrition]
Index: []

ATTRITON ANALYSIS
Total employees
>>> df["EmployeeID"].count()
np.int64(8)

Attrition count

