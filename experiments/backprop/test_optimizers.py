import pytest
import numpy as np

from .optimizers import SGD
from .activations import Activation
from .losses import MSE


def test_sgd():
    sgd = SGD(lr=0.01)
    assert(sgd.lr == 0.01)


def test_activation():
    sigmoid = Activation('sigmoid')
    activation_val = sigmoid.get(0)
    assert activation_val == 0.5


def test_mse():
    mse = MSE()
    mse_error = mse.calculate(predicted=2, output=1)
    assert mse_error == 0.5
