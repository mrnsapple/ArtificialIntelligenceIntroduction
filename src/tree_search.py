
from ArtificialIntelligenceIntroduction.src.algorithm import Algorithm
from ArtificialIntelligenceIntroduction.src.problem import Problem
from ArtificialIntelligenceIntroduction.src.node import Node


class TreeSearchException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class TreeSearch():
    def __init__(self, visited_states=[], use_graph_search=False) -> None:
        self.visited_states = visited_states
        self.use_graph_search = use_graph_search        

    def tree_search(self, problem: Problem, algorithm:Algorithm):
        if not problem or not algorithm:
            raise(TreeSearchException("Problem or Algorithm are empty"))
        n = problem.initial_state
        while (n):
            if problem.compare_with_desired_state(n):
                return n
            n = algorithm.get_successor(problem, n)
            if not n:
                raise(TreeSearchException("No solution found"))
        return None
        print("SOLUTION FOUND")
         
    
    def check_node(self, node:Node):
        return True if node in self.visited_states else False
    
 