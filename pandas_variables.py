# OPERATIONS ON VARIABLES:

import pandas as pd
import seaborn as sns

# df = sns.load_dataset("titanic")
# df.head()
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

"age" in df   # True

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head())    # pandas.core.series.Series


# when we want to remain as a dataframe:
df[["age"]].head()
type(df[["age"]].head())    # pandas.core.frame.DataFrame.

# multiple selections:
df[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df[col_names]    # multiple selection w list


# new variable added as 'age ** 2'
df["age2"] = df["age"]**2   # if entered value is not exist; it is added as a new variable.
df.head()

# age3 is added:
df["age3"] = df["age"] / df["age2"]
df.head()

# delete(not permanent):
df.drop("age3", axis=1).head()

# multiple delete (not permanent):
df.drop(col_names, axis=1).head()

# it selected variables that contained the expression of age:
df.loc[:, df.columns.str.contains("age")].head()

# except(delete that contained "age")
df.loc[:, ~df.columns.str.contains("age")].head()
