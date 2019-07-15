"""
Description: Numpy implementation of feed forward neural networks and
             and backpropagation
author: syedmohsinbukhari@googlemail.com
"""

import numpy as np

from experiments.backprop_numpy.models_sequential import FeedForwardModel
from experiments.backprop_numpy.losses import SSELoss

if __name__ == '__main__':
    ffm = FeedForwardModel([3, 2, 1])

    nn_out = ffm.forward(np.array([[1.0], [2.0], [3.0]]), with_grads=True)
    print(f"Neural Network Output: {nn_out}")

    loss_obj = SSELoss()
    loss_value = loss_obj.forward(np.array([[1.0]]), nn_out)
    print(f"Neural Network Loss")

    ffm.backward(loss_obj)
    print(f"Neural Network Gradients: {ffm.layer_grads}")
