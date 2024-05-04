import tensorflow as tf

# Defining and initializing variables

# Define a floating-point variable
# Variables are mutable tensors that the TensorFlow execution engine
# can automatically differentiate and optimize during machine learning training.
float_variable = tf.Variable([1, 2, 3, 4, 5, 6], dtype=tf.float32)

# Define an integer variable
# Specifying the data type ensures that the numerical precision is maintained
# as needed for the operations that the variable will be involved in.
int_variable = tf.Variable([1, 2, 3, 4, 5, 6], dtype=tf.int16)

# Assume float_variable is a previously defined TensorFlow variable

# Define a constant using tf.constant.
# This creates a constant tensor with the specified value and data type.
constant_b= tf.constant(2, dtype=tf.float32)

# Compute the product of the TensorFlow variable and the constant.
# This will perform element-wise multiplication.

# Using tf.multiply, which is a TensorFlow operation for element-wise multiplication.
product_c0 = tf.multiply(float_variable , constant_b)

# Using the overloaded '*' operator, which is a more pythonic way to perform element-wise multiplication.
product_c1 = float_variable * constant_b

# Both product_c0 and product_c1 will yield the same result.
