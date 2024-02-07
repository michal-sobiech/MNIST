from __future__ import annotations
from Node import Node
from EntryNode import EntryNode


class Layer:
    nodes: list[Node] = []
    prev_layer: Layer = None
    next_layer: Layer = None

    def __init__(self, node_count: int) -> None:
        self.__generate_nodes(node_count)

    def activate(self) -> None:
        for node in self.nodes:
            node.activate()
        self.next_layer.activate()

    def __generate_nodes(self, node_count: int) -> None:
        for _ in range(node_count):
            self.__generate_node()

    def generate_node_conns(self) -> None:
        for node in self.nodes:
            node.generate_prev_conns()

    def __generate_node(self) -> None:
        node = EntryNode() if self.__is_first() else Node()
        self.nodes.append(node)
        if not self.__is_first():
            node.generate_prev_conns(self.prev_layer.nodes)

    def __is_last(self):
        return not self.next_layer

    def __is_first(self):
        return not self.prev_layer
