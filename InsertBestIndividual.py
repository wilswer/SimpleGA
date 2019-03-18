import numpy as np

def InsertBestIndividual(population, bestIndividual, numberOfCopies):
    "Inserts numberOfCopies number of best individuals in the population"
    newPopulation = population.copy()

    for i in range(numberOfCopies):
        newPopulation[i,:] = bestIndividual

    return newPopulation
