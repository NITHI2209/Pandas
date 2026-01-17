Rename:
>>> df.rename(columns={"Department":"Dept"},inplace = True)
>>> print(df)
      Name     Dept   Salary
0    Alice       HR  55000.0
1      Bob       IT  65000.0
2  Charlie  Finance  75000.0
3    David       IT  67000.0
4      Eve       HR      NaN
5    Alice       HR  55000.0

Unique Values:
>>> df["Dept"].unique()
array(['HR', 'IT', 'Finance'], dtype=object)
>>> df["Salary"].unique()
array([55000., 65000., 75000., 67000.,    nan])

Counting:
>>> df["Dept"].value_counts()
Dept
HR         3
IT         2
Finance    1
Name: count, dtype: int64
