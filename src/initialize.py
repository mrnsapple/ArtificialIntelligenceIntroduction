from ArtificialIntelligenceIntroduction.src.problem import Problem
from ArtificialIntelligenceIntroduction.src.tree_search import TreeSearch
from ArtificialIntelligenceIntroduction.src.algorithm import Algorithm, AlgorithmType


class InitializeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
class Initialize():
    def __init__(self, algorithm_type:AlgorithmType, problem:Problem, algorithm:Algorithm) -> None:
        self.algorithm_type =algorithm_type
        self.problem = problem
        self.algorithm = algorithm
        self.tree = TreeSearch()

    def launch_tree(self):
        self.tree.tree_search(self.problem, self.algorithm)