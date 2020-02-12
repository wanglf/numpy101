# 3. How to create a boolean array?
# Q. Create a 3x3 numpy array of all True's

import numpy as np

arr = np.full((3, 3), True, dtype=bool)
print(repr(arr))