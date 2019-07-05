"""
Description: PyTest file for testing activations.py
author: syedmohsinbukhari@googlemail.com
"""

import pytest

from numpy import exp
from experiments.backprop_numpy.activations import Relu, Sigmoid


@pytest.mark.parametrize('test_input,output', [
    (0.0, 0.0),
    (1.0, 1.0),
    (-1.0, 0.0),
])
def test_relu_forward(test_input, output):
    assert Relu.forward(test_input) == output


@pytest.mark.parametrize('test_input,output', [
    (0.0, 0.5),
    (1.0, 1.0/(1.0+exp(-1.0))),
    (-1.0, 1.0/(1.0+exp(1.0))),
])
def test_sigmoid_forward(test_input, output):
    assert Sigmoid.forward(test_input) == output


@pytest.mark.parametrize('test_input,output', [
    (0.0, 0.0),
    (100.0, 1.0),
    (-1.0, 0.0),
])
def test_relu_derivative(test_input, output):
    assert Relu.derivative(test_input) == output


@pytest.mark.parametrize('test_input,output', [
    (0.0, 0.25),
    (1.0, Sigmoid.forward(1.0) * (1 - Sigmoid.forward(1.0))),
    (-1.0, Sigmoid.forward(-1.0) * (1 - Sigmoid.forward(-1.0))),
])
def test_sigmoid_derivative(test_input, output):
    assert Sigmoid.derivative(test_input) == output
