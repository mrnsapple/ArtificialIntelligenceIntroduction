
#import ArtificialIntelligenceIntroduction.src.algorithm 
import abc
from ArtificialIntelligenceIntroduction.src.node import Node

class ProblemException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        

class Problem():
    """
    Logics that are specific for each problem to be solve
    """

    """
    @param intial_state Initial state at which the algorithm start
    @return nNone
    """
    def __init__(self, initial_state= None) -> None:
        self.initial_state = initial_state


    """
    Compare node with desired state.
    Determine if curre

    """
    @abc.abstractmethod
    def compare_with_desired_state(self, current:Node):
        return False
