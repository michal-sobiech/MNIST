from typing import List
from node.NonfirstNode import NonfirstNodeABC
from Connection import Connection


class MiddleNode(NonfirstNodeABC):
    def __init__(self) -> None:
        super().__init__()

    def add_prev_conn(self, conn: Connection) -> None:
        self.prev_conns.append(conn)
