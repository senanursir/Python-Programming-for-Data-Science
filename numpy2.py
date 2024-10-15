# FANCY INDEX

import numpy as np

v = np.arange(0, 30, 3)  # 0 to 30, 3 by 3
# [ 0  3  6  9 12 15 18 21 24 27]
print(v[1]) # 3
print(v[4]) # 12

catch = [1, 2, 3] # index list
print(v[catch]) # [3 6 9]


# CONDITIONS ON NUMPY

v = np.array([1, 2, 3, 4, 5])

# we pick v < 3
print(v[v < 3])   # [1 2]
print(v[v != 3])  # [1 2 4 5]


# MATHEMATICAL OPERATIONS

v = np.array([1, 2, 3, 4, 5])

# We want to divide all elements by 5:

print(v / 5)  # w float: [0.2 0.4 0.6 0.8 1. ]
print(v * 5 / 10) # [0.5 1.  1.5 2.  2.5]
print(v ** 2)     # [ 1  4  9 16 25]

#

print(np.subtract(v, 1))   # [0 1 2 3 4]
print(np.add(v, 1))     # [2 3 4 5 6]
print(np.mean(v))       # 3.0
print(np.sum(v))        # 15
print(np.min(v))        # 1
print(np.max(v))       # 5
print(np.var(v))       #
# This is not a permanent change.


# Solution of a two-variable equation:
# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])   # Coefficients of the first and second variables.
b = np.array([12, 10])    # Results
solution = np.linalg.solve(a, b)
print(solution)    # [1.85714286 2.71428571]





