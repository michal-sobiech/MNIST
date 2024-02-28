from __future__ import annotations
import numpy as np


class Gradients:
    def __init__(self,
                 weight=np.empty((0, 0)),
                 bias=np.empty((0, 0)),
                 act_vals=np.empty((0, 0))) -> None:
        self.weight = weight
        self.bias = bias
        self.act_vals = act_vals

    def __add__(self, layer_gradients: Gradients):
        self.weight = np.vstack(
            self.weight,
            layer_gradients.weight
        )
        self.bias = np.vstack(
            self.bias,
            layer_gradients.bias
        )
        self.bias = np.vstack(
            self.bias,
            layer_gradients.bias
        )
