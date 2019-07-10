"""
Description: Numpy implementation of activation functions and
             and their derivatives
author: syedmohsinbukhari@googlemail.com

Reference
http://neuralnetworksanddeeplearning.com/chap2.html
"""

from numpy import exp


class ActivationFunction:

    def __init__(self):
        pass

    @staticmethod
    def forward(x):
        pass

    @staticmethod
    def derivative(x):
        pass


class Sigmoid(ActivationFunction):

    @staticmethod
    def forward(x):
        return 1.0 / (1.0 + exp(-1.0*x))

    @staticmethod
    def derivative(x):
        return Sigmoid.forward(x) * (1.0 - Sigmoid.forward(x))


class Relu(ActivationFunction):

    @staticmethod
    def forward(x):
        if x > 0.0:
            return x
        else:
            return 0.0

    @staticmethod
    def derivative(x):
        if x > 0.0:
            return 1.0
        else:
            return 0.0

