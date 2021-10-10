

class NodeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)    
class Node():
    """
    Class with the necessary information to represent a node in the tree search
    """

    """
    @param data:Dict data that this node will hold
    @param parent:Node the parent of the current node
    @param childs:Node[] the childs of the current node
    @param tree_lvl:int the level of the tree this node belongs to
    @param is_visited:bool if the node has been visited
    @return None
    """
    def __init__(self, data=None, parent=None, childs=[], tree_lvl=0, is_visited=False) -> None:
        #value of the node
        self.data = data
        self.parent = parent
        self.childs = childs
        self.tree_lvl = tree_lvl
        self.is_visited = is_visited
       

    """
    wheter the current node has a parent

    @return bool wheter the current node has a parent
    """
    def has_parent(self) -> bool:
        return True if self.parent else False
        
    """
    Remove a child from the current node

    @param node:Node the child to remove from the current node
    @return bool if the child has been correctly removed
    """
    def remove_child(self, node: None) -> None:
        if not node:
            return False
        self.childs.remove(node)
        return True


    """
    Add a child to the node
    @param node:Node child to add
    @return bool if the child has been added correctly
    """
    def add_child(self, node: None) -> None:
        if not node:
            return False
        self.childs.append(node)
        return True

    
    #@staticmethod
    #def make_node(data, parent:Node):
    #    return Node(data=data,parent=parent, childs=[], tree_lvl=parent.tree_level+1, is_visited=False)
    
    """
    Override __EQ__ function to check if 2 nodes are equal comparint it's data only
    @param other:Node the node to check with current node
    @return if the nodes are equal
    """
    def __EQ__(self, other):
        if self._data == other._data:
            return True
        return False
