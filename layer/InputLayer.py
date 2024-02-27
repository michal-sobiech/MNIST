import numpy as np
from layer.LayerABC import LayerABC
from node.InputNode import InputNode


class InputLayer(LayerABC):
    def __init__(self, node_count: int) -> None:
        super().__init__(node_count)

    def _generate_node(self) -> None:
        node = InputNode()
        self._nodes.append(node)
