import tensorflow as tf

# tf.constant: Creates a constant tensor from a list of values.
# Useful for creating tensors with specific values that you want to use as constants.
tensor_a = tf.constant([1, 2, 3])  # Example: Creates a 1D tensor with values [1, 2, 3]

# tf.zeros: Generates a tensor filled with zeros.
# Commonly used for initializing weights in a model to zero.
tensor_b = tf.zeros([2, 2])  # Example: Creates a 2x2 tensor filled with zeros

# tf.zeros_like: Creates a tensor with all elements set to zero.
# Useful when you need a zero tensor with the same shape as another tensor.
tensor_c = tf.zeros_like(input_tensor)  # Assumes 'input_tensor' is a previously defined tensor

# tf.ones: Generates a tensor filled with ones.
# Commonly used for initializing tensors for certain algorithms that need a starting value of 1.
tensor_d = tf.ones([2, 2])  # Example: Creates a 2x2 tensor filled with ones

# tf.ones_like: Creates a tensor with all elements set to one.
# Useful for creating a tensor with the same shape as another tensor, but with all ones.
tensor_e = tf.ones_like(input_tensor)  # Assumes 'input_tensor' is a previously defined tensor

# tf.fill: Fills a tensor with a scalar value.
# Handy when you need to create a tensor with a specific size and fill it with a specific value.
tensor_f = tf.fill([3, 3], 7)  # Example: Creates a 3x3 tensor filled with the value 7

