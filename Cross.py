import numpy as np

def Cross(chromosome1,chromosome2):
    "Preforms one-point crossover"
    nGenes = chromosome1.size

    crossoverPoint = np.round(np.random.rand()*(nGenes - 1) - 1).astype(int)
    newChromosomePair = np.zeros((2,nGenes))

    for j in range(nGenes):
        if j <= crossoverPoint:
            newChromosomePair[0,j] = chromosome1[j]
            newChromosomePair[1,j] = chromosome2[j]
        else:
            newChromosomePair[0,j] = chromosome2[j]
            newChromosomePair[1,j] = chromosome1[j]

    return newChromosomePair
