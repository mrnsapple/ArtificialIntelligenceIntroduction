
#import minmax_src.source.algorithm 
import abc
from minmax_src.source.node import Node
from typing import List

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
    def compare_with_desired_state(self, node:List[Node]):
        return False
