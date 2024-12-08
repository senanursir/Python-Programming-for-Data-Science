# OVERVİEW
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()

# Gives an overview of the data:
def check_df(dataframe, head=5):
       print("#######SHAPE############")
       print(dataframe.shape)
       print("#######TYPES############")
       print(dataframe.dtypes)
       print("#######HEAD############")
       print(dataframe.head(head))
       print("#######NA############")
       print(dataframe.isnull().sum())
       print("#######TAIL############")
       print(dataframe.tail(head))
       print("#######QUANTILES############")
       print(dataframe.describe([0, 0.05, 0.50, 0.95, 1]).T)



check_df(df)
print(df.columns)
# CATEGORICAL VARIABLE ANALYSIS:

df["embarked"].value_counts()
df["sex"].unique()
df["class"].nunique()
df["survived"].value_counts()  # actually a categorical variable.

# catching the variables depends on it's datatype.
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"] ]
print(cat_cols)
# str(df["sex"].dtypes)in ["object"]  # True

# catching the variables that are actually categorical but seems numerical:
# catch if the uniqe class number less than 10:
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
print(num_but_cat)

# catching the variables that are actually numerical but seems categorical:
# there are too many classes to define.
# high cardinal categorical columns.
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
print(cat_but_car)  # there is none.

# all the categorical variables in the same list:
cat_cols = cat_but_car + num_but_cat

# deleting the high kardinal variables.
cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols]

df[cat_cols].nunique()

# variables that not in cat_cols :
[col for col in df.columns if col not in cat_cols]

######

df["survived"].value_counts() # frequency info.
100 * df["survived"].value_counts() / len(df) # percentage information of the revelant dataframe.

# it calculates the frequencies and percentage ratios of the values in a categorical column,
# and presents them in an easily analyzable table format:
def cat_summary(dataframe, col_name):
       print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                           "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
       print("##############################")

cat_summary(df, "sex")

# all the categorical variabels on dataset showed categorically.
for col in cat_cols:
       cat_summary(df, col)
















