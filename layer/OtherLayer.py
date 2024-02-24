from typing import List
from numpy import exp
from layer.LayerABC import LayerABC
from node.NodeABC import NodeABC
from node.OtherNode import OtherNode


class OtherLayer(LayerABC):
    def __init__(self, node_count: int,
                 prev_layer_nodes: List[NodeABC]) -> None:
        super().__init__(node_count)
        self._generate_nodes(prev_layer_nodes)

    def activate(self) -> None:
        for node in self.nodes:
            node.activate()
        self.next_layer.activate()

    def _generate_nodes(self, node_count: int,
                        prev_layer_nodes: List[NodeABC]) -> None:
        for _ in range(node_count):
            self._generate_node(prev_layer_nodes)

    def _generate_node(self, prev_layer_nodes: List[NodeABC]) -> None:
        node = OtherNode(prev_layer_nodes)
        self.nodes.append(node)

    def _softmax(self, values: List[float]):
        denominator = sum(map(lambda v: exp(v), values))
        return [exp(v) / denominator for v in values]
