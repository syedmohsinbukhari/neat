"""
Description: Numpy implementation of backprop and gradient descent
author: syedmohsinbukhari@googlemail.com

Reference
http://neuralnetworksanddeeplearning.com/chap2.html
"""

# import numpy as np
import math


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
        if x > 100.0:
            return 1.0
        elif x < -100.0:
            return 0.0

        try:
            return 1.0 / (1.0 + math.exp(-1.0*x))
        except OverflowError:
            return 0.0
        finally:
            pass

    @staticmethod
    def derivative(x):
        return Sigmoid.forward(x) * (1 - Sigmoid.forward(x))


class Relu(ActivationFunction):

    @staticmethod
    def forward(x):
        if x > 0:
            return x
        else:
            return 0

    @staticmethod
    def derivative(x):
        if x > 0:
            return 1
        else:
            return 0


if __name__ == '__main__':
    print(Sigmoid.derivative(-1))
