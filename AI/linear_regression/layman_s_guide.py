'''
Sumber: https://medium.com/@derekchia/a-line-by-line-laymans-guide-to-linear-regression-using-tensorflow-3c0392aa9e1f

Linear Regression using Tensorflow

Belum semua dimodifikasi
'''

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def generate_dataset():
    '''
    Generating dataset namely x and y.
    It generates 100 points with value between 0 to 2, spreaded evenly.
    It also

    :return:
    '''
    x_batch = np.linspace(0, 2, 100)
    y_batch = 1.5 * x_batch * np.random.randn(*x_batch.shape) * 0.2 + 0.5
    return x_batch, y_batch


def linear_regression():
    '''
    formula: y = Wx + b

    some addition notes:
    1. tf.Variable() = variable maintains state in the graph across calls to run(). The type and shape of it are fixed
    but the value can be changed through assign method
    2. tf.placeholder = just a placeholder that will be replaced. It allows us to create our operations and build our computation graph without needing the data. It's more like static programming in java
    :return:
    '''
    x = tf.placeholder(tf.float32, shape=(None,), name='x')
    y = tf.placeholder(tf.float32, shape=(None,), name='y')

    with tf.variable_scope('lreg') as scope:
        w = tf.Variable(np.random.normal(), name='w')
        b = tf.Variable(np.random.normal(), name='b')

        y_pred = tf.add(tf.multiply(w, x), b)

        loss = tf.reduce_mean(tf.square(y_pred - y))
    return x, y, y_pred, loss


def run(epoch=30):
    x_batch, y_batch = generate_dataset()
    x, y, y_pred, loss = linear_regression()

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train_op = optimizer.minimize(loss)

    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        feed_dict = {x: x_batch, y: y_batch}

        for i in range(epoch):
            session.run(train_op, feed_dict)
            print(i, 'loss:', loss.eval(feed_dict))

        print('Predicting')

        y_pred_batch = session.run(y_pred, {x: x_batch, })

    plt.scatter(x_batch, y_batch)
    plt.plot(x_batch, y_pred_batch, color='red', )
    plt.xlim(0, 2)
    plt.ylim(0, 2)
    plt.savefig('plot.png')

if __name__ == '__main__':
    run()
