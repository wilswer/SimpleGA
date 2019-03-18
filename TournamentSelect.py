import numpy as np

def TournamentSelect(fitness, tournamentSelectionParameter, tournamentSize):
    "Selects an individual using tournament selection"

    populationSize = fitness.size
    iTmp = np.round(np.random.rand(tournamentSize)*(populationSize - 1)).astype(int)
    iTmpFitness = fitness[iTmp]
    sortedFitness = np.argsort(iTmpFitness)[::-1]
    sortedFitnessIndex = iTmp[sortedFitness]
    iSelected = sortedFitnessIndex[-1]
    for i in range(tournamentSize):
        r = np.random.rand()
        if r < tournamentSelectionParameter:
            iSelected = sortedFitnessIndex[i]
            break
            
    return iSelected
