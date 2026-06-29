Invalid values
>>> df["Promoted Salary"] = df["Promoted Salary"].apply(lambda x:x/10 if x > 650000 else x)
>>> print(df)
      Name   Age     Dept   Salary  Promoted Salary
0    Alice  25.0       HR  50000.0         505000.0
1      Bob  30.0       IT  60000.0         605000.0
2  Charlie  35.0  Finance  70000.0          70500.0
3    David   NaN       IT  62000.0         625000.0
4      Eve  29.0       HR      NaN              NaN
5    Alice  25.0       HR  50000.0         505000.0
