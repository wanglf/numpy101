# 8. How to stack two arrays vertically?
# Stack arrays a and b vertically.

import numpy as np

a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

output1 = np.concatenate([a, b], axis=0)
output2 = np.vstack([a, b])
output3 = np.r_[a, b]


print(repr(output1))
print(repr(output2))
print(repr(output3))