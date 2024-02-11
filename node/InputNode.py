from node.NodeABC import NodeABC
from Connection import Connection


class InputNode(NodeABC):
    def __init__(self) -> None:
        super().__init__()

    def add_next_conn(self, conn: Connection) -> None:
        self.next_conns.append(conn)

    def activate(self, input_value) -> None:
        self.value = self.__activation_function(input_value)
