from typing import List
from node.NodeABC import NodeABC
from layer.LayerABC import LayerABC
from Connection import Connection


class OutputNode(NodeABC):
    def __init__(self) -> None:
        self.prev_layer: LayerABC = None
        super().__init__()

    def add_prev_conn(self, conn: Connection) -> None:
        self.prev_conns.append(conn)

    def generate_prev_conns(self, prev_layer_nodes: List[NodeABC]) -> None:
        """
        Connects the node to the nodes from the previous layer.
        """
        for prev_node in prev_layer_nodes:
            conn = Connection()
            self.add_prev_conn(conn)
            prev_node.add_next_conn(conn)

    def activate(self):
        input = self._get_input()
        self.value = self._activation_function(input)

    def _get_input(self):
        input = sum([c.weight * c.prev_node.value for c in self.prev_conns])
        input += self.bias
        return input
