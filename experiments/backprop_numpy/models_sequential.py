"""
Description: Numpy implementation of feed forward neural networks and
             and backpropagation
author: syedmohsinbukhari@googlemail.com

Reference
http://neuralnetworksanddeeplearning.com/chap2.html
"""

import numpy as np
from .activations import Sigmoid
from .losses import Losses


class SequentialModel:
    def __init__(self, neuron_config):
        self.layers = []
        self.layer_grads = []
        self.neuron_config = neuron_config

    def forward(self, x, with_grads=False):
        pass

    def backward(self, loss_obj):
        pass

    def clear_grads(self):
        pass


class FeedForwardModel(SequentialModel):
    def __init__(self, neuron_config):
        super().__init__(neuron_config)
        self.layer_z = []
        self.layer_x_n1 = []

        for i in range(len(neuron_config)-1):
            w = np.zeros((neuron_config[i+1], neuron_config[i]), dtype=np.float)
            b = np.zeros((neuron_config[i+1], 1), dtype=np.float)
            self.layers.append((w, b))

    def forward(self, x, with_grads=False):
        if len(self.layers) == 0:  # Make sure this is right
            return np.abs(x)

        self.layer_z = []
        self.layer_x_n1 = [x]

        x_n = x
        for (w, b) in self.layers:
            z = np.add(np.dot(w, x_n), b)
            x_n1 = Sigmoid.forward(z)
            x_n = x_n1

            if with_grads:
                self.layer_z.append(z)
                self.layer_x_n1.append(x_n1)

        return x_n

    def backward(self, loss_obj):
        assert isinstance(loss_obj, Losses)
        assert len(self.layer_x_n1) > 1, "Exiting because no forward pass with grads"
        assert len(self.layer_grads) < 1, "Exiting because previous gradients are not cleared"

        loss_grad = loss_obj.backward()

        delta_arr = [loss_grad]
        self.layer_grads = []  # (delta_n1, delta_w_n, delta_b_n)

        for i in range(len(self.layer_x_n1)-1, 0, -1):
            x_n1 = self.layer_x_n1[i]
            x_n = self.layer_x_n1[i-1]
            z = self.layer_z[i-1]
            w_n, _ = self.layers[i-1]

            delta_n1 = delta_arr[-1]
            delta_n = np.dot(w_n.T, np.multiply(Sigmoid.derivative(z), delta_n1))
            delta_arr.append(delta_n)

            delta_w_n = np.multiply(
                np.outer(np.ones((x_n1.shape[0], 1), dtype=np.float), x_n.T),
                np.multiply(Sigmoid.derivative(z), delta_n1)
            )
            delta_b_n = np.multiply(Sigmoid.derivative(z), delta_n1)

            self.layer_grads.append((delta_w_n, delta_b_n))

        self.layer_grads = self.layer_grads[::-1]

        return

    def clear_grads(self):
        self.layer_grads = []
