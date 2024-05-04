import tensorflow as tf

#ex1
gray = tf.random.uniform([2,2], maxval=255, dtype="int32")
gray_reshaped = tf.reshape(gray, [2*2,1])


#ex2
color = tf.random.uniform([2,2,3], maxval=255, dtype="int32")
color_reshaped = tf.reshape(color, [2*2,3])
