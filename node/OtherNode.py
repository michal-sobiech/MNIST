import numpy as np
from node.NodeABC import NodeABC


class OtherNode(NodeABC):
    def __init__(self, prev_layer_node_count: int) -> None:
        super().__init__()
        self._setup(prev_layer_node_count)

    def _setup(self, prev_layer_node_count: int) -> None:
        self.weights = np.random.rand(1, len(prev_layer_node_count))
