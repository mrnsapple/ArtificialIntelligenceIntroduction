
import sys
sys.path.insert(0, '..')
sys.path.insert(0, '../..')
from minmax_src.source.initialize import Initialize

from minmax_src.MinMaxAlgorithm import MinMaxAlgorithm
from minmax_src.MinMaxProblem import MinMaxProblem
from minmax_src.source.algorithm import AlgorithmType

def main():
    initialize = Initialize(AlgorithmType.Random, MinMaxProblem(), MinMaxAlgorithm()) 
    initialize.run()  
 

main()