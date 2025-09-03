import pygame
import sys

pygame.init()

screenWidth = 1800
screenHeight = 1000
screen = pygame.display.set_mode((screenWidth, screenHeight))
center = screen.get_size()
TestSurface = pygame.Surface((500, 500))

clock = pygame.time.Clock()
isRunning = True



automataAmountX = 75
automataAmountY = 75
padding = 1
automataWidth = 15
automataHeight = 15
automataRect = (automataWidth, automataHeight)

arrayWidth = (automataWidth * automataAmountX) + (padding * automataAmountX)
arrayHeight = (automataHeight * automataAmountY) + (padding * automataAmountY)

centerOfScreenAndArray = (screenWidth / 2 - arrayWidth / 2, screenHeight / 2 - arrayHeight / 2)
drawingSurface = pygame.Surface((arrayWidth,arrayHeight))


def createAutomataArray():
    global grid
    grid = []
    for i in range(automataAmountY):
        row = []
        for j in range(automataAmountX):
            automataPosX = j * (automataWidth + padding) + 10
            automataPosY = i * (automataHeight + padding) + 10
            rect = pygame.Rect(automataPosX, automataPosY, automataWidth, automataHeight)
            row.append([rect, False])
        grid.append(row)
    return grid


def drawAutomataArray(grid):
    drawingSurface.fill((0, 0, 0)) 
    global rectArray
    rectArray = []
    for row in grid:
        for rect, alive in row:
            pygame.draw.rect(screen, (80, 80, 80), rect, width=1)
            if alive:
                drawnRect = pygame.draw.rect(screen, "White", rect)
                rectArray.append(drawnRect)

def drawAutomataArrayToTestSurface(arr):
    for arrRect, boolVal in arr:
        if boolVal == True:
            pygame.draw.rect(TestSurface, "White", arrRect, width=1)

neighbourArray = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

def resetArray(arr):
    resetArr = []
    for row in arr:
        returnRow = []
        for rect, boolVal in row:
            if boolVal:
                boolVal = False
                returnRow.append([rect, boolVal])
            else:
                returnRow.append([rect, boolVal])
        resetArr.append(returnRow)
    return resetArr

def validateAutomataArray(grid):
    newGrid = []
    for row in range(automataAmountY):
        newRow = []
        for col in range(automataAmountX):
            rect, alive = grid[row][col]
            neighbours = 0

            for rowOffset, columnOffset in neighbourArray:
                neighbourRow, neighbourColumn = row + rowOffset, col + columnOffset
                if 0 <= neighbourRow < automataAmountY and 0 <= neighbourColumn < automataAmountX:
                    if grid[neighbourRow][neighbourColumn][1]:
                        neighbours += 1

            if alive and (neighbours < 2 or neighbours > 3):
                newAlive = False
            elif not alive and neighbours == 3:
                newAlive = True
            else:
                newAlive = alive

            newRow.append([rect, newAlive])
        newGrid.append(newRow)
    return newGrid


automataArray = createAutomataArray()

drawAutomataArray(automataArray)


# def printArray(string, arr):
#     print(f"Array {string}: ")
#     for item in range(0, len(arr), automataAmountX):
#         print(arr[item:item + automataAmountX])


#printArray("before", automataArray)


isDrawing = False
DRAW_EVENT = pygame.event.custom_type()

while isRunning:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_SPACE:
                if isDrawing:
                    pygame.time.set_timer(DRAW_EVENT, 0)
                    isDrawing = False
                else:
                    pygame.time.set_timer(DRAW_EVENT, 50)
                    isDrawing = True

            if event.key == pygame.K_LCTRL:
                newArr = validateAutomataArray(automataArray)
                drawAutomataArray(newArr)
                automataArray = newArr

            if event.key == pygame.K_r:
                isDrawing = False
                screen.fill((0,0,0))
                pygame.time.set_timer(DRAW_EVENT, 0)
                resetedArray = resetArray(automataArray)
                automataArray = resetedArray
                drawAutomataArray(resetedArray)

        if event.type == DRAW_EVENT and isDrawing:
            screen.fill((0,0,0))
            newArr = validateAutomataArray(automataArray)
            drawAutomataArray(newArr)
            automataArray = newArr

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos
            isDrawing = False
            pygame.time.set_timer(DRAW_EVENT, 0)

            for i, row in enumerate(grid):
                for j, item in enumerate(row):
                    if item[0].collidepoint(mousePos):
                        screen.fill((0,0,0))
                        automataArray
                        clickedCell = automataArray[i][j][1]
                        if clickedCell:
                            automataArray[i][j][1] = False
                        elif clickedCell == False:
                            automataArray[i][j][1] = True
                        
                        drawAutomataArray(automataArray)


    #clock.tick(60)

    #pygame.Surface.blit(screen,drawingSurface, (centerOfScreenAndArray))
    #pygame.Surface.blit(screen,drawingSurface, ((100, 100)))
    #pygame.Surface.blit(screen,TestSurface, ((800, 100)))

    pygame.display.update()