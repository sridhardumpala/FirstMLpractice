import tensorflow as tf

x1 = tf.constant(10)
x2 = tf.constant(5)

result = tf.multiply(x1,x2)
print(result)

with tf.Session() as sess:
	output = sess.run(result)
	print(output)

