import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.index  # RangeIndex(start=0, stop=891, step=1)
df[0:13]
df.drop(0, axis=0).head()  # 0.index has gone.

delete_indexes = [1, 3, 5, 7]    # these indexes are gone
df.drop(delete_indexes, axis=0).head(10)

# for making permanent
# df = df.drop(delete_indexes, axis=0)
# df.drop(delete_indexes, axis=0, inplace=True)


# CONVERTING VARIABLE TO INDEX

df["age"].head()  # variable selection
df.age.head()

df.index     # RangeIndex(start=0, stop=891, step=1)
df.index = df["age"]

df.drop("age", axis=1).head()

df.drop("age", axis=1, inplace=True)
df.head()

# CONVERTİNG VARIABLE TO INDEX

df.index
df["age"] = df.index  # If the entered expression does not exist in the dataframe, it means a new variable entry.
df.head()   # df variable has added.
df.drop("age", axis=1, inplace=True)

# 2. way:
# The value in the index was deleted and added as a column:
df = (df.reset_index())
df.head()





