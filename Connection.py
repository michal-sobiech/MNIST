import numpy as np


class Connection:
    weight: float = None

    def __init__(self) -> None:
        self.weight = np.random.uniform(-0.1, 0.1)
