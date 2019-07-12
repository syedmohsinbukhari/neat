"""
Description: Numpy implementation of loss functions and their derivatives
author: syedmohsinbukhari@googlemail.com
"""

import numpy as np


class Losses:
    def __init__(self):
        pass

    def forward(self, target, achieved):
        pass

    def backward(self, target, achieved):
        pass


class SSELoss(Losses):
    def forward(self, target, achieved):
        assert np.shape(target) == np.shape(achieved), 'Shape of target and achieved is not same'

        sse_loss = np.sum(np.power(np.subtract(target, achieved), 2))
        return sse_loss

    def backward(self, target, achieved):
        assert np.shape(target) == np.shape(achieved), 'Shape of target and achieved is not same'

        sse_grad = np.multiply(2.0, np.subtract(achieved, target))
        return sse_grad
