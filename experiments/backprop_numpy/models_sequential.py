"""
Description: Numpy implementation of feed forward neural networks and
             and backpropagation
author: syedmohsinbukhari@googlemail.com

Reference
http://neuralnetworksanddeeplearning.com/chap2.html
"""

import numpy as np
from activations import Sigmoid


class SequentialModel:
    def __init__(self):
        pass

    def forward(self, x, with_grads=False):
        pass

    def backward(self, loss_grad):
        pass


class FeedForwardModel(SequentialModel):
    def __init__(self, neuron_config):
        super().__init__()
        self.layers = []
        self.layer_z = []
        self.layer_x_n1 = []
        self.layer_grads = []

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

    def backward(self, loss_grad):
        if len(self.layer_x_n1) <= 1:
            print("Exiting because no forward pass with grads")
            return

        delta_n = loss_grad
        self.layer_grads = []  # (dx_n1/dx_n, dx_n1/dw_n, dx_n1/db_n)

        for i in range(len(self.layer_x_n1)-1, 0, -1):
            x_n1 = self.layer_x_n1[i]
            x_n = self.layer_x_n1[i-1]
            z = self.layer_z[i-1]
            w_n, _ = self.layers[i-1]

            # print(f'Ones vector: {np.ones((x_n1.shape[0], 1), dtype=np.float)}')
            # print(f'x_n.T: {x_n.T}')
            print(f'w_n.T:\n{w_n.T}', end='\n\n')
            print(f'np.dot(w_n.T, delta_n):\n{np.dot(w_n.T, delta_n)}', end='\n\n')
            print(f'Sigmoid.derivative(z):\n{Sigmoid.derivative(z)}', end='\n\n')
            delta_n = np.multiply(Sigmoid.derivative(z), np.dot(w_n.T, delta_n))
            print(f'delta_n:\n{delta_n}', end='\n\n')
            # dx_n1_dx_n = np.dot(w_n.T, Sigmoid.derivative(z))
            # dx_n1_dw_n = np.dot(
            #     Sigmoid.derivative(z),
            #     np.outer(np.ones((x_n1.shape[0], 1), dtype=np.float), x_n.T)
            # )
            # dx_n1_db_n = Sigmoid.derivative(z)
            #
            # self.layer_grads.append((dx_n1_dx_n, dx_n1_dw_n, dx_n1_db_n))

        return


if __name__ == '__main__':
    ffm = FeedForwardModel([3, 2, 1])

    nn_out = ffm.forward(np.array([[1.0], [2.0], [3.0]]), with_grads=True)
    print(f"Neural Network Output: {nn_out}")

    ffm.backward(np.array([[0.1]]))
    print(f"Neural Network Gradients: {ffm.layer_grads}")
