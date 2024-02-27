from numpy.typing import NDArray


class Sample:
    def __init__(self, input_values: NDArray,
                 expected_outcome: NDArray) -> None:
        self.input_values = input_values
        self.expected_output = expected_outcome
