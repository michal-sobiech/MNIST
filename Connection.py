from Node import Node
import numpy as np


class Connection:
    weight: float = None
    prev_node: Node = None
    next_node: Node = None

    def __init__(self,
                 prev_node: Node,
                 next_node: Node) -> None:
        self.weight = np.random.uniform(-0.1, 0.1)
        self.prev_node = prev_node
        self.next_node = next_node
