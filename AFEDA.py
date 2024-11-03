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

df = sns.load_dataset("flights")
check_df(df)

# CATEGORICAL VARIABLE ANALYSIS
df["embarked"].value_counts()
df["sex"].unique()
df["sex"].nunique()
df["embarked"].nunique()
df.info()

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]



