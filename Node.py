from Connection import Connection
import numpy as np


class Node:
    bias: float = None
    prev_conns: list[Connection] = []
    next_conns: list[Connection] = []

    def __init__(self) -> None:
        self.bias = np.random.uniform(-0.01, 0.01)

    def add_prev_conn(self, conn: Connection) -> None:
        self.prev_conns.append(conn)

    def add_next_conn(self, conn: Connection) -> None:
        self.next_conns.append(conn)
