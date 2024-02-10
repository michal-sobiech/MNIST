from layer.NonfirstLayerABC import NonfirstLayerABC
from layer.LayerABC import LayerABC
from node.MiddleNode import MiddleNode


class MiddleLayer(NonfirstLayerABC):
    prev_layer: LayerABC = None
    next_layer: LayerABC = None

    def __init__(self, node_count: int, prev_layer: LayerABC) -> None:
        self.prev_layer = prev_layer
        super().__init__(node_count)

    def _generate_node(self) -> None:
        node = MiddleNode()
        self.nodes.append(node)
        node.generate_prev_conns(self.prev_layer.nodes)
