"""
Description: Numpy implementation of loss functions and their derivatives
author: syedmohsinbukhari@googlemail.com
"""

import numpy as np


class Losses:
    def __init__(self):
        self.target = None
        self.achieved = None

    def forward(self, target, achieved):
        pass

    def backward(self):
        pass


class SSELoss(Losses):
    def forward(self, target, achieved):
        assert np.shape(target) == np.shape(achieved), 'Shape of target and achieved is not same'

        self.target = target
        self.achieved = achieved

        sse_loss = np.multiply(np.power(np.subtract(self.target, self.achieved), 2), 0.5)
        return sse_loss

    def backward(self):
        assert np.shape(self.target) == np.shape(self.achieved), "Shape of target and achieved is not same"
        assert self.achieved is not None, "Need to compute loss before computing gradient"
        assert self.target is not None, "Need to compute loss before computing gradient"

        sse_grad = np.subtract(self.achieved, self.target)

        return sse_grad
