import numpy as np
import tensorflow as tf

#Declare list of feautures, we only have one real0valued feature
def model(feautures, labels, mode):
    #Build a linear model adn predict values
    W = tf.get_variable("W", [1], dtype=tf.float64)
    b = tf.get_variable("b", [1], dtype=tf.float64)
    y = W *feautures['x'] + b

    #LOss sub graph
    loss = tf.reduce_sum(tf.square(y-labels))

    #Training sub-graph
    global_step = tf.train.get_global_step()
    optimizer =tf.train.GradientDescentOptimizer(0.01)
    train = tf.group(optimizer.minimize(loss),
                     tf.assign_add(global_step, 1))
    #ModelFnops connects subgraphs we built to the
    # appropriate functionality
    return tf.contrib.learn.ModelFnOps(
        mode=mode, predictions= y,
        loss = loss, train_op=train)


estimator = tf.contrib.learn.Estimator(model_fn=model)
#define our dataset
x = np.array([1., 2., 3., 4.])
y = np.array([0., -1., -2., -3.])

input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x}, y, 4, num_epochs= 1000)

#train
estimator.fit(input_fn =input_fn, steps = 1000)

#evaluate
print(estimator.evaluate(input_fn= input_fn, steps= 10))

    
