import numpy as np

def DecodeChromosome(chromosome, numberOfVariables, variableRange):
    "Decodes the chromosome"
    nGenes = chromosome.size
    kGroups = int(nGenes/numberOfVariables)
    x = np.zeros(numberOfVariables)

    for i in range(numberOfVariables):
        kGroupLimit = i*kGroups
        for j in range(kGroups):
            x[i] = x[i] + chromosome[j + kGroupLimit]*(2**(-j - 1))
        x[i] = -variableRange + 2*variableRange*x[i]/(1 - 2**(-kGroups))

    return x
