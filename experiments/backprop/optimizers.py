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

    def get_gradient(self, wgts, wgt_grds, biases, bias_grd):
        """
        w - eta*grad
        Add new weights
        :return:
        """
        updated_weights = []
        updated_biases = []

        # wgt_grds = wgt_grds[::-1]
        # bias_grd = bias_grd[::-1]

        for layer_idx in range(len(wgts)):
            updated_weights.append(wgts[layer_idx] - self.lr*wgt_grds[layer_idx])
            updated_biases.append(biases[layer_idx] - self.lr*bias_grd[layer_idx])

        return updated_weights, updated_biases
