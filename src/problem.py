
#import ArtificialIntelligenceIntroduction.src.algorithm 
import abc
from ArtificialIntelligenceIntroduction.src.node import Node

class ProblemException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        

class Problem():
    def __init__(self, algorithm_type=None, initial_state= None) -> None:
        self.initial_state = initial_state
        self.algorithm_type = algorithm_type

    @abc.abstractmethod
    def compare_with_desired_state(self, current:Node):
        return False
