# 24. How to print the full numpy array without truncating?
# Q. Print the full numpy array a without truncating.

import numpy as np
import sys

a = np.arange(1000)
np.set_printoptions(threshold=6)
print(repr(a))

np.set_printoptions(threshold=sys.maxsize)
print(repr(a))


