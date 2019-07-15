"""
Description: PyTest file for testing activations.py
author: syedmohsinbukhari@googlemail.com
"""

import pytest

from numpy import exp, array, shape
from experiments.backprop_numpy.activations import Relu, Sigmoid
from experiments.backprop_numpy.losses import SSELoss
from experiments.backprop_numpy.optimizers import SGD
from experiments.backprop_numpy.models_sequential import FeedForwardModel


class TestActivations:
    @pytest.mark.parametrize('test_input,output', [
        (0.0, 0.0),
        (1.0, 1.0),
        (-1.0, 0.0),
    ])
    def test_relu_forward(self, test_input, output):
        assert Relu.forward(test_input) == output

    @pytest.mark.parametrize('test_input,output', [
        (0.0, 0.5),
        (1.0, 1.0/(1.0+exp(-1.0))),
        (-1.0, 1.0/(1.0+exp(1.0))),
    ])
    def test_sigmoid_forward(self, test_input, output):
        assert Sigmoid.forward(test_input) == output

    @pytest.mark.parametrize('test_input,output', [
        (0.0, 0.0),
        (100.0, 1.0),
        (-1.0, 0.0),
    ])
    def test_relu_derivative(self, test_input, output):
        assert Relu.derivative(test_input) == output

    @pytest.mark.parametrize('test_input,output', [
        (0.0, 0.25),
        (1.0, Sigmoid.forward(1.0) * (1 - Sigmoid.forward(1.0))),
        (-1.0, Sigmoid.forward(-1.0) * (1 - Sigmoid.forward(-1.0))),
    ])
    def test_sigmoid_derivative(self, test_input, output):
        assert Sigmoid.derivative(test_input) == output


class TestLosses:
    sse_object = SSELoss()

    @pytest.mark.parametrize('test_input1,test_input2,output', [
        (0.0, 0.0, 0.0),
        (1.0, 0.0, 0.5),
        (3.0, 1.0, 2.0),
        (array(3.0), 1.0, array(2.0)),
        (array([3.0, 1.0]), array([1.0, 3.0]), array([2.0, 2.0])),
    ])
    def test_sse_loss_forward(self, test_input1, test_input2, output):
        assert (self.sse_object.forward(test_input1, test_input2) == output).all()

    @pytest.mark.parametrize('test_input1,test_input2,output', [
        (0.0, 0.0, 0.0),
        (1.0, 0.0, -1.0),
        (3.0, 1.0, -2.0),
        (array(3.0), 1.0, array(-2.0)),
        (array([3.0, 1.0]), array([1.0, 3.0]), array([-2.0, 2.0])),
    ])
    def test_sse_loss_backward(self, test_input1, test_input2, output):
        _ = self.sse_object.forward(test_input1, test_input2)
        assert (self.sse_object.backward() == output).all()


class TestOptimizers:
    nnm = FeedForwardModel([3, 2, 1])
    loss_obj = SSELoss()
    optimizer = SGD(0.01, nnm)

    def test_optimizer_apply_grads(self):
        nn_out = self.nnm.forward(array([[1.0], [1.0], [1.0]]), with_grads=True)
        _ = self.loss_obj.forward(array([[1.0]]), nn_out)
        self.nnm.backward(self.loss_obj)
        self.optimizer.apply_grads()

        assert len(self.nnm.layers) == len(self.nnm.layer_grads)


class TestModels:
    nnm = FeedForwardModel([3, 2, 1])
    loss_obj = SSELoss()
    optimizer = SGD(0.01, nnm)

    def test_feed_forward_forward(self):
        nn_out = self.nnm.forward(array([[1.0], [1.0], [1.0]]))
        assert shape(nn_out) == (self.nnm.neuron_config[-1], 1), "Gradients are not populated"

    def test_feed_forward_backward(self):
        nn_out = self.nnm.forward(array([[1.0], [1.0], [1.0]]), with_grads=True)
        _ = self.loss_obj.forward(array([[1.0]]), nn_out)
        self.nnm.backward(self.loss_obj)

        assert len(self.nnm.layer_grads) > 0, "Gradients are not populated"
