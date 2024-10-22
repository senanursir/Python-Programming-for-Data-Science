import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex", "embarked")
# values, row, column.
# The intersection was predefined as averaged.


# According to standart deviation:
df.pivot_table("survived", "sex", "embarked", aggfunc="std")

# w 2 columns:
df.pivot_table("survived", "sex", ["embarked", "class"])

# w 2 rows, 2 columns:
# df.pivot_table("survived", ["sex", "#--"], ["embarked", "class"])

# since the age variable is numeric, a breakdown cannot be provided:
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

# categorized by age(0 to 10, 10 to 18 vs)
df.pivot_table("survived", "sex", "new_age")

#
df.pivot_table("survived", "new_age", "embarked")

#
df.pivot_table("survived", "sex", ["new_age", "class"])

# çıktının güzel gözükmesi için:
pd.set_option('display.width', 500)
