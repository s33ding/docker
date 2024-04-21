import tensorflow as tf

# How to Perform Multiplication in TensorFlow

# Element-wise multiplication is done using tf.multiply operation
# This requires both tensors to have the same shape
# Example of valid element-wise operations:
# tf.multiply([1,2,3], [3,4,5]) or tf.multiply([1,2], [3,4])

# Matrix multiplication is performed with tf.matmul operation
# The number of columns in the first matrix must be equal to the number of rows in the second matrix
# Example of valid matrix multiplication:
# tf.matmul(matrix1, matrix2) where matrix1 columns == matrix2 rows

# Applying the multiplication operators

# Import required functions from TensorFlow
from tensorflow import ones, matmul, multiply

# Define tensors
A0 = ones((1))       # A scalar (though represented as a tensor with one element)
A31 = ones((3, 1))   # A 3x1 matrix
A34 = ones((3, 4))   # A 3x4 matrix
A43 = ones((4, 3))   # A 4x3 matrix

# Exploring valid operations
# Element-wise multiplication is only valid for tensors with the same shape.
# For example, multiply(A31, A31) is valid since both are 3x1 matrices.
# Matrix multiplication with matmul requires compatible dimensions.
# matmul(A43, A34) is valid since A43 is a 4x3 matrix and A34 is a 3x4 matrix,
# fulfilling the requirement for matrix multiplication where the number of columns in the first matrix
# must match the number of rows in the second matrix.
# However, matmul(A43, A43) would not be valid because the shapes do not align for matrix multiplication.

# Examples of valid multiplication operations:
multiply_A0_A0 = multiply(A0, A0)          # Element-wise multiplication of two scalars
multiply_A31_A31 = multiply(A31, A31)      # Element-wise multiplication of two 3x1 matrices
multiply_A34_A34 = multiply(A34, A34)      # Element-wise multiplication of two 3x4 matrices

# Example of valid matrix multiplication operation:
matmul_A43_A34 = matmul(A43, A34)          # Matrix multiplication of a 4x3 matrix with a 3x4 matrix

# Remember that for tf.multiply, both tensors must be of the same shape,
# whereas for tf.matmul, the inner dimensions must align (columns of the first matrix, rows of the second).
