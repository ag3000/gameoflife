#Game of life
#let 1 represent a live cell and 0 represent a dead cell
#enter a game of life as an n x m numpy array
import numpy as np

seed = np.array([
        [1,0,1,0,0,0,1,0],
        [0,0,1,0,0,0,1,0],
        [1,0,1,0,0,0,1,0],
        [1,0,0,1,0,0,1,0],
        [0,0,1,0,0,0,1,0],
        [0,0,1,0,0,0,1,0],
        ])

#A function to check if scenario 0 applies
def isNoInteraction(gameboard):
    if np.count_nonzero(gameboard) == 0:
        return True
    else:
        return False

#scenario1
def underPopulation(numberOfNeighbours):
    if numberOfNeighbours < 2:
        return True
    else:
        return False

#scenario2
def overCrowding(numberOfNeighbours):
    if numberOfNeighbours > 3:
        return True
    else:
        return False

#scenario3
def survival(numberOfNeighbours):
    if numberOfNeighbours == 2 or numberOfNeighbours == 3:
        return True
    else:
        return False

#scenario4
def creationOfLife(numberOfNeighbours):
    if numberOfNeighbours == 3:
        return True
    else:
        return False

#If the neighbouring cell is 1 then add 1 to the counter
def addNeighbour(neighbouringCell, numberOfNeighbours):
    if neighbouringCell == 1:
        numberOfNeighbours += 1
    return numberOfNeighbours

def calcNewCellState(i, j, gameboard):
    numberOfNeighbours = 0
    numberOfRows = np.size(gameboard,0)
    numberOfColumns = np.size(gameboard,1)
    #count southern neighbour
    if i < numberOfRows - 1:
        numberOfNeighbours = addNeighbour(gameboard[i+1,j],numberOfNeighbours)
        #count southeastern neighbour
        if j < numberOfColumns - 1:
            numberOfNeighbours = addNeighbour(gameboard[i+1,j+1],numberOfNeighbours)
        #count southwestern neighbour
        if j > 0:
            numberOfNeighbours = addNeighbour(gameboard[i+1,j-1],numberOfNeighbours)
    #count west neighbour
    if j > 0:
        numberOfNeighbours = addNeighbour(gameboard[i,j-1],numberOfNeighbours)
    #count east neighbour
    if j < numberOfColumns - 1:
        numberOfNeighbours = addNeighbour(gameboard[i,j+1],numberOfNeighbours)
    #count northern neighbour
    if i > 0:
        numberOfNeighbours = addNeighbour(gameboard[i-1,j],numberOfNeighbours)
        if j > 0:
            #count northwestern neighbour
            numberOfNeighbours = addNeighbour(gameboard[i-1,j-1],numberOfNeighbours)
            #count northeastern neighbour
        if j < numberOfColumns - 1:
            numberOfNeighbours = addNeighbour(gameboard[i-1,j+1],numberOfNeighbours)

    if gameboard[i,j] == 1:
        if underPopulation(numberOfNeighbours) or overCrowding(numberOfNeighbours) or not survival(numberOfNeighbours):
            newState = 0
        else:
            newState = 1
    else:
        if creationOfLife(numberOfNeighbours):
            newState = 1
        else:
            newState = 0

    return newState


def nextState(gameboard):
    newboard = np.zeros((np.size(gameboard,0),np.size(gameboard,1)),dtype = int)
    #iterate over the rows
    for i in range(np.size(gameboard,0)):
        for j in range(np.size(gameboard,1)):
            newboard[i,j] = calcNewCellState(i,j, gameboard)

    return newboard

for i in range(10):
    print(seed)
    seed = nextState(seed)
    print("\n")
