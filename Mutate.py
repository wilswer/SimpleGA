import numpy as np

def Mutate(chromosome, mutationProbability):
    "Mutates the chromosome"

    nGenes = chromosome.size

    mutatedChromosome = chromosome.copy()

    for i in range(nGenes):
        r = np.random.rand()
        if r < mutationProbability:
            mutatedChromosome[i] = 1 - chromosome[i]
    return mutatedChromosome
