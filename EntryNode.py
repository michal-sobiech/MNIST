from Node import Node


class EntryNode(Node):
    def __init__(self) -> None:
        super().__init__()

    # Overriden method
    def activate(self, input_value) -> None:
        self.value = self.__activation_function(input_value)
