import tensorflow as tf

# 0-Dimensional Tensor
zero_d_tensor = tf.ones(shape=())

# 1-Dimensional Tensor
one_d_tensor = tf.ones(shape=(2,))

# 2-Dimensional Tensor
two_d_tensor = tf.ones(shape=(2, 2))

# 3-Dimensional Tensor
three_d_tensor = tf.ones(shape=(2, 2, 2))


#Convert to a np array
three_d_tensor.numpy()

import tensorflow as tf

# Define a 2x3 constant.
const_a = tf.constant(3, shape=[2, 3])

# Define a 2x2 constant.
const_b = tf.constant([1, 2, 3, 4], shape=[2, 2])

