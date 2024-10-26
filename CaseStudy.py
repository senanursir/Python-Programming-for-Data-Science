import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()

# mission 1:
["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

# mission 2:
[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

og_list = ['abbrev', "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df

# mission 3:

df = sns.load_dataset("Titanic")
df.head()
df.shape

# mission 4:

df["sex"].value_counts() # male: 577, female: 314

# mission 5:
df.nunique()

# mission 6:
df[["pclass", "parch"]].nunique()

# mission 7:
df["embarked"].dtype

# mission 8:
df["embarked"] = df["embarked"].astype("category")
#
df[df["embarked"] == "C"].head(10)

#
df[df["embarked"] != "S"].head(10)

df[(df["age"] < 30) & (df["sex"] == "female")].head()