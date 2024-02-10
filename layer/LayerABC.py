from __future__ import annotations
from abc import ABC, abstractmethod
from node.NodeABC import NodeABC
from typing import List


class LayerABC(ABC):
    def __init__(self, node_count: int) -> None:
        self.nodes: List[NodeABC] = []
        self._generate_nodes(node_count)

    def _generate_nodes(self, node_count: int) -> None:
        for _ in range(node_count):
            self._generate_node()

    @abstractmethod
    def _generate_node(self) -> None:
        pass
