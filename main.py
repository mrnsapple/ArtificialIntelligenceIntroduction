

import sys
import os
os.chdir('../')
path = os.getcwd()
sys.path.append(os.getcwd())
##
from ArtificialIntelligenceIntroduction.src.initialize import Initialize

def main():
    initialize = Initialize(None, None, None) 
    initialize.launch_tree()  
 

main()