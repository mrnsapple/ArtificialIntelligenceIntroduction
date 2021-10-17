
import sys
sys.path.insert(0, '..')
sys.path.insert(0, '../..')
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