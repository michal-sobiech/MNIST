from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np
from typing import List
from Connection import Connection


class Node(ABC):
    value: int = None
    bias: float = None
    prev_conns: list[Connection] = []
    next_conns: list[Connection] = []

    def __init__(self) -> None:
        self.bias = np.random.uniform(-0.01, 0.01)

    def add_prev_conn(self, conn: Connection) -> None:
        self.prev_conns.append(conn)

    def __activation_function(self, input) -> int:
        return max(0, input)

    @abstractmethod
    def activate(self) -> None:
        pass

    @abstractmethod
    def __get_input(self) -> None:
        pass

    @abstractmethod
    def __generate_node(self) -> None:
        pass
