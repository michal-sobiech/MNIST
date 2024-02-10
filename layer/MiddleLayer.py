from layer.LayerABC import LayerABC
from node.MiddleNode import MiddleNode


class MiddleLayer(LayerABC):
    def __init__(self, node_count: int, prev_layer: LayerABC) -> None:
        self.prev_layer: LayerABC = prev_layer
        self.next_layer: LayerABC = None
        super().__init__(node_count)

    def activate(self) -> None:
        for node in self.nodes:
            node.activate()
        self.next_layer.activate()

    def _generate_node(self) -> None:
        node = MiddleNode()
        self.nodes.append(node)
        node.generate_prev_conns(self.prev_layer.nodes)
