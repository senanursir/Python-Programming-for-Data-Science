# NUMPY

import numpy as np

# The two lists were converted into numpy arrays:
a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])
print(a * b)     # [ 1  4  9 16]


print(type(np.array([1, 2, 3, 4, 5])))
print(np.zeros(10, dtype=int))     # [0 0 0 0 0 0 0 0 0 0]
print(np.random.randint(0, 10, size=5))  # [2 5 6 7 5]
print(np.random.normal(10, 4, (3, 4)))


# ndim: number of dimensions
# shape: shape information (dimensions)
# size: total number of elements
# dtype: array data type

a = np.random.randint(10, size=5)
print(a) # [6 3 6 6 4]
print(a.ndim) # 1
print(a.shape) # (5,)
print(a.size)  # 5
print(a.dtype) # int64


# Reshaping:
# print(np.random.randint(1, 10, size=9))  # [1 6 4 2 4 2 6 2 3]
print(np.random.randint(1, 10, size=9).reshape(3, 3))            # 3 dimensions.


# Index operations:

a = np.random.randint(10, size=10)
a[0]
# slicing:
a[0:5]  # second border is not included.
a[0] = 999 # 0. index has changed.

#

m = np.random.randint(10, size=(3, 5))     # 3 satır, 5 sütunlu array.
print(m)
print(m[0, 0])    # 7
print(m[1, 1])    # 4
print(m[2, 3])    # 9
