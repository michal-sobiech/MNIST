from __future__ import annotations
import numpy as np


class Gradients:
    def __init__(self,
                 weight_gradient=np.empty((0, 0)),
                 bias_gradient=np.empty((0, 0))) -> None:
        self.weight_gradient = weight_gradient
        self.bias_gradient = bias_gradient

    def __add__(self, layer_gradients: Gradients):
        self.weight_gradient = np.vstack(
            self.weight_gradient,
            layer_gradients.weight_gradient
        )
        self.bias_gradient = np.vstack(
            self.bias_gradient,
            layer_gradients.bias_gradient
        )
