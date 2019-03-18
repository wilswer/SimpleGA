import numpy as np
from InitializePopulation import InitializePopulation
from DecodeChromosome import DecodeChromosome
from EvaluateIndividual import EvaluateIndividual
from TournamentSelect import TournamentSelect
from Cross import Cross
from Mutate import Mutate
from InsertBestIndividual import InsertBestIndividual

populationSize = 100
numberOfGenes = 50
crossoverProbability = 0.5
mutationProbability = 0.02
tournamentSelectionParameter = 0.75
tournamentSize = 2
variableRange = 10
numberOfGenerations = 100
numberOfVariables = 2
numberOfCopies = 1

fitness = np.zeros(populationSize)

population = InitializePopulation(populationSize, numberOfGenes)
maximumFitness = 0
for iGeneration in range(numberOfGenerations):
    bestIndividualIndex = 0
    for i in range(populationSize):
        chromosome = population[i,:]
        x = DecodeChromosome(chromosome, numberOfVariables, variableRange)
        fitness[i] = EvaluateIndividual(x)
        if fitness[i] > maximumFitness:
            maximumFitness = fitness[i]
            bestIndividualIndex = i
            xBest = x.copy()
            print(maximumFitness)

    tempPopulation = population.copy()

    for i in range(0, populationSize, 2):
        i1 = TournamentSelect(fitness, tournamentSelectionParameter, tournamentSize)
        i2 = TournamentSelect(fitness, tournamentSelectionParameter, tournamentSize)
        chromosome1 = population[i1,:]
        chromosome2 = population[i2,:]

        r = np.random.rand()
        if r < crossoverProbability:
            newChromosomePair = Cross(chromosome1, chromosome2)
            tempPopulation[i,:] = newChromosomePair[0,:]
            tempPopulation[i+1,:] = newChromosomePair[1,:]
        else:
            tempPopulation[i,:] = chromosome1
            tempPopulation[i+1,:] = chromosome2

    for i in range(populationSize):
        originalChromosome = tempPopulation[i,:]
        mutatedChromosome = Mutate(originalChromosome, mutationProbability)
        tempPopulation[i,:] = mutatedChromosome

    bestIndividual = population[bestIndividualIndex,:]
    population = InsertBestIndividual(tempPopulation, bestIndividual, numberOfCopies)

print("Minimum function value " + str(np.round(1/maximumFitness,decimals = 3)) + " at point " + str(np.round(xBest,decimals = 3)))
