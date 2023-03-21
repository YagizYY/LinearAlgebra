# %%
import os

# %%
# Reflecting Bear
# Background
# Panda Bear is confused. He is trying to work out how things should look when reflected in a mirror, but is getting the wrong results. In Bear's coordinates, the mirror lies along the first axis. But, as is the way with bears, his coordinate system is not orthonormal: so what he thinks is the direction perpendicular to the mirror isn't actually the direction the mirror reflects in. Help Bear write a code that will do his matrix calculations properly!

# Instructions
# In this assignment you will write a Python function that will produce a transformation matrix for reflecting vectors in an arbitrarily angled mirror.

# Building on the last assingment, where you wrote a code to construct an orthonormal basis that spans a set of input vectors, here you will take a matrix which takes simple form in that basis, and transform it into our starting basis. Recall the from the last video,

# T= E (T_E) (E^-1)

# You will write a function that will construct this matrix. This assessment is not conceptually complicated, but will build and test your ability to express mathematical ideas in code. As such, your final code submission will be relatively short, but you will receive less structure on how to write it.

# Matrices in Python
# For this exercise, we shall make use of the @ operator again. Recall from the last exercise, we used this operator to take the dot product of vectors. In general the operator will combine vectors and/or matrices in the expected linear algebra way, i.e. it will be either the vector dot product, matrix multiplication, or matrix operation on a vector, depending on it's input. For example to calculate the following expressions,

# a = s.t
# s = At
# M = AB

# One would use the code,

# a = s @ t
# s = A @ t
# M = A @ B
# (This is in contrast to the ∗ operator, which performs element-wise multiplication, or multiplication by a scalar.)

# You may need to use some of the following functions:

# inv(A)
# transpose(A)
# gsBasis(A)
# These, respectively, take the inverse of a matrix, give the transpose of a matrix, and produce a matrix of orthonormal column vectors given a general matrix of column vectors - i.e. perform the Gram-Schmidt process. This exercise will require you to combine some of these functions.

# %%
import numpy as np
from numpy.linalg import norm, inv, norm
from numpy import transpose
from readonly.bearNecessities import *

# %%
# In this function, you will return the transformation matrix T,
# having built it out of an orthonormal basis set E that you create from Bear's Basis
# and a transformation matrix in the mirror's coordinates TE.
def build_reflection_matrix(
    bearBasis,
):  # The parameter bearBasis is a 2×2 matrix that is passed to the function.
    # Use the gsBasis function on bearBasis to get the mirror's orthonormal basis.
    E = gsBasis(bearBasis)
    # Write a matrix in component form that performs the mirror's reflection in the mirror's basis.
    # Recall, the mirror operates by negating the last  component of a vector.
    # Replace a,b,c,d with appropriate values
    TE = np.array([[1, 0], [1, -1]])
    # Combine the matrices E and TE to produce your transformation matrix.
    T = E @ TE @ inv(E)
    # Finally, we return the result. There is no need to change this line.
    return T


# %%
c = np.array([[1, 2, 3], [2, 3, 4]])

x = gsBasis(c)

avector = np.array([[1], [2], [3]])
avector.shape

result = c @ avector
print(result)
# %%
