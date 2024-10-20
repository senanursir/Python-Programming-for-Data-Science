# ILOC - LOC

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# iloc: integer based selection:
df.iloc[0:3]  # 0, 1, 2. indexes
df.iloc[0, 0] # first column, first row : 0


# loc: label based selection:
df.loc[0:3]  # 0, 1, 2, 3. indexes

df.iloc[0:3, "age"]   # erroe: index wanted.
df.iloc[0:3, 0:3]    # 3 variable selected.

df.loc[0:3, "age"]   # 3 index value of "age" variable.

#
col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]




