import numpy as np
import pygame, sys
from pygame.locals import *
import scenarios

# If the neighbouring cell is 1 then add 1 to the counter
def addNeighbour(neighbouringCell, numberOfNeighbours):
    if neighbouringCell == 1:
        numberOfNeighbours += 1
    return numberOfNeighbours

# Returns a count of all living neighbouring cells
def calcNumberOfNeighbours(i, j, gameboard):
    numberOfNeighbours = 0
    numberOfRows = np.size(gameboard,0)
    numberOfColumns = np.size(gameboard,1)

    # Count southern neighbour
    if i < numberOfRows - 1:
        numberOfNeighbours = addNeighbour(gameboard[i+1, j], numberOfNeighbours)
        # Count southeastern neighbour
        if j < numberOfColumns - 1:
            numberOfNeighbours = addNeighbour(gameboard[i+1, j+1], numberOfNeighbours)
        # Count southwestern neighbour
        if j > 0:
            numberOfNeighbours = addNeighbour(gameboard[i+1, j-1], numberOfNeighbours)
    # Count western neighbour
    if j > 0:
        numberOfNeighbours = addNeighbour(gameboard[i, j-1], numberOfNeighbours)
    # Count eastern neighbour
    if j < numberOfColumns - 1:
        numberOfNeighbours = addNeighbour(gameboard[i, j+1], numberOfNeighbours)
    # Count northern neighbour
    if i > 0:
        numberOfNeighbours = addNeighbour(gameboard[i-1, j], numberOfNeighbours)
        if j > 0:
            # Count northwestern neighbour
            numberOfNeighbours = addNeighbour(gameboard[i-1, j-1], numberOfNeighbours)
            # Count northeastern neighbour
        if j < numberOfColumns - 1:
            numberOfNeighbours = addNeighbour(gameboard[i-1, j+1], numberOfNeighbours)

    return numberOfNeighbours

# Takes a cell in the gameboard and calculates its new state depending on it's number of neighbours
def calcNewCellState(i, j, gameboard):
    numberOfNeighbours = calcNumberOfNeighbours(i, j, gameboard)

    if gameboard[i, j] == 1:
        if scenarios.underPopulation(numberOfNeighbours) or scenarios.overCrowding(numberOfNeighbours) or not scenarios.survival(numberOfNeighbours):
            newState = 0
        else:
            newState = 1
    else:
        if scenarios.creationOfLife(numberOfNeighbours):
            newState = 1
        else:
            newState = 0

    return newState

# Returns the next step in the game of life by iterating through each cell
def nextState(gameboard):
    numberOfRows = np.size(gameboard,0)
    numberOfColumns = np.size(gameboard,1)
    newboard = np.zeros((numberOfRows, numberOfColumns), dtype = int)
    # Iterate through array
    for i in range(numberOfRows):
        for j in range(numberOfColumns):
            newboard[i, j] = calcNewCellState(i, j, gameboard)

    return newboard

##
## Rendering
##

def renderArray(gameboard, display):
    white = (255, 255, 255)
    black = (0, 0, 0)

    screenWidth, screenHeight = pygame.display.get_surface().get_size()
    numberOfRows = np.size(gameboard, 0)
    numberOfColumns = np.size(gameboard, 1)
    cellWidth = screenWidth / numberOfColumns
    cellHeight = screenHeight / numberOfRows
    cellSize = min(cellWidth, cellHeight)

    for i in range(numberOfRows):
        for j in range(numberOfColumns):
            positionx = i * cellSize
            positiony = j * cellSize

            if gameboard[i, j] == 1:
                pygame.draw.rect(display, white, (positionx, positiony, cellSize, cellSize))
            else:
                pygame.draw.rect(display, black, (positionx, positiony, cellSize, cellSize))


def renderGameOfLife(seed, numberOfIterations):
    pygame.init()
    display = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Game of life animation')

    # Draw game board
    for i in range(numberOfIterations):
        if scenarios.isNoInteraction(seed):
            renderArray(seed,display)
            font = pygame.font.Font(None, 36)
            text_surface = font.render("No interactions", 1, (255, 255, 255))
            display.blit(text_surface, (0, 0))
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.display.quit()
            pygame.quit()
            sys.exit()
            return

        # close game when user quits
        elif pygame.event.peek(eventtype = QUIT):
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        else:
            renderArray(seed,display)
            seed = nextState(seed)
            pygame.time.delay(1000)
            pygame.display.update()


def main():
    # Initial State
    seed = np.array([
            [1,0,1,0,0,0,1,0],
            [0,0,1,0,0,0,1,0],
            [1,0,1,0,0,0,1,0],
            [1,0,0,1,0,0,1,0],
            [0,0,1,0,0,0,1,0],
            [0,0,1,0,0,0,1,0],
            ])

    renderGameOfLife(seed, 15)

if __name__ == "__main__":
    main()
