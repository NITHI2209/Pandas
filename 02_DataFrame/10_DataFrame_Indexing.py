Indexing in DataFrame
>>> df.iloc[1:3]
      Name   Age Department   Salary
1      Bob  30.0         IT  60000.0
2  Charlie  35.0    Finance  70000.0
>>> df.iloc[1:3,:2]
      Name   Age
1      Bob  30.0
2  Charlie  35.0

>>> df.loc[1:2,["Age","Department"]]
    Age Department
1  30.0         IT
2  35.0    Finance
  
>>> df[["Age","Department"]]
    Age Department
0  25.0         HR
1  30.0         IT
2  35.0    Finance
3   NaN         IT
4  29.0         HR
5  25.0         HR
