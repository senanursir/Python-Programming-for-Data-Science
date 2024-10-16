
# Pandas Series:

# It has index information.
import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
print(type(s))
print(s.index)
print(s.dtype)
print(s.size)
print(s.ndim)
print(s.values) # numpy array
print(s.head(3))  # first 3 index
print(s.tail(3))  # last three index


# data reading:
df = pd.read_csv("datasets/Advertising.csv")
print(df)
print(df.head)


# QUICK LOOK AT DATA

import seaborn as sns

df = sns.load_dataset("titanic")
print(df.head())
print(df.tail())
print(df.info()) # RangeIndex: 891 entries, 0 to 890
print(df.shape) # (891, 15): row,column
print(df.info)  # includes some summary infos: dtypes: bool(2), category(2), float64(2), int64(4), object(5)
print(df.columns) # all variables
print(df.index) # RangeIndex(start=0, stop=891, step=1)
df.describe().T  # A quick look at the variables of our dataset in an analytical way.
print(df.isnull().values.any()) # do we have any null data: True
print(df.isnull().sum())  # how many null data
print(df["sex"].head())   # displays the datas of the column.
print(df["sex"].value_counts())
