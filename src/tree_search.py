
from ArtificialIntelligenceIntroduction.src.node import Node


class TreeSearchException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class TreeSearch():
    def __init__(self, algorithm_type=None, initial_state=None, desired_state=None, visited_states=[], use_graph_search=False) -> None:
        self.algorithm_type = algorithm_type
        self.initial_state = initial_state
        self.desired_state = desired_state
        self.visited_states = visited_states
        self.use_graph_search = use_graph_search        

    
    def check_node(self, node:Node):
        return True if node in self.visited_states else False
    
 