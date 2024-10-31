# DATA VISUALİZATION: MATPLOTLIB & SEABORN

# MATPLOTLIB:

# Categorical Variable: column chart. countplot (seaborn), bar(matplotlib)
# Numerical Variable: hist, boxplot


# CATEGORICAL VARIABLE VISUALIZATION:
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

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


# MATPLOTLIB FEATURES:

# plot:
x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y, 'o')
plt.show(block=True)

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y, 'o')
plt.show(block=True)


# marker:
z = np.array([13, 28, 11, 100])

plt.plot(z, marker='o')
plt.show(block=True)

plt.plot(z, marker='*')
plt.show(block=True)
# markers = ['o', '*', '.', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']


# line:
s = np.array([13, 28, 11, 100])
plt.plot(s)
plt.show(block=True)

plt.plot(s, linestyle='dotted', color="r")   # dashed, dotted, dashdot
plt.show(block=True)


# multiple lines:

x = np.array([23, 18, 31, 10])
y = np.array([13, 38, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show(block=True)

# LABELS:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.show()

# title:
plt.title("MAIN TITLE")
plt.show()
# title for x
plt.xlabel("Title of x")

# title for y
plt.ylabel("Title of y")

plt.grid()
plt.show()

# Subplots :

# plot1:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)      # 1st chart of 1 row,2 column
plt.title("1")
plt.plot(x, y)

# plot2:

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 2)      # 2nd chart of 1 row,2 column chart.
plt.title("2")
plt.plot(x, y)

# Solution to the graph visibility issue:

# import matplotlib
# matplotlib.use("Qt5Agg")
# from matplotlib import pyplot as plt
