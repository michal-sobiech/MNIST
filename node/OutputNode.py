from node.NonfirstNode import NonfirstNodeABC
from layer.LayerABC import LayerABC


class OutputNode(NonfirstNodeABC):
    prev_layer: LayerABC = None

    def __init__(self) -> None:
        super().__init__()
