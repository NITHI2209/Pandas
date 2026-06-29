shape:
>>> df.shape
(6, 3)

Information:
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   Name        6 non-null      object
 1   Department  6 non-null      object
 2   Salary      5 non-null      float64
dtypes: float64(1), object(2)
memory usage: 276.0+ bytes

Describe:
>>> df.describe()
             Salary
count      5.000000
mean   58400.000000
std     8532.291603
min    50000.000000
25%    50000.000000
50%    60000.000000
75%    62000.000000
max    70000.000000
