from ArtificialIntelligenceIntroduction.src.node import Node


class MinMaxProblemException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
      
class MinMaxProblem():
    def __init__(self) -> None:
        pass

    def checkNodeValue(self, data):
        print(data)

    def getSuccessors(self, node:Node):
        pass

