from typing import List
from numpy import exp
import numpy as np
from numpy.typing import NDArray
from layer.LayerABC import LayerABC
from node.OtherNode import OtherNode


class OtherLayer(LayerABC):
    def __init__(self, node_count: int,
                 prev_layer_node_count: int,
                 is_last: bool) -> None:
        super().__init__(node_count)
        self._prev_layer_node_count = prev_layer_node_count
        self._generate_nodes(prev_layer_node_count)
        self._is_last = is_last

    def _generate_node(self, prev_layer_node_count: int) -> None:
        node = OtherNode(prev_layer_node_count)
        self._nodes.append(node)

    def get_weights(self) -> NDArray:
        weights = np.empty()
        for node in self._nodes:
            weights = np.vstack(
                weights,
                node.weights
            )
        return weights

    def get_biases(self) -> NDArray:
        biases = np.empty((len(self._nodes, 1)))
        for i, node in enumerate(self._nodes):
            biases[i, 0] = node.bias
        return biases

    def calc_gradients(self, self_act_vals: NDArray):
        pass

    def relu(self, x: float) -> float:
        return x if x > 0 else 0

    def relu_deriv(self, x: float) -> float:
        return 1 if x > 0 else 0

    def calc_dC_over_dw(self,
                        self_z_vals: NDArray,
                        prev_layer_node_count: int,
                        prev_layer_act_vals: NDArray,
                        self_dC_over_da: NDArray) -> NDArray:
        """
        Calculates dC / dw for all weights in the layer
        """
        j = len(self._nodes)
        k = prev_layer_node_count
        # TODO check matrix sizes
        return (
            self.relu_deriv(np.diag(self_z_vals))
            * (np.diag(self_dC_over_da) * np.ones((j, k)))
            * np.diag(prev_layer_act_vals)
        )

    def calc_dC_over_da(self, self_act_vals: NDArray,
                        next_layer_node_count: int,
                        next_layer_z_vals: NDArray,
                        expected_output: NDArray,
                        next_layer_dC_over_da: NDArray) -> NDArray:
        if self._is_last:
            return 2 * (self_act_vals - expected_output)
        else:
            return (
                np.transpose(next_layer_dC_over_da)
                * self.relu_deriv(next_layer_z_vals)
                * self_act_vals
            )
