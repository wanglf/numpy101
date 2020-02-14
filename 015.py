# 15. How to make a python function that handles scalars to work on numpy arrays?
# Q. Convert the function maxx that works on two scalars, to work on two arrays.

import numpy as np

def maxx(x, y):
    if x >= y:
        return x
    else:
        return y

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max = np.vectorize(maxx, otypes=[float])

result = pair_max(a, b)

print(repr(result))