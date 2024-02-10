from typing import List
from numpy import exp
from LayerABC import LayerABC


class OutputLayer(LayerABC):
    prev_layer: LayerABC

    def __init__(self, node_count: int) -> None:
        super().__init__(node_count)

    def _softmax(self, values: List[float]):
        denominator = sum(map(lambda v: exp(v), values))
        return [exp(v) / denominator for v in values]
