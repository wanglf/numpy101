# 20. How to create a 2D array containing random floats between 5 and 10?
# Q. Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.

import numpy as np

arr = np.arange(9).reshape(3, 3)

# Method 1:
rand_arr = np.random.randint(low=5, high=10, size=(5, 3))+np.random.random((5, 3))
print(repr(rand_arr))

# Method 2:
rand_arr = np.random.uniform(5, 10, size=(5, 3))
print(repr(rand_arr))