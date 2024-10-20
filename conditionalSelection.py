# CONDITIONAL SELECTION

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()   # people who older than 50.
df[df["age"] > 50]["age"].count()   # 64 people are older than 50: based "age" variable.

df.loc[df["age"] > 50, "class"].head()    # Class information of persons over the age of 50.
df.loc[df["age"] > 50, ["age", "class"]].head() # 2 columns together.

# more than 1 condition:
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class", "sex"]].head()

df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & (df["embark_town"] == "Cherbourg"),
       ["age", "class", "embark_town"]].head()

#

df["embark_town"].value_counts()  # 3 classes.

df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]].head()

df_new["embark_town"].value_counts()  # 2 classes are selected.

