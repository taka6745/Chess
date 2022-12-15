
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
    for index in range(positionX, 7):
        if not gameArray[index][positionY] == " ":
            maxX = index
            break
    for index in range(positionY, 7):
        if not gameArray[positionX][index] == " ":
            maxY = index
            break

    minX = 0
    minY = 0
    for index in range(0, positionX):
        if not gameArray[positionX - index][positionY] == " ":
            minX = positionX - index - 1
            break
    for index in range(0, positionY):
        if not gameArray[positionX][positionY - index] == " ":
            minY = positionY - index
            break
    
    return (minX, maxX, minY, maxY)


def validateRook(initialPosition, finalPosition, gameArray):
    (minX, maxX, minY, maxY) = minMaxHorizontal(initialPosition, gameArray)
    if not (initialPosition[0] == finalPosition[0]) and not (initialPosition[1] == finalPosition[1]):
        return False
    elif finalPosition[0] in range(minX, maxX) and finalPosition[1] in range(minY, maxY):
        return True
    else:
        return False

    

    pass

def validateKnight(initialPosition, finalPosition, gameArray):
    pass

def validateBishop(initialPosition, finalPosition, gameArray):
    pass

def validateQueen(initialPosition, finalPosition, gameArray):
    pass

def validateKing(initialPosition, finalPosition, gameArray):
    pass

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











