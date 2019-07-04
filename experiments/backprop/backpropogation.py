"""
Description: Implementation of backpropagation algorithm in python
Author: bazarovay@github

Partial derivative of cost function with respect to weight/biases
Shows how cost changes with respect to w/b

How changing weight changes the overall behaviour
w^l(jk) : weight for k to j neuron connection. j at lth layer
b^l(j) : bias at layer l for jth neuron
a^l(j) : activation at layer l for jth neuron

activation at layer l is related to activations in l-1

alj=σ(∑kwljkal−1k+blj)

a^l=σ(w^l*a^(l−1)+b^l)

weighted output : w^l*a^(l−1)+b^
we just apply the weight matrix to the activations, then add the bias vector,
and finally apply the σ function*

The goal of backpropagation is to compute the partial derivatives


Assumptions about the cost function in order that backpropagation
can be applied
1. Cost function can be written as average

we need this assumption is because what backpropagation actually lets us do is
compute the partial derivatives ∂Cx/∂w and ∂Cx/∂b for a single training
example. We then recover ∂C/∂w and ∂C/∂b by averaging over training examples

2. C can be written as a function of the outputs from the neural network
Is a function of output activations

Hadamard/Schur product s⊙t where s and t are vectors of the same dim

4 fundamental equations behind backprop


partial detivative C/z is error (compute error)
Backprop will allow us to relate this error to cost change wrt w & bias

4 equations allow computing error and gradient of cost function

error in the output layer
error in the next layer
Rate of change of cost wrt any bias
Rate of change of cost wrt any weight

Input: x
Feedforward: z = w*a + b & a = sigmoid(z^l)
Output error: Change in cost Hadamard Product FeedForward
Back prop error: error =

Reference: http://neuralnetworksanddeeplearning.com
"""
# standard libraries comes first
import json
import random
import sys

# Third-party libraries
import numpy as np


#### Define the quadratic and cross-entropy cost functions

class QuadraticCost(object):

    @staticmethod
    def fn(a, y):
        """Return the cost associated with an output ``a`` and desired output
        ``y``.

        """
        return 0.5*np.linalg.norm(a-y)**2

    @staticmethod
    def delta(z, a, y):
        """Return the error delta from the output layer."""
        return (a-y) * sigmoid_prime(z)


class CrossEntropyCost(object):

    @staticmethod
    def fn(a, y):
        """Return the cost associated with an output ``a`` and desired output
        ``y``.  Note that np.nan_to_num is used to ensure numerical
        stability.  In particular, if both ``a`` and ``y`` have a 1.0
        in the same slot, then the expression (1-y)*np.log(1-a)
        returns nan.  The np.nan_to_num ensures that that is converted
        to the correct value (0.0).

        """
        return np.sum(np.nan_to_num(-y*np.log(a)-(1-y)*np.log(1-a)))

    @staticmethod
    def delta(z, a, y):
        """Return the error delta from the output layer.  Note that the
        parameter ``z`` is not used by the method.  It is included in
        the method's parameters in order to make the interface
        consistent with the delta method for other cost classes.

        """
        return (a-y)

class Network(object):

    def __init__(self, sizes):
        """
        """
        #TODO add doc for  this fnction
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
        self.cost=cost

    def update_mini_batch(self, mini_batch, eta):
        """
        Update weight and bias by applying gradient descent from BP
        mini_batch: list of tuples
        eta: learning rate
        """
        nabla_b = [np.zerors(b.shape) for b in self.biases]
        nabla_w = [np.zerors(w.shape) for w in self.weights]

        for x,y in mini_batch: # input, output
            # partial derivates wrt to b and w respectively
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)

            # tuple of biase/weight and derivative of cost wrt bias/weight
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]


        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]



    def backprop(self, x, y):
        """Return a tuple "(nabla_b, nabla_w)" representing the
        gradient for the cost function C_x.  "nabla_b" and
        "nabla_w" are layer-by-layer lists of numpy arrays, similar
        to "self.biases" and "self.weights"."""

        # 0 matrix
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        # feedforward
        activation = x
        activations = [x] # list to store all the activations, layer by layer

        # aw + b
        zs = [] # list to store all the z vectors, layer by layer


        for b, w in zip(self.biases, self.weights):
            # find actiavation at each layer
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        # backward pass
        delta = self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        # Note that the variable l in the loop below is used a little
        # differently to the notation in Chapter 2 of the book.  Here,
        # l = 1 means the last layer of neurons, l = 2 is the
        # second-last layer, and so on.  It's a renumbering of the
        # scheme in the book, used here to take advantage of the fact
        # that Python can use negative indices in lists.
        for l in xrange(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)


    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        return (output_activations-y)


    def evaluate(self, test_data):
        # Pick the max
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)



    def SGD(self, training_data, epochs, mini_batch_size, eta,
            test_data=None):
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for j in xrange(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in xrange(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print "Epoch {0}: {1} / {2}".format(
                    j, self.evaluate(test_data), n_test)
            else:
                print "Epoch {0} complete".format(j)

# Activation functions
def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

# derivative of sigmoid
def sigmoid_prime(z):
    return sigmoid(z)*(1-sigmoid(z))


if __name__ == "__main__":
    Network(sizes=[1,2,1])
