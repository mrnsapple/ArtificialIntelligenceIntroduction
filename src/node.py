
class NodeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        

class Node():
    def __init__(self, data=None, parent=None, childs=[], tree_lvl=0, is_visited=False) -> None:
        self._data = data
        self.parent = parent
        self.childs = childs
        self.tree_lvl = 0
        self.is_visited = False

    def has_parent(self) -> bool:
        return True if self.parent else False
        
    
    def remove_child(self, node: None) -> None:
        self.childs.remove(node)

    def add_child(self, node: None) -> None:
        self.childs.append(node)
    
    @property
    def data(self, data) -> None:
        self._data = data
    
    @data.setter
    def data(self, data):
        return self._data
    
    @staticmethod
    def make_node(data, parent):
        return Node(data=data,parent=parent, childs=[], tree_lvl=0, is_visited=False)
    
    def __EQ__(self, other):
        if self._data == other._data:
            return True
        return False
