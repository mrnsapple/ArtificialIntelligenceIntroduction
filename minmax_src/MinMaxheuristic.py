from ArtificialIntelligenceIntroduction.src.node import Node


class MinMaxHeuristicException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
      
class MinMaxHeuristic():
    def __init__(self) -> None:
        pass

    def checkNodeValue(self, data):
        print(data)

    def getSuccessors(self, node:Node):
        pass

