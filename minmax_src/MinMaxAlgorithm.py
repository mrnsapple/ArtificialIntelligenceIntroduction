from ArtificialIntelligenceIntroduction.minmax_src.MinMaxProblem import MinMaxProblem
from ArtificialIntelligenceIntroduction.minmax_src.src.node import Node
from ArtificialIntelligenceIntroduction.minmax_src.src.problem import Problem
from ArtificialIntelligenceIntroduction.minmax_src.src.algorithm import Algorithm, AlgorithmException
import random
from enum import Enum
from typing import List
class NodeState(Enum):
    Max=1
    Min=2
    Final=3

class MinMaxAlgorithm(Algorithm):
    def __init__(self) -> None:
        self.depth = 4
        self.final_nodes = []
    
    """
    Get a successor for a given node until reached a final node in all branches
    
    @param problem:MinMaxProblem the problem to solve
    @param node:Node the node to find successors 
    """
    def addChild(self, problem: MinMaxProblem, node: Node):
        if not "node_state" in node.data:
            node.data["node_state"] = "min"
        if node.data["node_state"] is "final":
            self.final_nodes.append(node)
            return 
        problem.getSuccessors(node)
        [self.addChild(problem, child) for child in node.childs]
        return 

    """
    unused function-Check which node gives better heuristic

    """
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

    """
    Give the best successors for a set of nodes.
    
    @param problem:MinMaxProblem 
    @param nodes:List[Nodes] the nodes to find the best successors from
    """
    def get_successor(self, problem: MinMaxProblem, nodes: List[Node]) -> Node:
        if not nodes or not problem:
            raise AlgorithmException("Node or problem does not exist")
        self.final_nodes = []
        for node in nodes:
            self.addChild(problem,node)
        return self.final_nodes
