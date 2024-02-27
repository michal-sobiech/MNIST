from __future__ import annotations
from abc import ABC
import numpy as np


class NodeABC(ABC):
    def __init__(self) -> None:
        self.bias: float = np.random.uniform(-0.01, 0.01)

    def activate(self, input_value) -> float:
        return self._activation_function(input_value)

    def _activation_function(self, input) -> int:
        return max(0, input)
