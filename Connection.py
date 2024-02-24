import numpy as np
from node.NodeABC import NodeABC


class Connection:
    def __init__(self, prev_node: NodeABC) -> None:
        self.prev_node: NodeABC = prev_node
        self.weight = np.random.uniform(-0.1, 0.1)
