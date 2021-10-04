
from ArtificialIntelligenceIntroduction.src.problem import Problem
from ArtificialIntelligenceIntroduction.src.node import Node
import abc
from enum import Enum
class AlgorithmType(Enum):
    MinMax=1
    Random=2
class AlgorithmException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        

class Algorithm():
    """
    All logic for the specific algorithm used to move in the tree search.
    It’s generic and can be used to solve any kind of problem
    """
    
    """
    @return None
    """
    def __init__(self) -> None:
        pass

    """
    Given a node, it will create and return the child node with best heuristic value
    
    @param problem:Problem The problem containing specific information about the problem to solve
    @param node:Node current node in the search tree
    @return the child node with best heuristic value 
    """
    @abc.abstractmethod
    def get_successor(self, problem:Problem, node:Node) -> Node:
        return