# 5. How to replace items that satisfy a condition with another value in numpy array?
# Q. Replace all odd numbers in arr with -1

import numpy as np

arr = np.arange(10)
arr[arr % 2 == 1] = -1

print(repr(arr))