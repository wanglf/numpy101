# 21. How to print only 3 decimal places in python numpy array?
# Q. Print or show lonly 3 decimal places of the numpy array rand_arr

import numpy as np

rand_arr = np.random.random([5, 3])
print(repr(rand_arr))

np.set_printoptions(precision=3)
print(repr(rand_arr[:4]))