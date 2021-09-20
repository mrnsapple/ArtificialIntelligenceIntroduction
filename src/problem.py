
class ProblemException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        

class Problem():
    def __init__(self) -> None:
        pass