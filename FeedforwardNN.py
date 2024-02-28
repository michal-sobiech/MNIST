from typing import List, Tuple
from numpy.typing import NDArray
import numpy as np
from layer.LayerABC import LayerABC
from layer.InputLayer import InputLayer
from layer.OtherLayer import OtherLayer
from Sample import Sample
from Gradients import Gradients


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
            self._generate_layer(node_count, index == 0)

    def train_on_a_batch(self, samples: List[Sample]) -> None:
        batch_gradient = self.get_gradient_avg_from_batch(samples)
        self.backpropagate(batch_gradient)

    def get_gradient_avg_from_batch(self, samples: List[Sample]) -> NDArray:
        weights = self.get_weights()
        biases = self.get_biases()

        gradient_sum = Gradients()
        for sample in samples:
            act_vals = self.single_sample_act_vals(sample.input_values)
            gradient_sum += self.calc_gradients(act_vals)
        return gradient_sum / len(samples)
    
    def get_gradient_from_sample(self,
                                 weights: NDArray,
                                 biases: NDArray, 
                                 sample: Sample) -> Gradients:
        gradients = 


    def _softmax(self, values: NDArray):
        denominator = sum(np.exp(values))
        return (lambda x: np.exp(x) / denominator)(values)

    def single_sample_error(self, sample: Sample) -> float:
        layers_act_vals = self.single_sample_act_vals(sample.input_values)
        network_output = self._softmax(layers_act_vals[-1])
        return self._mse(network_output, sample.expected_output)

    def _mse(self, network_output: NDArray, expected_output: NDArray) -> float:
        return (expected_output - network_output) ** 2

    def single_sample_act_vals(self, network_input: NDArray) -> List[NDArray]:
        """
        Returns the layer activation values.
        """
        layers_act_vals: List[NDArray] = []
        layer_input = network_input
        for layer in self.layers:
            act_vals = layer.activate(layer_input)
            layers_act_vals.append(act_vals)
            layer_input = act_vals
        return layers_act_vals

    def calc_gradients(self, layers_act_vals: List[NDArray]):
        pass

    def get_weights(self) -> List[NDArray]:
        return [layer.get_weights() for layer in self.layers[1:]]

    def get_biases(self) -> List[NDArray]:
        return [layer.get_biases() for layer in self.layers[1:]]

    def backpropagate(self, gradients: Gradients):
        pass
