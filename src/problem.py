
class ProblemException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        

class Problem():
    def __init__(self, algorithm_type=None, initial_state=None, desired_state=None) -> None:
        self.initial_state = initial_state
        self.desired_state = desired_state
        self.algorithm_type = algorithm_type

        pass