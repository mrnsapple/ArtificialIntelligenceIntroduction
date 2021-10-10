from ArtificialIntelligenceIntroduction.src.problem import Problem
import socket
import logging
from logging.handlers import RotatingFileHandler
import os
import json
import random

class RandomProblem(Problem):
    def __init__(self, algorithm_type=None, initial_state=None) -> None:
        super().__init__(algorithm_type=algorithm_type, initial_state=initial_state)

    def compare_with_desired_state(self, current):
        print("comparr with desired state")
        if current.tree_lvl > 0:
            return True
        return False    
      
    

