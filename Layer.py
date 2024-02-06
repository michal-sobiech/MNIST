from Node import Node


class Layer:
    nodes: list[Node] = []

    def __init__(self, nodes: list[Node]) -> None:
        self.nodes = nodes