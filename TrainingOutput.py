from typing import List
from numpy.typing import NDArray


class TrainingOutput:
    def __init__(self, layers_act_vals: List[NDArray]) -> None:
        self.layers_act_vals = layers_act_vals
        self.