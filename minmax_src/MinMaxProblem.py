from typing import Dict, List, Set
from ArtificialIntelligenceIntroduction.minmax_src.source.node import Node
from ArtificialIntelligenceIntroduction.minmax_src import globals


class MinMaxProblemException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
      
class MinMaxProblem():
    
    def __init__(self, initial_state:Node= None) -> None:
        self.question_types = {
            #"select position":self.select_positions,
            "select character":self.select_characters,
            #"activate":self.activate_power,#boolean of yes or no do it
            #"purple character power":self.activate_power,
            #"brown character power":self.activate_power,
            #"white character power move ":self.activate_power,
            #"grey character power":self.activate_power,
            #"blue character power room":self.activate_power,
            #"blue character power exit":self.activate_power
        }
        self.initial_state = initial_state
        if self.initial_state:
            self.initial_state.data["node_state"] = "min"
        self.tree_lvl = 1
        self.iteration = 0
        self.moves_to_play=[]


    def select_positions(self, node:Node):
        if node.parent.data["question type"] is not "select character":
            return
        #get character to move from parent
        parent_response_index = node.parent.data["response_index"]
        character_to_move = node.parent.data["data"][parent_response_index]
        #create a child node which each possible player move
        #update character position+change question+addresponse of position took in child
        for pos in node.data["data"]:
            child = Node(data=node.data.copy(), parent=node, childs=[], tree_lvl=node.tree_lvl+1, is_visited=False)
            node.childs.append(child)
            for character_pos in range(child.data["characters"]):
                if child.data["characters"][character_pos]["color"] is character_to_move["color"]:
                    child.data["characters"][character_pos]["position"] = pos
                    child.data["response_index"] = pos
                    child.data["question type"] = ""#check which player is
    
    def select_characters(self, node:Node):
        if "response_index" in node.data:       
            if not self.activate_power(node, globals.before, node.data["data"][node.data["response_index"]]):
                #select positions after activate power
                self.activate_power(node, globals.after, node.data["data"][node.data["response_index"]])
                #self.select_positions(node.data["response_index"]) 
            #else:
                #select positions without activate power, power activations will be called 
            #    self.select_positions(child) 
        else:
            #its initial node
            characters = node.data["data"]
            index = 0
            for character_pos in range(len(characters)):
                character = characters[character_pos]
                child = Node(data=node.data.copy(), parent=node, childs=[], tree_lvl=node.tree_lvl+1, is_visited=False)
                node.childs.append(child)
                child.data["response_index"] = character_pos
                    
    def activate_power(self, node:Node, activables, character):
        if not character["color"] in activables:
            return False 
        for i in range(2):
            child = Node(data=node.data.copy(), parent=node, childs=[], tree_lvl=node.tree_lvl+1, is_visited=False)
            node.childs.append(child)
            child.data["question type"] = "activate {} power".format(character["color"])
            child.data["data"] = [0,1]
            child.data["node_state"] = "final"
            child.data["response_index"] = i
            #print("response index:{}".format(i))
        #print("in activate_power")
        return True
    
    """
    Calculate node heuristic
    To do->should be the sum of previous nodes corresponding to the same turn heuristics

    @param node:Node
    """
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

    def get_instructions(self, node:Node):
        if not node or not "response_index" in node.data  or node.parent is self.initial_state:
            return self.moves_to_play
        if node.data["game state"]["num_tour"] == self.initial_state.data["game state"]["num_tour"]:
            self.moves_to_play.append(node.data["response_index"])
        self.get_instructions(node.parent)

    def compare_with_desired_state(self, nodes:List[Node]):
        chosen_node=None
        self.moves_to_play=[]
        for node in nodes:
            if node.tree_lvl >= self.tree_lvl+ self.initial_state.tree_lvl:# + self.initial_state.data["game state"]["num_tour"]:
                chosen_node = node
        self.get_instructions(chosen_node)    
        return self.moves_to_play
    
