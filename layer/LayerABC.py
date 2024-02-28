from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import numpy as np
from numpy.typing import NDArray
from node.NodeABC import NodeABC


class LayerABC(ABC):
    def __init__(self, node_count: int) -> None:
        self._nodes: List[NodeABC] = []
        self._generate_nodes(node_count)

    def activate(self, input_vals: List[float]) -> NDArray:
        input_val_count = len(input_vals)
        node_count = len(self._nodes)

        if input_val_count != node_count:
            raise ValueError("Invalid input")

        layer_act_vals = np.empty((1, node_count))
        for i, nodes_and_input_vals in enumerate(zip(self._nodes, input_vals)):
            node, input_val = nodes_and_input_vals
            act_val = node.activate(input_val)
            layer_act_vals[i, 0] = act_val
        return layer_act_vals

    def _generate_nodes(self, node_count: int) -> None:
        for _ in range(node_count):
            self._generate_node()

    @abstractmethod
    def _generate_node(self) -> None:
        pass