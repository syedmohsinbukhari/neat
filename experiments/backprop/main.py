import numpy as np


class Layer:

    def __init__(self, number_of_neuron, is_input=False):
        self.neurons = number_of_neuron
        self.input = is_input


class Network:

    def __init__(self):
        """
        create layers and bias
        """
        self.layers = [Layer(2, is_input=True), Layer(2), Layer(1), Layer(1)]
        self.biases = [np.random.randn(y.neurons, 1) for y in layers if not y.input]
        self.weights = [(y.neurons, x.neurons) for x, y in zip(layers[:-1], layers[1:])]

    def feed_forward(self, input):
        """
        Feed forward go over all layers
        Args:
            a: activation of the previous layer

        Returns:
            sigmoid(x*w + b)
        """
        for weight, bias in zip(self.weights, self.biases):
            inputs = sigmoid(np.dot(weight, input) + bias)

        return inputs

    def cost_function(self):
        """

        Returns:

        """
        pass

    def sgd(self, batch_data, epochs, learning_rate):
        """
        - Select a minibatch from the data
        - Use a learning rate
        - Calculate gradient descent
        - x - delta*delta_x
        Returns:

        """
        for _ in range(epochs):

def sigmoid(x):
    """
    Sigmoid activation function
    1/(1 + e^(-x))
    Args:
        x:

    Returns:
    """
    return 1/(1 + np.exp(-x))



