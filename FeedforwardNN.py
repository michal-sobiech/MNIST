from typing import Dict, List, Tuple
from layer.LayerABC import LayerABC
from layer.InputLayer import InputLayer
from layer.OtherLayer import OtherLayer


class FeedforwardNN:
    def __init__(self, layer_sizes: Tuple[int], batch_size: int) -> None:
        self.batch_size: int = batch_size
        self.layers: List[LayerABC] = []
        self._generate_layers(layer_sizes)

    def _generate_layer(self, node_count: int, is_first: bool) -> None:
        layer: LayerABC = None
        if is_first:
            layer = InputLayer(node_count)
        else:
            layer = OtherLayer(node_count)
        self.layers.append(layer)

    def _generate_layers(self, layer_sizes: Tuple[int]) -> None:
        for index, node_count in enumerate(layer_sizes):
            print(f"index: {index}, node count: {node_count}")
            self._generate_layer(index, node_count)

    def train_on_a_batch(self, samples: List[Dict]) -> None:
        # for sample in samples:
        #     self
        pass

    def single_sample_error(self, sample: Dict) -> List[float]:
        pass

    def _get_the_first_layer(self) -> LayerABC:
        return self.layers[0]

    def _get_the_last_layer(self) -> LayerABC:
        return self.layers[-1]

    def backpropagate(self, grad):
        pass
