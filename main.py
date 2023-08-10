import numpy as np


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# get dimensions
b = a.ndim

# get shape
b = a.shape

# get type
b = a.dtype

# get size
b = a.itemsize

# get total size
b = a.nbytes

# get a specific element
b = a[0, -2]

# 3-D array
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

c = b[:,1,:]

output = np.ones((5, 5))
z = np.zeros((3,3))
z[1,1] = 9
output[1:4, 1:4] = z
# print(output)

