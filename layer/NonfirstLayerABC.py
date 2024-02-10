from layer.LayerABC import LayerABC


class NonfirstLayerABC(LayerABC):
    def __init__(self, node_count: int) -> None:
        super().__init__(node_count)

    def activate(self) -> None:
        for node in self.nodes:
            node.activate()
        self.next_layer.activate()
