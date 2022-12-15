
"""
convertStringToIndex()
-----------------
moveString: The string that pertains to the move of form
Returns: Tuple of tuple of indices pertaining to moveString
(Effectively two lots of tuples holding the x and y positions
of initial and final positions)
"""
def convertStringToIndex(moveString):
    (initialString, finalString) = moveString.split(",")
    #Convert capital character to number
    initialPosition = (ord(initialString[0]) - 65, initialString[1] - 1)
    finalPosition = (ord(finalString[0]) - 65, finalString[1] - 1)
    return (initialPosition, finalPosition)

"""
validatePieceFunctions()
----------------
initialPosition: tuple of starting position
finalPosition: tuple of ending position
Returns: True if move possible, false if otherwise
"""
def minMaxHorizontal(position, gameArray):
    positionX = position[0]
    positionY = position[1]
    maxX = 8
    maxY = 8
    for index in range(positionX, 8):
        if not (gameArray[index][positionY] == " "):
            maxX = index
            break
    for index in range(positionY, 8):
        if not (gameArray[positionX][index] == " "):
            maxY = index
            break

    minX = 0
    minY = 0
    for index in range(0, positionX):
        if not (gameArray[positionX - index][positionY] == " "):
            minX = positionX - index - 1
            break
    for index in range(0, positionY):
        if not (gameArray[positionX][positionY - index] == " "):
            minY = positionY - index
            break
    
    return (minX, maxX, minY, maxY)

def minMaxDiagonal(position, gameArray):
    positionX = position[0]
    positionY = position[1]
    maxUpperRightDiagonal = 8
    minUpperRightDiagonal = 0
    #Max defined in the positive Y direction
    maxUpperLeftDiagonal = 8
    minUpperLeftDiagonal = 0
    for index in range(positionY, 8):
        if not (gameArray[index-positionY + positionX][index] == " "):
            maxUpperRightDiagonal = index
            break
    for index in range(positionY, 8):
        if not (gameArray[positionY-index + positionX][index] == " "):
            maxUpperLeftDiagonal = index
            break
    
    for index in range(0, positionY):
        if not(gameArray[index + positionX][positionY - index] == " "):
            minUpperRightDiagonal = positionY - index
            break
    for index in range(0, positionY):
        if not(gameArray[positionX - index][positionY - index] == " "):
            minUpperRightDiagonal = positionY - index
            break
    
    return (maxUpperRightDiagonal, minUpperRightDiagonal, \
        maxUpperLeftDiagonal, minUpperLeftDiagonal)


def validateRook(initialPosition, finalPosition, gameArray):
    (minX, maxX, minY, maxY) = minMaxHorizontal(initialPosition, gameArray)
    if not (initialPosition[0] == finalPosition[0]) and not\
         (initialPosition[1] == finalPosition[1]):
        return False
    elif finalPosition[0] in range(minX, maxX) and \
        finalPosition[1] in range(minY, maxY):
        return True
    else:
        return False

def validateKnight(initialPosition, finalPosition, gameArray):
    knightMoves = [(-1,2), (1,2), (2,1), (2,-1), \
        (-1,-2), (-1,2), (-2,1), (-2,-1)]
    if not(finalPosition[0] in range(0,8)) or \
        not(finalPosition[1] in range(0, 8)):
        return False

    for move in knightMoves:
        if initialPosition + move == finalPosition:
            return True
    return False

def validateBishop(initialPosition, finalPosition, gameArray):
    (maxUpperRightDiagonal, minUpperRightDiagonal, \
        maxUpperLeftDiagonal, minUpperLeftDiagonal) = \
            minMaxDiagonal(initialPosition, gameArray)
    # if (abs(initialPosition[0] - finalPosition[0]) - \
    #     abs(initialPosition[1] - finalPosition[1])):
    #     return False 
    if initialPosition[0] > finalPosition[0]: #this means it moved up
        if initialPosition[1] < finalPosition[1]: #this moved right
            spacesMovedUp = initialPosition[1] - finalPosition[1]
            spacesMoveRight = initialPosition[0] - finalPosition[0]
            if spacesMovedUp == spacesMoveRight and spacesMovedUp <= maxUpperRightDiagonal:
                return True
            else:
                return False
        else: #this moved up left
            spacesMovedUp = initialPosition[1] - finalPosition[1]
            spacesMoveleft = finalPosition[0] - initialPosition[0] 
            if spacesMovedUp == spacesMoveleft and spacesMovedUp <= maxUpperLeftDiagonal:
                return True
            else:
                return False
    else: # this means it moved down
        if initialPosition[1] < finalPosition[1]: #this moved down right
            spacesMovedDown = finalPosition[1] - initialPosition[1]
            spacesMoveRight = finalPosition[0] - initialPosition[0] 
            if spacesMovedUp == spacesMoveRight and spacesMovedDown <= minUpperLeftDiagonal:
                return True
            else:
                return False
        else: #this moved down left
            spacesMovedDown = finalPosition[1] - initialPosition[1]
            spacesMoveleft = initialPosition[0] - finalPosition[0]
            if spacesMovedUp == spacesMoveleft and spacesMovedDown <= minUpperRightDiagonal:
                return True
            else:
                return False
def validateQueen(initialPosition, finalPosition, gameArray):
    return validateBishop(initialPosition, finalPosition, gameArray) or \
        validateRook(initialPosition, finalPosition, gameArray)

def validateKing(initialPosition, finalPosition, gameArray):
    kingMoves = [(1,-1), (1,0), (1,1), (0,-1), (0,1), (-1,-1), (-1,0), (-1,1)]
    for move in kingMoves:
        if initialPosition + move == finalPosition:
            return True
    return False

def validatePawn(initialPosition, finalPosition, gameArray):
    pass


"""
validateMove()
----------------
moveString: The string that pertains to the move of form
"A1,A2"
gameArray: The game array obviously
Returns: True if move possible, false if otherwise.
"""
def validateMove(moveString, gameArray):
    (initialPosition, finalPosition) = convertStringToIndex(moveString)
    #piece variable is the piece being moved, must first validate
    #the existence of a piece at initialPosition
    piece = gameArray[initialPosition[0]][initialPosition[1]]
    if piece == " ": return False #Could give more detailed error messages
    #Now, must ascertain if move is possible depending on piece
    #Use switch statement to call correct function
    match str(piece):
        case "R":
            validateRook(initialPosition, finalPosition, gameArray)
        case "H":
            validateKnight(initialPosition, finalPosition, gameArray)
        case "B":
            validateBishop(initialPosition, finalPosition, gameArray)
        case "K":
            validateKing(initialPosition, finalPosition, gameArray)
        case "Q":
            validateQueen(initialPosition, finalPosition, gameArray)
        case "P":
            validatePawn(initialPosition, finalPosition, gameArray)



def updateBoard(startMove, endMove, board):
    board[endMove[0]][endMove[1]] = board[startMove[0]][startMove[1]]
    board[startMove[0]][startMove[1]] = ' '
    return board







