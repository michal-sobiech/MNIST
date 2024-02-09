from __future__ import annotations
from abc import ABC, abstractmethod
from NodeABC import Node
from EntryNode import EntryNode


class LayerABC(ABC):
    nodes: list[Node] = []
    prev_layer: LayerABC = None
    next_layer: LayerABC = None

    def __init__(self, node_count: int, is_first: bool) -> None:
        self.__generate_nodes(node_count, is_first)

    def activate(self) -> None:
        for node in self.nodes:
            node.activate()
        self.next_layer.activate()

    def __generate_nodes(self, node_count: int, is_first: bool) -> None:
        for _ in range(node_count):
            self.__generate_node()

    @abstractmethod
    def __generate_node(self) -> None:
        pass
