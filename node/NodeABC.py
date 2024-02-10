from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np
from Connection import Connection


class NodeABC(ABC):
    def __init__(self) -> None:
        self.value: int = None
        self.bias: float = None
        self.prev_conns: list[Connection] = []
        self.next_conns: list[Connection] = []
        self.bias = np.random.uniform(-0.01, 0.01)

    def add_next_conn(self, conn: Connection) -> None:
        self.next_conns.append(conn)

    def _activation_function(self, input) -> int:
        return max(0, input)
