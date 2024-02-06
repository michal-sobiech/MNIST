from Layer import Layer


class FeedforwardNN:
    layers: list[Layer] = []

    def __init__(self, layers: list[Layer]) -> None:
        self.layers = layers