from node.NodeABC import NodeABC


class InputNode(NodeABC):
    def __init__(self) -> None:
        super().__init__()

    def activate(self, input_value) -> None:
        self.value = self.__activation_function(input_value)
