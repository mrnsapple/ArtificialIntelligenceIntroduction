
import sys
import os
#os.chdir('../')

path = os.getcwd()
sys.path.append(os.getcwd())
sys.path.append("/home/oriol/Epitech_projects/5_Year/AI")

sys.path.append("/home/oriol/Epitech_projects/5_Year/AI/ArtificialIntelligenceIntroduction")
##
print(path)
from ArtificialIntelligenceIntroduction.src.initialize import Initialize

from ArtificialIntelligenceIntroduction.minmax_src.MinMaxAlgorithm import MinMaxAlgorithm
from ArtificialIntelligenceIntroduction.minmax_src.MinMaxProblem import MinMaxProblem
from ArtificialIntelligenceIntroduction.random_src.RandomAlgorithm import RandomAlgorithm
from ArtificialIntelligenceIntroduction.random_src.RandomProblem import RandomProblem
from ArtificialIntelligenceIntroduction.src.algorithm import AlgorithmType

def main():
    initialize = Initialize(AlgorithmType.MinMax, MinMaxProblem(), MinMaxAlgorithm()) 
    initialize.run()  
 

main()