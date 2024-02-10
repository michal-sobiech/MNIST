from typing import List
from LayerABC import LayerABC


class OutputLayer(LayerABC):
    prev_layer: LayerABC

    def __init__(self, node_count: int) -> None:
        super().__init__(node_count)

    def _softmax(self, values: List[float]):
        lowest = min(values)
        highest = max(values)
        