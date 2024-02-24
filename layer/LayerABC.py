from __future__ import annotations
from abc import ABC, abstractmethod
from node.NodeABC import NodeABC
from typing import List


class LayerABC(ABC):
    def __init__(self, node_count: int) -> None:
        self.nodes: List[NodeABC] = []
        self._generate_nodes(node_count)

    @abstractmethod
    def _generate_nodes(self) -> None:
        pass

    @abstractmethod
    def _generate_node(self) -> None:
        pass
