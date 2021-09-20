
from ArtificialIntelligenceIntroduction.src.problem import Problem
from ArtificialIntelligenceIntroduction.src.node import Node
import abc


class AlgorithmException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        

class Algorithm():
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def get_successor(problem:Problem, node:Node) -> Node:
        return