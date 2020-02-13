# 9. How to stack two arrays horizontally?
# Q. stack the arrays a and b horizontally.

import numpy as np

a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

output1 = np.concatenate((a, b), axis=1)
output2 = np.hstack([a, b])
output3 = np.c_[a, b]

print(repr(output1))
print(repr(output2))
print(repr(output3))