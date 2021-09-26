
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
        pass
    
    def check_node(self, node:Node):
        return True if node in self.visited_states else False
    
 