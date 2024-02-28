import numpy as np
from numpy.typing import NDArray
from layer.LayerABC import LayerABC
from node.OtherNode import OtherNode
from Gradients import Gradients


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

    def calc_gradients(self,
                       self_z_vals: NDArray,
                       prev_layer_act_vals: NDArray,
                       self_act_val_gradient: NDArray,
                       self_act_val_gradient: NDArray,
                       self_z_vals: NDArray,
                       self_act_vals: NDArray,
                       next_layer_z_vals: NDArray,
                       next_layer_act_val_gradient: NDArray,
                       expected_output: NDArray) -> Gradients:
        act_val_gradient: NDArray = self.calc_act_val_gradient(
            self_act_vals,
            next_layer_z_vals,
            next_layer_act_val_gradient,
            expected_output
        )
        return Gradients(
            weight=self.calc_weight_gradient(
                self_z_vals,
                prev_layer_act_vals,
                self_act_val_gradient
            ),
            bias=self.calc_bias_gradient(
                self_act_val_gradient,
                self_z_vals
            )
        )

    def calc_weight_gradient(self,
                             self_z_vals: NDArray,
                             prev_layer_act_vals: NDArray,
                             self_act_val_gradient: NDArray) -> NDArray:
        """
        Calculates dC / dw for all weights in the layer
        """
        j = len(self._nodes)
        k = len(prev_layer_act_vals)
        return (
            self.relu_deriv(np.diag(self_z_vals))
            @ (np.diag(self_act_val_gradient) @ np.ones((j, k)))
            @ np.diag(prev_layer_act_vals)
        )

    def calc_bias_gradient(self,
                           self_act_val_gradient: NDArray,
                           self_z_vals: NDArray) -> NDArray:
        """
        Calculates dC / db for all nodes in the layer
        """
        return (
            self_act_val_gradient
            * self.relu_deriv(self_z_vals)
        )

    def calc_act_val_gradient(self,
                              self_act_vals: NDArray,
                              next_layer_z_vals: NDArray,
                              next_layer_act_val_gradient: NDArray,
                              expected_output: NDArray) -> NDArray:
        """
        Calculates dC / da for all nodes in the layer
        """
        if self._is_last:
            return 2 * (self_act_vals - expected_output)
        else:
            return (
                np.transpose(next_layer_act_val_gradient)
                @ self.relu_deriv(next_layer_z_vals)
                @ self_act_vals
            )
