
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
    initialPosition = (ord(initialString[0]) - 65, int(initialString[1]) - 1)
    finalPosition = (ord(finalString[0]) - 65, int(finalString[1]) - 1)
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
    for index in range(positionX+1, 8):
        if not (gameArray[index][positionY] == " "):
            maxY = index
            break
    for index in range(positionY+1, 8):
        if not (gameArray[positionX][index] == " "):
            maxX = index
            break

    minX = 0
    minY = 0
    for index in range(0, positionX):
        if not (gameArray[positionX - index][positionY] == " "):
            minY = positionX - index - 1
            break
    for index in range(0, positionY):
        if not (gameArray[positionX][positionY - index - 1] == " "):
            minX = positionY - index 
            break
    
    return (minX, maxX, minY, maxY)



def validateRook(initialPosition, finalPosition, gameArray):
    #Method seems to work based off basic checks.
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

def validateBishop(board, start, end):
    # check if the start and end positions are on the same diagonal
    if abs(start[0] - end[0]) != abs(start[1] - end[1]):
        return False
    if start[0] > 7 or start[1] > 7 or end[0] > 7 or end[1] > 7:
        return False
    # check if there are any pieces blocking the bishop's path
    row_step = 1 if start[0] < end[0] else -1
    col_step = 1 if start[1] < end[1] else -1
    row = start[0] + row_step
    col = start[1] + col_step

    while row != end[0] and col != end[1]:
        if board[row][col] != " ":
            return False
        row += row_step
        col += col_step

    return True
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
    if piece == " ":
         return False #Could give more detailed error messages
    #Now, must ascertain if move is possible depending on piece
    #Use switch statement to call correct function
    pieceString = str(piece)
    match pieceString:
        case "R":
            return(validateRook(initialPosition, finalPosition, gameArray))
        case "H":
            return(validateKnight(initialPosition, finalPosition, gameArray))
        case "B":
            return(validateBishop(initialPosition, finalPosition, gameArray))
        case "K":
            return(validateKing(initialPosition, finalPosition, gameArray))
        case "Q":
            return(validateQueen(initialPosition, finalPosition, gameArray))
        case "P":
            return(validatePawn(initialPosition, finalPosition, gameArray))



def updateBoard(startMove, endMove, board):
    board[endMove[0]][endMove[1]] = board[startMove[0]][startMove[1]]
    board[startMove[0]][startMove[1]] = ' '
    return board