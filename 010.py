# 10. How to generate custom sequences in numpy without hardcoding?
# Q. Create the following pattern without hardcoding. Use only numpy functions and the below input array a.

# a = np.array([1, 2, 3])
# output = array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

import numpy as np

a = np.array([1, 2, 3])

output = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(repr(output))