from Node import Node


class Connection:
    weight: float = None
    prev_node: Node = None
    next_node: Node = None

    def __init__(self, weight: float,
                 prev_node: Node,
                 next_node: Node) -> None:
        self.weight = weight
        self.prev_node = prev_node
        self.next_node = next_node