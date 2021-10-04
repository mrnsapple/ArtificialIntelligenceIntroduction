from src.algorithm import Algorithm
from src.node import Node

class MinMax(Algorithm):
    def __init__(self) -> None:
        self.minimisernode = ["1", "2"]
        self.maximisernode = ["0"]
    
    def CompareNodeMin(self, nodes):
        minNode = nodes[0]
        for node in nodes:
            if (minNode > node):
                minNode = node
        return node
            
        
    def CompareNodeMax(self, nodes):
        maxNode = nodes[0]
        for node in nodes:
            if (maxNode < node):
                maxNode = node
        return maxNode
    
    def algo(self, node: Node):
        next_values = list()
        
        if node.tree_lvl not in self.minimisernode and node.tree_lvl not in self.maximisernode:
            return node.data
        
        if node.tree_lvl in self.minimisernode:
            for next_node in node.childs:
                next_values.append(self.algo(next_node))
            nodeValue = self.CompareNodeMin(next_values)
            return nodeValue
            
        if node.tree_lvl in self.maximisernode:
            for next_node in node.childs:
                next_values.append(self.algo(next_node))
            nodeValue = self.CompareNodeMax(next_values)
            return nodeValue