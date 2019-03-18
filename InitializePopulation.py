import sys

import numpy as np

def InitializePopulation(populationSize, nGenes):
    "Initializes the population"
    population = np.zeros((populationSize, nGenes))

    for i in range(populationSize):
        for j in range(nGenes):
            s = np.random.rand()
            if s < 0.5:
                population[i, j] = 0
            else:
                population[i, j] = 1

    return population.astype(int)
