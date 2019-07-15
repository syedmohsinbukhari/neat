"""
Description: Numpy implementation of optimizers to minimize using loss using
             loss functions and applying gradients
author: syedmohsinbukhari@googlemail.com
"""

import numpy as np

from .models_sequential import SequentialModel


class Optimizers:
    def __init__(self, learning_rate, model):
        assert isinstance(model, SequentialModel)
        assert type(learning_rate) == float

        self.model = model
        self.lr = np.array(learning_rate)

    def apply_grads(self):
        pass


class SGD(Optimizers):
    def apply_grads(self):
        new_weights = []

        for i in range(len(self.model.layers)):
            w, b = self.model.layers[i]
            dw, db = self.model.layer_grads[i]

            w = np.subtract(w, np.multiply(self.lr, dw))
            b = np.subtract(b, np.multiply(self.lr, db))

            new_weights.append((w, b))

        self.model.layers = new_weights
