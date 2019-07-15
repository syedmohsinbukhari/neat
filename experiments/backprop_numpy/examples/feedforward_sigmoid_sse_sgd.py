"""
Description: Numpy implementation of feed forward neural networks and
             and backpropagation
author: syedmohsinbukhari@googlemail.com
"""

import numpy as np

from experiments.backprop_numpy.models_sequential import FeedForwardModel
from experiments.backprop_numpy.losses import SSELoss
from experiments.backprop_numpy.optimizers import SGD

if __name__ == '__main__':
    ffm = FeedForwardModel([3, 2, 1])

    for i in range(1000):
        nn_out = ffm.forward(np.array([[1.0], [2.0], [3.0]]), with_grads=True)
        print(f"Neural Network Output: {nn_out}")

        loss_obj = SSELoss()
        loss_value = loss_obj.forward(np.array([[1.0]]), nn_out)
        print(f"Neural Network Loss: {loss_value}")

        ffm.backward(loss_obj)
        print(f"Neural Network Gradients: {ffm.layer_grads}")

        optimizer = SGD(0.1, ffm)
        optimizer.apply_grads()

        ffm.clear_grads()

    for i, (w, b) in enumerate(ffm.layers):
        print(f"layer {i} weights: {w}")
        print(f"layer {i} biases: {b}")
        print(f"final output: {ffm.forward(np.array([[1.0], [2.0], [3.0]]), with_grads=False)}")
