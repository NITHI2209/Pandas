#Logistics Delivery Performance Analysis
import pandas as pd
data = {
    "Shipment_ID": [201,202,203,204,205,206,207,208],
    "Origin": ["Chennai","Delhi","Mumbai","Chennai","Delhi","Mumbai","Chennai","Delhi"],
    "Destination": ["Bangalore","Jaipur","Pune","Hyderabad","Lucknow","Nagpur","Coimbatore","Agra"],
    "Distance_km": [350, 280, 150, 500, 420, 300, 200, 250],
    "Dispatch_Date": pd.to_datetime([
        "2024-01-01","2024-01-03","2024-01-05","2024-01-07",
        "2024-01-09","2024-01-11","2024-01-13","2024-01-15"
    ]),
    "Delivery_Date": pd.to_datetime([
        "2024-01-03","2024-01-05","2024-01-06","2024-01-10",
        "2024-01-13","2024-01-13","2024-01-15","2024-01-18"
    ]),
    "Transport_Mode": ["Truck","Air","Truck","Ship","Air","Truck","Truck","Ship"],
    "Cost": [15000, 25000, 8000, 20000, 27000, 12000, 9000, 18000]
}
df = pd.DataFrame(data)
print(df)
   ShipmentID   Origin Destination  Distance_km Dispatch_Date Delivery_Date Transport_Mode   Cost
0         201  Chennai   Bangalore          350    2024-01-01    2024-01-03          Truck  15000
1         202    Delhi      Jaipur          280    2024-01-03    2024-01-05            Air  25000
2         203   Mumbai        Pune          150    2024-01-05    2024-01-06          Truck   8000
3         204  Chennai   Hyderabad          500    2024-01-07    2024-01-10           Ship  20000
4         205    Delhi     Lucknow          420    2024-01-09    2024-01-13            Air  27000
5         206   Mumbai      Nagpur          300    2024-01-11    2024-01-13          Truck  12000
6         207  Chennai  Coimbatore          200    2024-01-13    2024-01-15          Truck   9000
7         208    Delhi        Agra          250    2024-01-15    2024-01-18           Ship  18000

#Calculate delivery time:
>>> df["Delivery_Time_Days"] = (df["Delivery_Date"] - df["Dispatch_Date"]).dt.days
>>> print(df)
   ShipmentID   Origin Destination  Distance_km Dispatch_Date Delivery_Date Transport_Mode   Cost  Delivery_Time_Days
0         201  Chennai   Bangalore          350    2024-01-01    2024-01-03          Truck  15000                   2
1         202    Delhi      Jaipur          280    2024-01-03    2024-01-05            Air  25000                   2
2         203   Mumbai        Pune          150    2024-01-05    2024-01-06          Truck   8000                   1
3         204  Chennai   Hyderabad          500    2024-01-07    2024-01-10           Ship  20000                   3
4         205    Delhi     Lucknow          420    2024-01-09    2024-01-13            Air  27000                   4
5         206   Mumbai      Nagpur          300    2024-01-11    2024-01-13          Truck  12000                   2
6         207  Chennai  Coimbatore          200    2024-01-13    2024-01-15          Truck   9000                   2
7         208    Delhi        Agra          250    2024-01-15    2024-01-18           Ship  18000                   3

#Identify Late Deliveries
>>> df["Late_Delivery"] = df["Delivery_Time_Days"] > 3
>>> print(df)
   ShipmentID   Origin Destination  Distance_km  ... Transport_Mode   Cost Delivery_Time_Days  Late_Delivery
0         201  Chennai   Bangalore          350  ...          Truck  15000                  2          False
1         202    Delhi      Jaipur          280  ...            Air  25000                  2          False
2         203   Mumbai        Pune          150  ...          Truck   8000                  1          False
3         204  Chennai   Hyderabad          500  ...           Ship  20000                  3          False
4         205    Delhi     Lucknow          420  ...            Air  27000                  4           True
5         206   Mumbai      Nagpur          300  ...          Truck  12000                  2          False
6         207  Chennai  Coimbatore          200  ...          Truck   9000                  2          False
7         208    Delhi        Agra          250  ...           Ship  18000                  3          False

#Basic Exploration
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8 entries, 0 to 7
Data columns (total 10 columns):
 #   Column              Non-Null Count  Dtype
---  ------              --------------  -----
 0   ShipmentID          8 non-null      int64
 1   Origin              8 non-null      object
 2   Destination         8 non-null      object
 3   Distance_km         8 non-null      int64
 4   Dispatch_Date       8 non-null      datetime64[ns]
 5   Delivery_Date       8 non-null      datetime64[ns]
 6   Transport_Mode      8 non-null      object
 7   Cost                8 non-null      int64
 8   Delivery_Time_Days  8 non-null      int64
 9   Late_Delivery       8 non-null      bool
dtypes: bool(1), datetime64[ns](2), int64(4), object(3)
memory usage: 716.0+ bytes
>>> df.describe()
       ShipmentID  Distance_km        Dispatch_Date        Delivery_Date         Cost  Delivery_Time_Days
count     8.00000     8.000000                    8                    8      8.00000            8.000000
mean    204.50000   306.250000  2024-01-08 00:00:00  2024-01-10 09:00:00  16750.00000            2.375000
min     201.00000   150.000000  2024-01-01 00:00:00  2024-01-03 00:00:00   8000.00000            1.000000
25%     202.75000   237.500000  2024-01-04 12:00:00  2024-01-05 18:00:00  11250.00000            2.000000
50%     204.50000   290.000000  2024-01-08 00:00:00  2024-01-11 12:00:00  16500.00000            2.000000
75%     206.25000   367.500000  2024-01-11 12:00:00  2024-01-13 12:00:00  21250.00000            3.000000
max     208.00000   500.000000  2024-01-15 00:00:00  2024-01-18 00:00:00  27000.00000            4.000000
std       2.44949   114.634512                  NaN                  NaN   7045.76874            0.916125

#Average Delivery Time
>>> df["Delivery_Time_Days"].mean()
np.float64(2.375)

#Performance by Transport Mode:
>>> df.groupby("Transport_Mode")["Delivery_Time_Days"].mean()
Transport_Mode
Air      3.00
Ship     3.00
Truck    1.75
Name: Delivery_Time_Days, dtype: float64

#Cost Analysis:
>>> df.groupby("Transport_Mode")["Cost"].mean()
Transport_Mode
Air      26000.0
Ship     19000.0
Truck    11000.0
Name: Cost, dtype: float64

#Late Delivery Percentage:
>>> late_percentage = df["Late_Delivery"].mean() * 100
>>> print(late_percentage)
12.5

#Region (Origin) with Most Shipments:
>>> df["Origin"].value_counts()
Origin
Chennai    3
Delhi      3
Mumbai     2
Name: count, dtype: int64
