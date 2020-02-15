# 16. How to swap two columns in a 2d numpy array?
# Q. Swap column 1 and 2 in the array arr.

import numpy as np

arr = np.arange(9).reshape(3, 3)

print(repr(arr))

arr = arr[:,[1, 0, 2]]

print(repr(arr))