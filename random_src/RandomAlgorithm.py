from ArtificialIntelligenceIntroduction.random_src.RandomProblem import RandomProblem
from ArtificialIntelligenceIntroduction.minmax_src.MinMaxProblem import MinMaxProblem
from ArtificialIntelligenceIntroduction.src.node import Node
from ArtificialIntelligenceIntroduction.src.problem import Problem
from ArtificialIntelligenceIntroduction.src.algorithm import Algorithm, AlgorithmException
import random

class RandomAlgorithm(Algorithm):
    def get_successor(self, problem: Problem, node: Node) -> Node:
        if not node or not problem:
            raise AlgorithmException("Node or problem does not exist")
        data = node.data["data"]
        game_state =  node.data["game state"]
        #RandomProblem(problem).heuristic.checkNodeValue(node.data)
        response_index = random.randint(0, len(data)-1)
        return Node(data=response_index, parent=node, childs=[], tree_lvl=node.tree_lvl+1, is_visited=False)