MISSING VALUES:
1)Getting rid of them -> dropna()
2)Filling them up -> fillna()
3)Forward filling -> ffill()   # fills the null value by before value but shows error if first value is null
4)Backward filling -> bfill()  #fills the null value by after value but shows error if last value is null

 dropna()
>>> df.dropna()  #drops the row which has null value
      Name   Age     Dept   Salary  Promoted Salary
0    Alice  25.0       HR  50000.0         500000.0
1      Bob  30.0       IT  60000.0         600000.0
2  Charlie  35.0  Finance  70000.0         700000.0
5    Alice  25.0       HR  50000.0         500000.0
>>> df.dropna(how="any")   #drops the row which has null value
      Name   Age     Dept   Salary  Promoted Salary
0    Alice  25.0       HR  50000.0         500000.0
1      Bob  30.0       IT  60000.0         600000.0
2  Charlie  35.0  Finance  70000.0         700000.0
5    Alice  25.0       HR  50000.0         500000.0
>>> df.dropna(how = "all") # drops  the row if the entire row contains null value
      Name   Age     Dept   Salary  Promoted Salary
0    Alice  25.0       HR  50000.0         500000.0
1      Bob  30.0       IT  60000.0         600000.0
2  Charlie  35.0  Finance  70000.0         700000.0
3    David   NaN       IT  62000.0         620000.0
4      Eve  29.0       HR      NaN              NaN
5    Alice  25.0       HR  50000.0         500000.0

 fillna()
>>> df.fillna(0)
      Name   Age     Dept   Salary  Promoted Salary
0    Alice  25.0       HR  50000.0         500000.0
1      Bob  30.0       IT  60000.0         600000.0
2  Charlie  35.0  Finance  70000.0         700000.0
3    David   0.0       IT  62000.0         620000.0
4      Eve  29.0       HR      0.0              0.0
5    Alice  25.0       HR  50000.0         500000.0
>>> df.fillna(df["Age"].mean())
      Name   Age     Dept   Salary  Promoted Salary
0    Alice  25.0       HR  50000.0         500000.0
1      Bob  30.0       IT  60000.0         600000.0
2  Charlie  35.0  Finance  70000.0         700000.0
3    David  28.8       IT  62000.0         620000.0
4      Eve  29.0       HR     28.8             28.8
5    Alice  25.0       HR  50000.0         500000.0
>>> df["Salary"].fillna(df["Salary"].median())
0    50000.0
1    60000.0
2    70000.0
3    62000.0
4    60000.0
5    50000.0

ffill()
>>> df["Age"].fillna(method = "ffill")
<python-input-17>:1: FutureWarning: Series.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
  df["Age"].fillna(method = "ffill")
0    25.0
1    30.0
2    35.0
3    35.0
4    29.0
5    25.0
Name: Age, dtype: float64

bfill()
>>> df["Age"].fillna(method = "bfill")
<python-input-18>:1: FutureWarning: Series.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
  df["Age"].fillna(method = "bfill")
0    25.0
1    30.0
2    35.0
3    29.0
4    29.0
5    25.0
Name: Age, dtype: float64

