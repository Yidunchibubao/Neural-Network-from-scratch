# -*- coding: utf-8 -*-
"""network.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ObY9agzSVaXGoWiRtxHNZI9-dSsxfHsS
"""

from .layers import LinearLayer, ActivationFunction
from . import cp


class NeuralNetwork:
    def __init__(self, layers_config, learning_rate=0.01):
        """
        layers_config: list of tuples
          (output_size, activation_name, input_size)
        e.g. [(16, "relu", 10), (3, "softmax", 16)]
        """
        self.lr = learning_rate
        self.layers = []
        for out_sz, act, in_sz in layers_config:
            self.layers.append(LinearLayer(in_sz, out_sz))
            self.layers.append(ActivationFunction(act))

    def forward(self, x):
        """
        x: input h^(0), shape = (input_size, batch)
        returns h^(L+1) after final activation
        """
        h = x
        for layer in self.layers:
            h = layer.forward(h)
        return h

    def compute_loss(self, y_pred, y_true):
        """
        Cross-entropy loss, averaged over batch:
        y_pred: probabilities after softmax, shape = (C, batch)
        y_true: one-hot labels,         shape = (C, batch)
        """
        eps = 1e-9 # small constant for numerical stability
        return -cp.sum(y_true * cp.log(y_pred + eps)) / y_true.shape[1] # Compute -sum(y_true * log(y_pred + eps)) / batch_size

    def compute_loss_derivative(self, y_pred, y_true):
        """
        ∇_{a^(L+1)} L = (y_pred - y_true) / batch
        """
        return (y_pred - y_true) / y_true.shape[1]

    def backward(self, y_pred, y_true):
        grad = self.compute_loss_derivative(y_pred, y_true)
        for layer in reversed(self.layers):
            if isinstance(layer, ActivationFunction):
                grad = layer.backward(grad)
            else:  # LinearLayer
                grad = layer.backward(grad, self.lr)
        return grad  # gradient w.r.t. network input
