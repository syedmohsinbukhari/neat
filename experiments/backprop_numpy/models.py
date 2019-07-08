"""
Description: Numpy implementation of feed forward neural networks and
             and backpropagation
author: syedmohsinbukhari@googlemail.com

Reference
http://neuralnetworksanddeeplearning.com/chap2.html
"""

import numpy as np
from .activations import Sigmoid


class SequentialModel:
    def __init__(self):
        pass

    def forward(self, x, with_grads=False):
        pass

    def backward(self, x):
        pass


class FeedForwardModel(SequentialModel):
    def __init__(self, neuron_config):
        super().__init__()
        self.layers = []

        for i in range(len(neuron_config)-1):
            w = np.zeros((neuron_config[i], neuron_config[i+1]), dtype=np.float)
            b = np.zeros((neuron_config[i+1], 1), dtype=np.float)
            self.layers.append((w, b))

    def forward(self, x, with_grads=False):
        if len(self.layers) == 0:  # Make sure this is right
            return np.abs(x)

        x_n = x
        for layer in self.layers:
            x_n_1 = Sigmoid.forward(np.add(np.dot(layer[0], x_n), layer[1]))
            x_n = x_n_1

        return x_n

    def backward(self, x):
        pass
