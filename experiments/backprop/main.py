import numpy as np
# from .losses import Quadratic


class Layer:

    def __init__(self, number_of_neuron, is_input=False):
        self.neurons = number_of_neuron
        self.input = is_input


class Network:

    def __init__(self):
        """
        create layers and bias
        """
        self.layers = [Layer(2, is_input=True), Layer(3), Layer(1)]
        self.biases = [np.random.randn(y.neurons, 1) for y in self.layers if not y.input]
        # connection Nkj
        # weights => k by j matrix
        self.weights = [np.random.randn(k.neurons, j.neurons)
                        for j, k in zip(self.layers[:-1], self.layers[1:])]

        self.activation_list = []

        self.inputs = []

    def set_input(self, input):
        self.inputs = input

    def feed_forward(self, activation):
        """
        Feed forward go over all layers
        Args:
            activation: activation of the previous layer

        Returns:
            sigmoid(x*w + b)
        """
        for weight, bias in zip(self.weights, self.biases):
            activation = sigmoid(np.dot(weight, activation) + bias)
            self.activation_list.append(activation)
        return activation

    def cost_function(self):
        """

        Returns:

        """
        pass

    def backprogagation(self, x):
        """
        Backpropagate the error
        . feed forward [done]
        . Calculate output error [done]
        . Backpropagate the error
        . Ourput/Calc

        :return:
        """
        final_output = self.feed_forward(x)
        # output error: cost_function_derivative * change in final activation

        cost_delta = derivative(np.array([[1]]), final_output)
        output_error = cost_delta * sigmoid_derivative(self.activation_list[-1])

        delta_error = output_error

        for i in range(len(self.weights), 0, -1): # going from last to the first layer
            delta_error = np.dot(self.weights[i - 1].transpose(), delta_error) * sigmoid_derivative(self.activation_list[i - 2])
            print(delta_error)

    def sgd(self, batch_data, epochs, learning_rate):
        """
        - Select a minibatch from the data
        - Use a learning rate
        - Calculate gradient descent
        - x - delta*delta_x
        Returns:

        """
        # for _ in range(epochs):


def derivative(predicted, output):
    """
    Derivative of the quadratic cost
    predicted - output
    :return:
    """
    return np.subtract(predicted, output)


def sigmoid(x):
    """
    Sigmoid activation function
    1/(1 + e^(-x))
    Args:
        x:

    Returns:
    """
    return 1/(1 + np.exp(-x))


def sigmoid_derivative(z):
    """
    Returns the derivative of sigmoid
    :param z:
    :return:
    """
    return sigmoid(z)*(1 - sigmoid(z))

"""
Network:
1. set layers, random weight, biases
2. set input [done]
3. feed forward [done]
4. Calculate output error [done]
5. Backpropagate the error
6. Ourput/Calc

7. Optimize = use gradient and learning rate | w - eta * grad
"""
input_data = [[[1], [1]],[[1], [1]]]
output_data = [[1]]
net = Network()

single_inp = np.array(input_data[0])

net.backprogagation(single_inp)
# net.set_input(input_data)
# predicted_out = net.feed_forward(single_inp)
# output error -> deltaC * deltaActivation
# derivate for a quadratic cost function => (predicted - actual)
# sigma_prime(last activation)
# cost_delta = np.subtract(predicted_out, output_data)
# output_error = cost_delta * sigmoid_derivative(net.activation_list[-1])
# print(output_error)
# Now backprogogate the error
# value for each weight
# error = weight_plus_l(transpose) * error_plus_1 (hadmard) sigma_derivative_of_z_of_l

# delta_error = output_error
# for i in range(len(net.weights), 0, -1):
#     delta_error = np.dot(net.weights[i - 1].transpose(), delta_error) * sigmoid_derivative(net.activation_list[i - 2])
#     print("Output error in layer {} : input neurons {}, {}".format((i - 1), net.weights[i - 1].shape[1], delta_error))
