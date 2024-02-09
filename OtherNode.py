from typing import List
from NodeABC import Node
from Connection import Connection


class OtherNode(Node):
    def __init__(self) -> None:
        super().__init__()

    def generate_prev_conns(self, prev_layer_nodes: List[Node]) -> None:
        """
        Connects the node to the nodes from the previous layer.
        """
        for prev_node in prev_layer_nodes:
            conn = Connection()
            self.add_prev_conn(conn)
            prev_node.add_next_conn(conn)

    def activate(self):
        input = self.__get_input()
        self.value = self.__activation_function(input)

    def __get_input(self):
        input = sum([c.weight * c.prev_node.value for c in self.prev_conns])
        input += self.bias
        return input

    def add_next_conn(self, conn: Connection) -> None:
        self.next_conns.append(conn)
