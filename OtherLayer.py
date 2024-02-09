from LayerABC import Layer
from OtherNode import OtherNode


class OtherLayer(Layer):
    def __init__(self, node_count: int) -> None:
        super().__init__(node_count)

    def __generate_node(self) -> None:
        node = OtherNode()
        self.nodes.append(node)
        node.generate_prev_conns(self.prev_layer.nodes)