import numpy as np

d2_33 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(d2_33 > 5)
print(d2_33[d2_33 > 5])
print(d2_33[:, 2])
print(d2_33[:, 2] > 5)
print(d2_33[:] % 2 == 0)
print(d2_33[d2_33[:] % 2 == 0])