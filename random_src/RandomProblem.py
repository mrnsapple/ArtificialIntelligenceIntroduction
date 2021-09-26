from ArtificialIntelligenceIntroduction.src.problem import Problem
import socket
import logging
from logging.handlers import RotatingFileHandler
import os
import json
import random

class RandomProblem(Problem):
    def compare_with_desired_state(self, current):
        print("comparr with desired state")
        if current.tree_lvl > 0:
            return True
        return False    
      
    

