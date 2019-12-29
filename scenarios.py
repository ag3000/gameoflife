import numpy as np

# A function to check if scenario 0 applies
def isNoInteraction(gameboard):
    if np.count_nonzero(gameboard) == 0:
        return True
    else:
        return False

# scenario 1
def underPopulation(numberOfNeighbours):
    if numberOfNeighbours < 2:
        return True
    else:
        return False

# scenario 2
def overCrowding(numberOfNeighbours):
    if numberOfNeighbours > 3:
        return True
    else:
        return False

# scenario 3
def survival(numberOfNeighbours):
    if numberOfNeighbours == 2 or numberOfNeighbours == 3:
        return True
    else:
        return False

# scenario 4
def creationOfLife(numberOfNeighbours):
    if numberOfNeighbours == 3:
        return True
    else:
        return False
