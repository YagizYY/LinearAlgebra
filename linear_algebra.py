# %%
import os

# %%
import numpy as np
import math

np.set_printoptions(suppress=True)

# %%
A = np.array([[1, 0], [1, 1]])
Ainv = np.linalg.inv(A)

# %%
ßA = [[4, 6, 2], [3, 4, 1], [2, 8, 13]]

s = [9, 7, 2]

r = np.linalg.solve(A, s)
print(A)
# %%
# matrix multiplication

matrix1 = np.array([[3, 1], [1, 1]])
matrix2 = np.array([1, 0])

print(matrix1 @ matrix2)

# %% [markdown]
# Eigenvalues
M = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
vals, vecs = np.linalg.eig(M)
vals

# %%
# Eigenvectors - Note, the eigenvectors are the columns of the output.
M = np.array([[3 / 2, -1], [-1 / 2, 1 / 2]])
vals, vecs = np.linalg.eig(M)
vecs
