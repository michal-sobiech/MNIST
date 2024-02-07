from __future__ import annotations
import numpy as np
from typing import List
from Connection import Connection


class Node:
    value: int = None
    bias: float = None
    prev_conns: list[Connection] = []
    next_conns: list[Connection] = []

    def __init__(self) -> None:
        self.bias = np.random.uniform(-0.01, 0.01)

    def add_prev_conn(self, conn: Connection) -> None:
        self.prev_conns.append(conn)

    def add_next_conn(self, conn: Connection) -> None:
        self.next_conns.append(conn)

    def __get_input(self):
        input = sum([c.weight * c.prev_node.value for c in self.prev_conns])
        input += self.bias
        return input

    def activate(self):
        input = self.__get_input()
        self.value = self.__activation_function(input)

    def __activation_function(self, input) -> int:
        return max(0, input)

    def generate_prev_conns(self, prev_layer_nodes: List[Node]) -> None:
        """
        Connects the node to the nodes from the previous layer.
        """
        for prev_node in prev_layer_nodes:
            conn = Connection()
            self.add_prev_conn(conn)
            prev_node.add_next_conn(conn)
