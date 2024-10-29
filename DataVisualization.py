# DATA VISUALİZATION: MATPLOTLIB & SEABORN

# MATPLOTLIB:

# Categorical Variable: column chart. countplot (seaborn), bar(matplotlib)
# Numerical Variable: hist, boxplot


# CATEGORICAL VARIABLE VISUALIZATION:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind='bar')
plt.show(block=True)


# NUMERICAL VARIABLE VISUALIZATION:
# hist:
plt.hist(df["age"])
plt.show(block=True)

# boxplot:
plt.boxplot(df["fare"])
plt.show(block=True)




