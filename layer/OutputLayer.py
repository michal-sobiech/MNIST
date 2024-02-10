from typing import List
from numpy import exp
from layer.LayerABC import LayerABC
from node.OutputNode import OutputNode


class OutputLayer(LayerABC):
    def __init__(self, node_count: int, prev_layer: LayerABC) -> None:
        self.prev_layer: LayerABC = prev_layer
        super().__init__(node_count)

    def activate(self) -> None:
        for node in self.nodes:
            node.activate()
        self.next_layer.activate()

    def _generate_node(self) -> None:
        node = OutputNode()
        self.nodes.append(node)
        node.generate_prev_conns(self.prev_layer.nodes)

    def _softmax(self, values: List[float]):
        denominator = sum(map(lambda v: exp(v), values))
        return [exp(v) / denominator for v in values]
