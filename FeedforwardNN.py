from typing import Dict, List
from layer.LayerABC import LayerABC
from layer.InputLayer import InputLayer
from layer.MiddleLayer import MiddleLayer
from layer.OutputLayer import OutputLayer


class FeedforwardNN:
    batch_size: int = None
    layer_count: int = None
    layers: list[LayerABC] = []

    def __init__(self, layer_sizes: tuple[int], batch_size: int) -> None:
        self.layer_count = len(layer_sizes)
        self.batch_size = batch_size
        self._generate_layers(layer_sizes)

    def _generate_layer(self, index: int, node_count: int) -> None:
        layer: LayerABC = None
        if self._is_layer_first(index):
            layer = InputLayer(node_count)
        else:
            prev_layer = self.layers[index - 1]
            if self._is_layer_last(index):
                layer = OutputLayer(node_count, prev_layer)
            else:
                layer = MiddleLayer(node_count, prev_layer)
            layer.prev_layer.next_layer = layer
        self.layers.append(layer)

    def _generate_layers(self, layer_sizes: tuple[int]) -> None:
        for index, node_count in enumerate(layer_sizes):
            print(f"index: {index}, node count: {node_count}")
            self._generate_layer(index, node_count)

    def train_on_a_batch(self, samples: List[Dict]) -> None:
        # for sample in samples:
        #     self
        pass

    def single_sample_error(self, sample: Dict) -> List[float]:
        

    def _is_layer_last(self, layer_index: int) -> bool:
        return layer_index == self.layer_count - 1

    def _is_layer_first(self, layer_index: int) -> bool:
        return layer_index == 0

    def _get_the_first_layer(self) -> LayerABC:
        return self.layers[0]

    def _get_the_last_layer(self) -> LayerABC:
        return self.layers[-1]

    def backpropagate(self, grad)