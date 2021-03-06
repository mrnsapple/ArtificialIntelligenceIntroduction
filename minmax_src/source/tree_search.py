
from minmax_src.source.algorithm import Algorithm
from minmax_src.source.problem import Problem
from minmax_src.source.node import Node
import minmax_src.globals as globals


class TreeSearchException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class TreeSearch():
    """
    Class containing the logic for generate a tree search that will return a node given a specific problem and algorithm
    """
    
    """
    @param: weather we use graph_search or tre search
    @return None
    """
    def __init__(self, use_graph_search=False) -> None:
        self.use_graph_search = use_graph_search        

    """
    Generate the tree search that solves the given problem using the given algorithm
    
    @param problem:Problem problem to solve
    @param algorith:Algorithm algorithm to use to solve problem
    @return Node the result node from the tree search
    """
    def tree_search(self, problem: Problem, algorithm:Algorithm):
        if not problem or not algorithm:
            raise(TreeSearchException("Problem or Algorithm are empty"))
        n = [problem.initial_state]
        iteration = 0
        
        while (n):
            result = problem.compare_with_desired_state(n)
            if result or iteration > globals.max_iterations:
                return result
            n = algorithm.get_successor(problem, n)
            if not n:
                raise(TreeSearchException("No solution found"))
            iteration+=1
        return None
        
