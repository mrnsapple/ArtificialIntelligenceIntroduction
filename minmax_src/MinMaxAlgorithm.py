from ArtificialIntelligenceIntroduction.random_src.RandomProblem import RandomProblem
from ArtificialIntelligenceIntroduction.minmax_src.MinMaxProblem import MinMaxProblem
from ArtificialIntelligenceIntroduction.src.node import Node
from ArtificialIntelligenceIntroduction.src.problem import Problem
from ArtificialIntelligenceIntroduction.src.algorithm import Algorithm, AlgorithmException
import random
from enum import Enum
class NodeState(Enum):
    Max=1
    Min=2
    Final=3

class MinMaxAlgorithm(Algorithm):
    def __init__(self) -> None:
        self.depth = 4
        self.final_nodes = []
    
    #call again problem until reached a final node in all branches
    def addChild(self, problem: MinMaxProblem, node: Node):
        #check node is  final, meaning the node is end of current player turn
        if not "node_state" in node.data:
            node.data["node_state"] = "min"
        if node.data["node_state"] is "final":
            self.final_nodes.append(node)
            return 
        problem.getSuccessors(node)
        [self.addChild(child) for child in node.childs]
        return 

    #check which node gives better value either min or max and return it
    def get_best_choice(self, node):
        state = node.data["node_state"]
        if not self.final_nodes:
            return node
        best_node = self.final_nodes[0]
        for node in self.final_nodes:
            if state == "min" and node.data["heuristic"] < best_node:
                best_node = node
            elif state == "max" and node.data["heuristic"] > best_node:
                best_node = node
        return best_node

    #give the node that has the better result to throw in this turn calculating all best moves this player can do in the turn
    def get_successor(self, problem: MinMaxProblem, node: Node) -> Node:
        if not node or not problem:
            raise AlgorithmException("Node or problem does not exist")
        self.final_nodes = []
        self.addChild(problem,node)
        return self.get_best_choice(node)
