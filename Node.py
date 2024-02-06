from Connection import Connection


class Node:
    bias: float = None
    prev_conns: list[Connection] = []
    next_conns: list[Connection] = []

    def __init__(self, bias: float,
                 prev_conns: list[Connection],
                 next_conns: list[Connection]) -> None:
        self.bias = bias
        self.prev_conns = prev_conns
        self.next_conns = next_conns
