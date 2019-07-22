import numpy as np

from activations import Activation
from losses import MSE
from optimizers import SGD


class Layer:

    def __init__(self, number_of_neuron, is_input=False):
        self.neurons = number_of_neuron
        self.input = is_input


class Network:

    def __init__(self, activation=None):
        """
        create layers and bias
        """
        self.layers = [Layer(2, is_input=True), Layer(3), Layer(1)]
        self.biases = [np.random.randn(y.neurons, 1) for y in self.layers if not y.input]
        # connection Nkj
        # weights => k by j matrix
        self.weights = [np.random.randn(k.neurons, j.neurons)
                        for j, k in zip(self.layers[:-1], self.layers[1:])]

        self.activation_fn = Activation(activation)
        self.loss_fn = MSE()
        self.optimizer_fn = SGD(lr=.01)

        self.activation_list = []
        self.inputs = []

        self.zs = []
        self.loss_list = []


    def set_activation(self, activation):
        """
        Sets activation fn for the model

        :param activation: name of the activation function
        """
        self.activation_fn = Activation(activation)

    def feed_forward(self, activation):
        """
        Feed forward go over all layers
        Args:
            activation: activation of the previous layer

        Returns:
            activation value
        """
        for weight, bias in zip(self.weights, self.biases):
            z = np.dot(weight, activation) + bias
            self.zs.append(z)
            activation = self.activation_fn.get(z)
            self.activation_list.append(activation)
        return activation

    def gradient_descent(self, input, output):
        """
        Calculate the gradient descent
        - Get weight + bias versus cost derivative
        - Use the value to update the weights

        :return:
        """
        # x = [[1], [1]]
        delta_b, delta_w = self.backprogagation(input, output)


        self.weights, self.biases = self.optimizer_fn.get_gradient(self.weights, delta_w, self.biases, delta_b)
        # print(self.weights, self.biases)


    def backprogagation(self, x, output):
        """
        Backpropagate the error
        . feed forward [done]
        . Calculate output error [done]
        . Backpropagate the error
        . Ourput/Calc

        :return:
        """
        # output = np.array([[1]])
        pred_output = self.feed_forward(x)
        # output error: cost_function_derivative * change in final activation

        loss_val = self.loss_fn.calculate(pred_output, output)
        # print(loss_val)
        self.loss_list.append(loss_val)

        delta_c_output = self.loss_fn.derivative(pred_output, output)

        # calculating error on the last layer
        output_error = delta_c_output * self.activation_fn.derivative(self.zs[-1])

        delta_error = output_error

        delta_cw_list = [np.dot(delta_error, self.activation_list[-1].transpose())]
        delta_b_list = [delta_error]

        # Calculate error for each layer
        for i in range(len(self.weights), 0, -1): # going from last to the first layer
            # print(i - 1)
            delta_error = np.dot(self.weights[i - 1].transpose(), delta_error) * sigmoid_derivative(self.zs[i - 2])

            delta_c_w = np.dot(delta_error,  self.activation_list[i - 1].transpose())
            # print(delta_c_w)
            delta_bw = delta_error

            delta_cw_list.append(delta_c_w)
            delta_b_list.append(delta_bw)

        # delta_c_w = activaction * error
        # delta_c_b = error
        return delta_b_list, delta_cw_list


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
output_data = [[1]]
net = Network(activation="sigmoid")


input = [ [[1], [1]] ,   [[1], [2]] ]
output = [ [[2]] , [[3]] ]
for i in range(len(output)):
    net.gradient_descent(input[i], output[i])

loss_rate = net.loss_list
print("-------------------------------")

for i in loss_rate:
    print(i)
    print("....")

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
