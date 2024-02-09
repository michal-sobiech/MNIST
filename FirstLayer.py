from LayerABC import Layer
from EntryNode import EntryNode


class FirstLayer(Layer):
    def __init__(self, node_count: int, is_first: bool) -> None:
        super().__init__(node_count, is_first)

    def __generate_node(self) -> None:
        node = EntryNode()
        self.nodes.append(node)
