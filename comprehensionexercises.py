# Renaming Variable Names in a Dataset

# Before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# After:
# ['total' 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

# without comprehensions:
# df is a dataframe

import seaborn as sns
df = sns.load_dataset("car_crashes")

A = []
for col in df.columns:  #
    A.append(col.upper())

df.columns = A
print(df.columns)


# with comprehensions:
# we have permanently saved the new version of the dataset:

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]
print(df.columns)

# ---------------------
# isminde "INS" olan degiskenlerin basina FLAG digerlerine NO_FLAG eklemek istiyoruz.

print([col for col in df.columns if "INS" in col])

print(["FLAG_" + col for col in df.columns if "INS" in col])   # col is a string

print(["FLAG_" + col if "INS" in col else "NO_FLAG" + col for col in df.columns])
# ['NO_FLAGTOTAL', 'NO_FLAGSPEEDING', 'NO_FLAGALCOHOL', 'NO_FLAGNOT_DISTRACTED',
# 'NO_FLAGNO_PREVIOUS', 'FLAG_INS_PREMIUM', 'FLAG_INS_LOSSES', 'NO_FLAGABBREV']

#--------------------------------------------------------------------------------


# THE OUTPUT:
# {'total': ['mean', 'min', 'max', 'sum'],
# 'speeding': ['mean', 'min', 'max', 'sum'],
# 'alcohol': ['mean', 'min', 'max', 'sum'],
# 'not_distracted': ['mean', 'min', 'max', 'sum'],
# 'no_previous': ['mean', 'min', 'max', 'sum'],
# 'ins_premium': ['mean', 'min', 'max', 'sum'],
# 'ins_losses': ['mean', 'min', 'max', 'sum']}

import seaborn as sns
df = sns.load_dataset("car_crashes")

# We are selecting the numerical ones:
num_cols = [col for col in df.columns if df[col].dtype != "O"]  # those are not objects.

dict1 = {}
agg_list = ['mean', 'min', 'max', 'sum']
for col in num_cols:
    dict1[col] = agg_list

print(dict1)

# short way:
print({col:agg_list for col in num_cols})

# Keep col constant, place agg_list next to it.






