"""
Description: PyTest file for testing activations.py
author: syedmohsinbukhari@googlemail.com
"""

import pytest
import activations


@pytest.mark.parametrize('test_input,output', [
    (0.0, 0.0),
    (1.0, 1.0),
    (-1.0, 0.0),
])
def test_relu_forward(test_input, output):
    assert activations.Relu.forward(test_input) == output


@pytest.mark.parametrize('test_input,output', [
    (0.0, 0.5),
    (1.0, 1.0/(1.0+activations.exp(-1.0))),
    (-1.0, 1.0/(1.0+activations.exp(1.0))),
])
def test_sigmoid_forward(test_input, output):
    assert activations.Sigmoid.forward(test_input) == output


@pytest.mark.parametrize('test_input,output', [
    (0.0, 0.0),
    (100.0, 1.0),
    (-1.0, 0.0),
])
def test_relu_derivative(test_input, output):
    assert activations.Relu.derivative(test_input) == output


@pytest.mark.parametrize('test_input,output', [
    (0.0, 0.25),
    (1.0, activations.Sigmoid.forward(1.0) * (1 - activations.Sigmoid.forward(1.0))),
    (-1.0, activations.Sigmoid.forward(-1.0) * (1 - activations.Sigmoid.forward(-1.0))),
])
def test_sigmoid_derivative(test_input, output):
    assert activations.Sigmoid.derivative(test_input) == output

