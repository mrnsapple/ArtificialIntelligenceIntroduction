from typing import List, Set
from ArtificialIntelligenceIntroduction.src.node import Node


class MinMaxProblemException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
      
class MinMaxProblem():
    
    def __init__(self) -> None:
        self.question_types = {
            "select position":self.select_positions,
            "select character":self.select_characters,
            "activate":self.activate_power,#boolean of yes or no do it
            "purple character power":self.activate_power,
            "brown character power":self.activate_power,
            "white character power move ":self.activate_power,
            "grey character power":self.activate_power,
            "blue character power room":self.activate_power,
            "blue character power exit":self.activate_power
        }

    
    def select_positions(self, node:Node):
        if node.parent.data["question type"] is not "select character":
            return
        #get character to move from parent
        parent_response_index = node.parent.data["response_index"]
        character_to_move = node.parent.data["data"][parent_response_index]
        #create a child node which each possible player move
        #update character position+change question+addresponse of position took in child
        for pos in node.data["data"]:
            child = Node(data=node.data["data"], parent=node, childs=[], tree_lvl=node.tree_lvl+1, is_visited=False)
            node.childs.append(child)
            for character_pos in range(child.data["characters"]):
                if child.data["characters"][character_pos]["color"] is character_to_move["color"]:
                    child.data["characters"][character_pos]["position"] = pos
                    child.data["response_index"] = pos
    
    def select_characters(self, node:Node):
        #heuristic for this fail
        print("in select_characters")
        pass
    
    def activate_power(self, node:Node):
        data = node.data["data"]

        print("in activate_power")
        pass
    

    def calculate_node_heuristic(self, node:Node):
        #calculate how many characters are alone and how many togheter
        game_state = node.data["game state"]
        characters = game_state["characters"]
        #Calculate locations of characters
        partition = [0]*10
        for i in range(10):
            for p in characters:
                if p["position"] == i:
                    partition[i] = partition[i]+1
        #Calculate number of characters alone
        number_characters_alone=0
        for p in partition:
            if p == 1:
                number_characters_alone+=1
        node.data["heuristic"] = number_characters_alone 
        #Determine if fantome is alone
        #if "fantome" in game_state:
        #    print("we are the fantome")
        
    def calculate_child_node_heuristic(self, node:Node):
            for child in node.childs:
                self.calculate_node_heuristic(child)
        
    

    def getSuccessors(self, node:Node):
        question_type = node.data["question type"]
        for question, function in self.question_types.items():
            if question in  question_type:
                function(node)
        self.calculate_child_node_heuristic(node)

    def compare_with_desired_state(self, current):
        print("comparr with desired state")
        if current.tree_lvl > 0:
            return True
        return False    
      
    
