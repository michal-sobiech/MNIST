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
        
    def s
        
    def calc_dC_over_dw(self, self_act_vals: NDArray)