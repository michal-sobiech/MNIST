from typing import Dict, List
from LayerABC import Layer


class FeedforwardNN:
    batch_size: int = None
    layer_count: int = None
    layers: list[Layer] = []

    def __init__(self, layer_sizes: tuple[int], batch_size: int) -> None:
        self.layer_count = len(layer_sizes)
        self.batch_size = batch_size
        self.__generate_layers(layer_sizes)

    def __generate_layer(self, index: int, node_count: int) -> None:
        layer = Layer(node_count)
        if not self.__is_layer_first(index):
            layer.prev_layer = self.layers[index - 1]
            layer.prev_layer.next_layer = layer
        self.layers.append(layer)

    def __generate_layers(self, layer_sizes: tuple[int]) -> None:
        for index, node_count in enumerate(layer_sizes):
            print(f"index: {index}, node count: {node_count}")
            self.__generate_layer(index, node_count)

    def train_on_a_batch(self, samples: List[Dict]) -> None:
        # for sample in samples:
        #     self
        pass

    def single_sample_error(self, sample: Dict) -> List[float]:
        pass

    def __is_layer_last(self, layer_index: int) -> bool:
        return layer_index == self.layer_count - 1

    def __is_layer_first(self, layer_index: int) -> bool:
        return layer_index == 0

    def __get_the_first_layer(self) -> Layer:
        return self.layers[0]

    def __get_the_last_layer(self) -> Layer:
        return self.layers[-1]
