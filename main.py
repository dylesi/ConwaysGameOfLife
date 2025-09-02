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



automataAmountX = 50
automataAmountY = 50
padding = 1
automataWidth = 15
automataHeight = 15
automataRect = (automataWidth, automataHeight)

#drawingSurface.fill((100,100,100))
arrayWidth = (automataWidth * automataAmountX) + (padding * automataAmountX)
arrayHeight = (automataHeight * automataAmountY) + (padding * automataAmountY)
#print(f"arraywidth {arrayWidth} arrheight: {arrayHeight}")
centerOfScreenAndArray = (screenWidth / 2 - arrayWidth / 2, screenHeight / 2 - arrayHeight / 2)

drawingSurface = pygame.Surface((arrayWidth,arrayHeight))
#pygame.draw.rect(drawingSurface, "White", (0, 0, 55, 55), width=1)
#pygame.draw.rect(TestSurface, "White", (0, 0, arrayWidth, arrayHeight), width=5)


def createAutomataArray():
    grid = []
    for i in range(automataAmountY):
        row = []
        for j in range(automataAmountX):
            automataPosX = j * (automataWidth + padding)
            automataPosY = i * (automataHeight + padding)
            rect = (automataPosX, automataPosY, automataWidth, automataHeight)
            row.append([rect, False])
        grid.append(row)
    return grid

#OLD REMADE
# def createAutomataArray():
#     automataArray = []
#     startingPointX = 0
#     startingPointY = 0


#     for i in range(automataAmountX):
#         for j in range(automataAmountY):
#             automataArray.append([(startingPointX, startingPointY, automataRect[0], automataRect[1]), False])
#             startingPointX += automataWidth + padding
#         startingPointX = 0
#         startingPointY += automataHeight + padding
#     return automataArray

def drawAutomataArray(grid):
    drawingSurface.fill((0, 0, 0))  # clear before drawing
    for row in grid:
        for rect, alive in row:
            pygame.draw.rect(drawingSurface, (100, 100, 100), rect, width=1)
            if alive:
                pygame.draw.rect(drawingSurface, "White", rect)

#OLD REMADE
# def drawAutomataArray(arr):
#     drawingSurface.fill((0,0,0))
#     for arrRect, boolVal in arr:
#         pygame.draw.rect(drawingSurface, (100,100,100), arrRect, width=1)
#         if boolVal == True:
#             pygame.draw.rect(drawingSurface, "White", arrRect)

def drawAutomataArrayToTestSurface(arr):
    for arrRect, boolVal in arr:
        if boolVal == True:
            pygame.draw.rect(TestSurface, "White", arrRect, width=1)

neighbourArray = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

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




# OLD REMADE
# def validateAutomataArray(arr):
#     returnArr = []
#     for index, automataCoords, in enumerate(list(arr)):

#         testBoolean = arr[index][1]

#         neighbourCount = 0
#         cellPositionX, cellPositionY = automataCoords[0][0], automataCoords[0][1]
        
#         topLeftNeighbour = cellPositionX - automataWidth - padding, cellPositionY - automataWidth - padding 
#         topCenterNeighbour = cellPositionX - automataWidth - padding, cellPositionY
#         topRightNeighbour = cellPositionX - automataWidth - padding, cellPositionY + automataWidth + padding
#         leftNeighbour = cellPositionX, cellPositionY - automataWidth - padding
#         rightNeighbour = cellPositionX, cellPositionY + automataWidth + padding
#         bottomLeftNeighbour = cellPositionX + automataWidth + padding, cellPositionY - automataWidth - padding 
#         bottomCenterNeighbour = cellPositionX + automataWidth + padding, cellPositionY
#         bottomRightNeighbour = cellPositionX + automataWidth + padding, cellPositionY + automataWidth + padding

#         neighbourArray =  [topLeftNeighbour, topCenterNeighbour, topRightNeighbour, leftNeighbour,rightNeighbour, bottomLeftNeighbour, bottomCenterNeighbour, bottomRightNeighbour]
#         #print(neighbourArray)
#         for cell in arr:
#             cellCoord = cell[0][0], cell[0][1]
#             status = cell[1]
#             if cellCoord in neighbourArray and status:
#                 neighbourCount += 1
#         #print(f"Pos: {cellPositionX, cellPositionY} neighbourcount: {neighbourCount}")
#         if neighbourCount < 2:
#             #print("Neighbour count less than 2")
#             testBoolean = False
#             #print(cellStatus)
#         elif neighbourCount == 2 and status == True:
        
#             #print("Neighbour count 2 or 3")
#             testBoolean = True
#         elif neighbourCount == 3 and status == True:
#             #print(f"Pos: {cellPositionX, cellPositionY} neighbourcount: {neighbourCount}")
#             testBoolean = True
#         elif neighbourCount > 3:
#             #print("Neighbour more  than 3")
#             testBoolean = False
#         elif neighbourCount == 3 and status == False:
#             #print("Neighbour exact 3 and dead")
#             testBoolean = True
        
#         returnArr.append([arr[index][0], testBoolean])
#         neighbourCount = 0
#     return returnArr


arr = [
    [True,False,False,True],

]
print(arr)
print(arr[0][1])


automataArray = createAutomataArray()

print(f"Lvl 1: {automataArray[1]}")
print(f"Lvl 1: {automataArray[1][1]}")

automataArray[5][2][1] = True
automataArray[5][3][1] = True
automataArray[6][2][1] = True
automataArray[6][3][1] = True
automataArray[3][12][1] = True
automataArray[3][13][1] = True
automataArray[4][11][1] = True
automataArray[5][10][1] = True
automataArray[6][10][1] = True
automataArray[6][14][1] = True
automataArray[4][15][1] = True
automataArray[8][15][1] = True
automataArray[5][16][1] = True
automataArray[6][16][1] = True
automataArray[7][16][1] = True
automataArray[6][17][1] = True
automataArray[7][10][1] = True
automataArray[8][11][1] = True
automataArray[9][12][1] = True
automataArray[9][13][1] = True
automataArray[2][22][1] = True
automataArray[1][24][1] = True
automataArray[2][24][1] = True
automataArray[3][20][1] = True
automataArray[3][21][1] = True
automataArray[4][20][1] = True
automataArray[4][21][1] = True
automataArray[5][20][1] = True
automataArray[5][21][1] = True

automataArray[6][22][1] = True
automataArray[6][24][1] = True
automataArray[7][24][1] = True

automataArray[3][30][1] = True
automataArray[3][31][1] = True
automataArray[4][30][1] = True
automataArray[4][31][1] = True






    


drawAutomataArray(automataArray)



#drawAutomataArrayToTestSurface(automataArray)


def printArray(string, arr):
    print(f"Array {string}: ")
    for item in range(0, len(arr), 5):
        print(arr[item:item+ 5])


# printArray("before", automataArray)
# printArray("after", validatedArray)
# validatedArray = validateAutomataArray(automataArray)
# drawAutomataArray(validatedArray)



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
                pygame.time.set_timer(DRAW_EVENT, 50)
        if event.type == DRAW_EVENT:
            newArr = validateAutomataArray(automataArray)
            drawAutomataArray(newArr)
            automataArray = newArr
        

    pygame.Surface.blit(screen,drawingSurface, (centerOfScreenAndArray))
    #pygame.Surface.blit(screen,drawingSurface, ((100, 100)))
    #pygame.Surface.blit(screen,TestSurface, ((800, 100)))

    pygame.display.update()