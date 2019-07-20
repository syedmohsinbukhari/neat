"""
description: Optimizer classes for the library
author: bazarovay@github.com
"""


class Optimizer(object):
    """
    Abstract class
    SGD,
    """
    def __init__(self):
        self.weights = []
        self.changes = []


class SGD(Optimizer):
    """
    Stochastic Gradient Descent
    """
    def __init__(self, lr):
        super(SGD, self).__init__()
        self.lr = lr

    def get_gradient(self):
        """
        w - eta*grad
        Add new weights
        :return:
        """

        for layer_idx in range(self.weights):
            self.weights[layer_idx] = self.weights[layer_idx] - self.lr*self.gradients[layer_idx]

        return self.weights
