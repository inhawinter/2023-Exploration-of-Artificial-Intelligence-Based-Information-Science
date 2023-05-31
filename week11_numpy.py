import numpy as np

# v = np.array([90, 70.0, "BTS", 80])
# v = np.array([90, 70.0, 80])
v = np.array([90, 70, 80])
m = np.array([[3, 2, 1], [7, 8, 9], [10, 12, 11]])
print(v, m)
print(v.ndim, m.ndim)
print(v.shape, m.shape)
print(v.dtype, m.dtype)
print(v.itemsize, m.itemsize)
print(v.nbytes, m.nbytes)
print(v.strides, m.strides)
