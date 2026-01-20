Dealing with Duplicate values
>>> df_dup = df[df.duplicated()]
>>> print(df_dup)
    Name   Age Dept   Salary  Promoted Salary
5  Alice  25.0   HR  50000.0         505000.0

>>> df_dup = df[df.duplicated(keep = "last")]  # keeps last one and shows first values as duplicate
>>> print(df_dup)
    Name   Age Dept   Salary  Promoted Salary
0  Alice  25.0   HR  50000.0         505000.0

>>> df_dup = df[df.duplicated(keep = "first")] # keeps first one and shows last one as duplicate value
>>> print(df_dup)
    Name   Age Dept   Salary  Promoted Salary
5  Alice  25.0   HR  50000.0         505000.0
