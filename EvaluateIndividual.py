def EvaluateIndividual(x):
    "Evaluates the fitness of the individual"
    gTerm1 = (x[0] + x[1] + 1)**2
    gTerm2 = 19 - 14*x[0] + 3*x[0]**2 - 14*x[1] + 6*x[0]*x[1] + 3*x[1]**2
    gTerm3 = (2*x[0] - 3*x[1])**2
    gTerm4 = 18 - 32*x[0] + 12*x[0]**2 + 48*x[1] - 36*x[0]*x[1] + 27*x[1]**2

    g = (1 + gTerm1*gTerm2)*(30 + gTerm3*gTerm4)
    f = 1/g
    return f
