import tensorflow as tf

# Define 0-dimensionanl tensors
A0 = constant([1])
B0 = constant([2])

# Define 1-dimensionanl tensors
A1 = constant([1,2])
B1 = constant([3,4])

# Define 2-dimensionanl tensors
A2 = constant([1,2],[3,4])
B2 = constant([5,6],[7,8])

# Define 2-dimensionanl tensors
A2 = constant([1,2],[3,4])
B2 = constant([5,6],[7,8])

C0 = add(A0, B0)
C1 = add(A1, B1)
C3 = add(A3, B3)

import tensorflow as tf

# Performing Tensor Addition with TensorFlow
# TensorFlow provides the tf.add operation for element-wise tensor addition.
# This operation is intuitive and follows the standard arithmetic addition rules:

# Element-wise addition requires both tensors to have the same shape.

# Scalar addition example:
# Simple addition of two scalars.
scalar_a = tf.constant(1)
scalar_b = tf.constant(2)
scalar_result = tf.add(scalar_a, scalar_b)  # Result is a scalar: 3

# Vector addition example:
# Adding two 1-dimensional tensors (vectors) of the same length.
vector_a = tf.constant([1, 2])
vector_b = tf.constant([3, 4])
vector_result = tf.add(vector_a, vector_b)  # Result is a vector: [4, 6]

# Matrix addition example:
# Adding two 2-dimensional tensors (matrices) of the same dimensions.
matrix_a = tf.constant([[1, 2], [3, 4]])
matrix_b = tf.constant([[5, 6], [7, 8]])
matrix_result = tf.add(matrix_a, matrix_b)  # Result is a matrix: [[6, 8], [10, 12]]

# The add() operator is overloaded in TensorFlow, which means that
# you can also use the '+' symbol to perform element-wise addition.
# For example, matrix_result can also be computed as follows:
matrix_result_overloaded = matrix_a + matrix_b  # Equivalent to tf.add(matrix_a, matrix_b)

# Now matrix_result and matrix_result_overloaded contain the same values.
# It's important to ensure that tensors in the addition operation are of the same shape
# to avoid shape-related errors.
