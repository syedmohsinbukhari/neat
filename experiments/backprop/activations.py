"""
description: Activation functions for the network
author: bazarovay@github.com
"""
import numpy as np


def sigmoid(x_in):
    """
    Activation function sigmoid

    input : input tensor

    :return: 1/(1 + e^(-input))
    """
    return 1/(1 + np.exp(-x_in))


def sigmoid_derivative(z):
    """
    Derivative of the sigmoid

    input : input tensor

    :return: 1/(1 + e^(-input))
    """
    return sigmoid(z) * (1 - sigmoid(z))


class Activation:
    """
    get activation methods
    """
    def __init__(self, activation_name):
        _functions = globals()
        self.get = _functions[activation_name]
        self.derive = _functions[activation_name+"_derivative"]

    def get(self, x):
        return self.get(x)

    def derive(self, x):
        return self.derive(x)