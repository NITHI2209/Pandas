>>> department_info = {
... "Department" : ["HR","IT","Finance"],
... "Location" : ["New york","San Fransisco","Chicago"],
... "Manager" : ["Laura","Steve","Nina"]
... }
>>> df2 = pd.DataFrame(department_info)
>>> print(df2)
  Department       Location Manager
0         HR       New york   Laura
1         IT  San Fransisco   Steve
2    Finance        Chicago    Nina

>>> pd.concat([df,df2])
      Name   Age     Dept   Salary  Promoted Salary Department       Location Manager
0    Alice  25.0       HR  50000.0         505000.0        NaN            NaN     NaN
1      Bob  30.0       IT  60000.0         605000.0        NaN            NaN     NaN
2  Charlie  35.0  Finance  70000.0          70500.0        NaN            NaN     NaN
3    David   NaN       IT  62000.0         625000.0        NaN            NaN     NaN
4      Eve  29.0       HR      NaN              NaN        NaN            NaN     NaN
5    Alice  25.0       HR  50000.0         505000.0        NaN            NaN     NaN
0      NaN   NaN      NaN      NaN              NaN         HR       New york   Laura
1      NaN   NaN      NaN      NaN              NaN         IT  San Fransisco   Steve
2      NaN   NaN      NaN      NaN              NaN    Finance        Chicago    Nina
  
>>> pd.concat([df,df2],axis = 1)
      Name   Age     Dept   Salary  Promoted Salary Department       Location Manager
0    Alice  25.0       HR  50000.0         505000.0         HR       New york   Laura
1      Bob  30.0       IT  60000.0         605000.0         IT  San Fransisco   Steve
2  Charlie  35.0  Finance  70000.0          70500.0    Finance        Chicago    Nina
3    David   NaN       IT  62000.0         625000.0        NaN            NaN     NaN
4      Eve  29.0       HR      NaN              NaN        NaN            NaN     NaN
5    Alice  25.0       HR  50000.0         505000.0        NaN            NaN     NaN

>>> pd.merge(df,df2,on = "Dept")
      Name   Age     Dept   Salary  Promoted Salary       Location Manager
0    Alice  25.0       HR  50000.0         505000.0       New york   Laura
1      Bob  30.0       IT  60000.0         605000.0  San Fransisco   Steve
2  Charlie  35.0  Finance  70000.0          70500.0        Chicago    Nina
3    David   NaN       IT  62000.0         625000.0  San Fransisco   Steve
4      Eve  29.0       HR      NaN              NaN       New york   Laura
5    Alice  25.0       HR  50000.0         505000.0       New york   Laura

JOINS
INNER JOIN
>>> pd.merge(df,df2,on = "Dept",how = "inner")
      Name   Age     Dept   Salary  Promoted Salary       Location Manager
0    Alice  25.0       HR  50000.0         505000.0       New york   Laura
1      Bob  30.0       IT  60000.0         605000.0  San Fransisco   Steve
2  Charlie  35.0  Finance  70000.0          70500.0        Chicago    Nina
3    David   NaN       IT  62000.0         625000.0  San Fransisco   Steve
4      Eve  29.0       HR      NaN              NaN       New york   Laura
5    Alice  25.0       HR  50000.0         505000.0       New york   Laura

RIGHT JOIN
>>> pd.merge(df,df2,on = "Dept",how = "right")
      Name   Age     Dept   Salary  Promoted Salary       Location Manager
0    Alice  25.0       HR  50000.0         505000.0       New york   Laura
1      Eve  29.0       HR      NaN              NaN       New york   Laura
2    Alice  25.0       HR  50000.0         505000.0       New york   Laura
3      Bob  30.0       IT  60000.0         605000.0  San Fransisco   Steve
4    David   NaN       IT  62000.0         625000.0  San Fransisco   Steve
5  Charlie  35.0  Finance  70000.0          70500.0        Chicago    Nina
  
OUTER JOIN
>>> pd.merge(df,df2,on = "Dept",how = "outer")
      Name   Age     Dept   Salary  Promoted Salary       Location Manager
0  Charlie  35.0  Finance  70000.0          70500.0        Chicago    Nina
1    Alice  25.0       HR  50000.0         505000.0       New york   Laura
2      Eve  29.0       HR      NaN              NaN       New york   Laura
3    Alice  25.0       HR  50000.0         505000.0       New york   Laura
4      Bob  30.0       IT  60000.0         605000.0  San Fransisco   Steve
5    David   NaN       IT  62000.0         625000.0  San Fransisco   Steve

LEFT JOIN
>>> pd.merge(df,df2,on = "Dept",how = "left")
      Name   Age     Dept   Salary  Promoted Salary       Location Manager
0    Alice  25.0       HR  50000.0         505000.0       New york   Laura
1      Bob  30.0       IT  60000.0         605000.0  San Fransisco   Steve
2  Charlie  35.0  Finance  70000.0          70500.0        Chicago    Nina
3    David   NaN       IT  62000.0         625000.0  San Fransisco   Steve
4      Eve  29.0       HR      NaN              NaN       New york   Laura
5    Alice  25.0       HR  50000.0         505000.0       New york   Laura
