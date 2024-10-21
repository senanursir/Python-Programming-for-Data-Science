# AGGREGATION & GROUPING

# aggregation -> max,min,mean,median vs...
# grouping -> process of categorizing a dataset based on a specific thing.

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean()

df.groupby("sex")["age"].mean()

# age variable's mean grouped by sex:
df.groupby("sex").agg({"age": "mean"})


# age variable's mean and sum grouped by sex:
df.groupby("sex").agg({"age": ["mean", sum]})


# 2 variable grouped:
df.groupby("sex").agg({"age": ["mean", sum],      # embark counting could not be performed properly
                      "embark_town": "count"})    # because the embark contained string.


df.groupby("sex").agg({"age": ["mean", sum],
                      "survived": "mean"})      # worked better with numeric variable.


# grouped by 2 variable:
df.groupby(["sex", "embark_town"]).agg({"age": ["mean", sum],
                                        "survived": "mean"})


df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean", sum],
                                                 "survived": "mean"})


df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean", sum],
    "survived": "mean",
    "sex": "count"})
