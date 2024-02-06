from Layer import Layer
from Node import Node
from Connection import Connection


class FeedforwardNN:
    layers: list[Layer] = []

    def __init__(self, layer_sizes: list[int]) -> None:
        self.__generate_layers()

    def __generate_layers(self, layer_sizes: list[int]) -> None:
        for layer_index, layer_size in enumerate(layer_sizes):
            # For each layer
            layer_nodes = []
            for _ in range(layer_size):
                # For each node in the layer
                node = Node()
                layer_nodes.append(node)

                # Add connections to the previous layer
                if layer_index == 0:
                    # The layer must not be the first one
                    continue
                prev_layer = self.layers[layer_index - 1]
                for prev_node in prev_layer.nodes:
                    conn = Connection(prev_node=prev_node, next_node=node)
                    prev_node.add_next_conn(conn)
                    node.add_prev_conn(conn)
            self.layers.append(Layer(layer_nodes))
