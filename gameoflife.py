#Game of life
#let 1 represent a live cell and 0 represent a dead cell
#enter a game of life as an n x n numpy array
import numpy as np

seed = np.array([
        [1,1,1,0],
        [0,0,1,0],
        [0,0,0,0],
        [0,0,0,0]])

#A function to check if scenario 0 applies
def isscenario0(gameboard):
    if np.count_nonzero(gameboard) == 0:
        return True
    else:
        return False


#A function that produces a neighbours
def neighbours(gameboard):
    #initialise numpy array of zeros of same size as gameboard
    #will hold the number of neighbours each cell has
    neighbouringCells = np.zeros((np.size(gameboard,0),np.size(gameboard,1)))
    count = 0
    #iterate over the columns
    for j in range(np.size(gameboard,1)):
        #iterate over the rows
        for i in range(np.size(gameboard,0)):
            count += 1
            if gameboard[i,j] == 1:
                if i < np.size(gameboard,0):
                    neighbouringCells[i+1,j] += 1
                    if j < np.size(gameboard,1):
                        neighbouringCells[i+1, j+1] += 1
                    if j > 0:
                        neighbouringCells[i+1, j-1] += 1
                if j > 0:
                    neighbouringCells[i, j-1] += 1
                if j < np.size(gameboard,1):
                    neighbouringCells[i, j+1] += 1
                if i > 0:
                    neighbouringCells[i-1, j] += 1
                    if j > 0:
                        neighbouringCells[i-1, j-1] += 1
                    if j < np.size(gameboard,1):
                        neighbouringCells[i-1, j+1] += 1
    print(count)
    return neighbouringCells



print(neighbours(seed))
