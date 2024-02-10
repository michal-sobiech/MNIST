from typing import List
from layer.LayerABC import LayerABC
from node.InputNode import InputNode


class InputLayer(LayerABC):
    def __init__(self, node_count: int) -> None:
        self.next_layer: LayerABC = None
        super().__init__(node_count)

    def activate(self, input_values: List[float]) -> None:
        if len(input_values) != len(self.nodes):
            raise ValueError("Invalid input")
        for node, input_val in zip(self.nodes, input_values):
            node.activate(input_val)
        self.next_layer.activate()

    def _generate_node(self) -> None:
        node = InputNode()
        self.nodes.append(node)
