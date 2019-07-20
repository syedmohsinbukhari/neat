"""
description: Loss functions
author: bazarovay@github.com
"""
import numpy as np


class Loss:

    def calculate(self, *kwargs):
        pass

    def derivative(self, *kwargs):
        pass


class MSE(Loss):

    def calculate(self, predicted, output):
        """

        .5 * (actual - pred)^2
        :return:
        """

        return 0.5*np.subtract(predicted, output)**2

    def derivative(self, predicted, output):
        """
        Derivative of the quadratic cost
        predicted - output
        :return:
        """
        return np.subtract(predicted, output)