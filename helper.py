from pieces import *
"""
convertStringToIndex()
-----------------
moveString: The string that pertains to the move of form
Returns: Tuple of tuple of indices pertaining to moveString
(Effectively two lots of tuples holding the x and y positions
of initial and final positions)
"""
def convertStringToIndex(moveString): # I've reversed this, our array system works (y,x) becuase of how the array is set
    (initialString, finalString) = moveString.split(",")
    #Convert capital character to number
    # initialPosition = (ord(initialString[0]) - 65, int(initialString[1]) - 1)
    # finalPosition = (ord(finalString[0]) - 65, int(finalString[1]) - 1)
    initialPosition = (8 - int(initialString[1]), (ord(initialString[0]) - 65))
    finalPosition = (8 - int(finalString[1]) , (ord(finalString[0]) - 65))

    return (initialPosition, finalPosition)

def gameArrayChecker(gameArray, xIndex, yIndex, pieceWhite):
    if not (gameArray[xIndex][yIndex] == " "):
        if gameArray[xIndex][yIndex].white == pieceWhite:
            return True


def minMaxHorizontal(position, gameArray, pieceWhite):
    positionX = position[0]
    positionY = position[1]
    maxX = 8
    maxY = 8
    for index in range(positionX+1, 8):
        if gameArrayChecker(gameArray, index, positionY, pieceWhite):
            maxY = index
            break
    for index in range(positionY+1, 8):
        if gameArrayChecker(gameArray, positionX, index, pieceWhite):
            maxX = index
            break

    minX = 0
    minY = 0
    for index in range(0, positionX):
        if gameArrayChecker(gameArray, positionX - index, \
            positionY, pieceWhite):
            minY = positionX - index - 1
            break
    for index in range(0, positionY):
        if gameArrayChecker(gameArray, positionX, \
            positionY - index, pieceWhite):
            minX = positionY - index 
            break
    
    return (minX, maxX, minY, maxY)

"""
validatePieceFunctions()
----------------
initialPosition: tuple of starting position
finalPosition: tuple of ending position
Returns: True if move possible, false if otherwise
"""
def validateRook(initialPosition, finalPosition, gameArray, pieceWhite):
    #Method seems to work based off basic checks.
    #(minX, maxX, minY, maxY) = minMaxHorizontal(initialPosition, gameArray, \
     #   pieceWhite)
    start = initialPosition
    end = finalPosition
    if not (initialPosition[0] == finalPosition[0]) and not\
         (initialPosition[1] == finalPosition[1]):
        return False
    if gameArray[end[0]][end[1]] != " ":
        if gameArray[end[0]][end[1]].white == pieceWhite:
            return False
    row_step = 0
    col_step = 0
    if start[0] == end[0]:
        col_step = 1 if start[1] < end[1] else -1
    elif start[1] == end[1]:
        row_step = 1 if start[0] < end[0] else -1
    row = start[0] + row_step
    col = start[1] + col_step
    while row != end[0] or col != end[1]:
        if gameArray[row][col] != " ": return False
        row+=row_step
        col+=col_step
    return True

def validateKnight(initialPosition, finalPosition, gameArray, pieceWhite):
    knightMoves = [(-1,2), (1,2), (2,1), (2,-1), \
        (-1,-2), (-1,2), (-2,1), (-2,-1)]
    if not(finalPosition[0] in range(0,8)) or \
        not(finalPosition[1] in range(0, 8)):
        return False
    
    x = finalPosition[0]
    y = finalPosition[1]
    
    if not(gameArray[x][y] == " "):
        if gameArray[x][y].white == pieceWhite:
            return False

    for move in knightMoves:
        if initialPosition[0] + move[0] == x and initialPosition[1] + move[1] == y:
            return True
    return False

def validateBishop(initialPosition, finalPosition, gameArray, pieceWhite):
    # check if the start and end positions are on the same diagonal
    start = initialPosition
    end = finalPosition
    if abs(int(start[0]) - int(end[0])) != abs(int(start[1]) - int(end[1])):
        return False
    if start[0] > 7 or start[1] > 7 or end[0] > 7 or end[1] > 7:
        return False
    # check if there are any pieces blocking the bishop's path
    row_step = 1 if start[0] < end[0] else -1
    col_step = 1 if start[1] < end[1] else -1
    row = start[0] + row_step
    col = start[1] + col_step
    if gameArray[end[0]][end[1]] != " ":
        if gameArray[end[0]][end[1]].white == pieceWhite:
            return False

    while row != end[0] and col != end[1]:
        if gameArray[row][col] != " ": return False
        row += row_step
        col += col_step

    return True

def validateQueen(initialPosition, finalPosition, gameArray, pieceWhite):
    return validateBishop(initialPosition, finalPosition, gameArray, \
        pieceWhite) or validateRook(initialPosition, finalPosition, \
            gameArray, pieceWhite)

def validateKing(initialPosition, finalPosition, gameArray, pieceWhite):
    kingMoves = [(1,-1), (1,0), (1,1), (0,-1), (0,1), (-1,-1), (-1,0), (-1,1)]
    if not(finalPosition[0] in range(0, 8)) or \
        not(finalPosition[1] in range(0, 8)):
        return False
    if gameArray[finalPosition[0]][finalPosition[1]] != " ":
        if gameArray[finalPosition[0]][finalPosition[1]].white == \
            pieceWhite:
            return False
    for move in kingMoves:
        if initialPosition[0] + move[0] == finalPosition[0] and \
            initialPosition[1] + move[1] == finalPosition[1]:
            return True
    return False

def validatePawn(initialPosition, finalPosition, gameArray, pieceWhite): # still needs En Passant
    pawnMoves = [(1,0)]
    print("Validating Pawn")
    pawnTakeMove = [(1,1),(1,-1)]
    if (initialPosition[0] == 1 and not pieceWhite) or (initialPosition[0] == 6 and pieceWhite):
        pawnMoves.append((2,0))
    if gameArray[finalPosition[0]][finalPosition[1]] != " ":

        if gameArray[finalPosition[0]][finalPosition[1]].colour != gameArray[initialPosition[0]][initialPosition[1]].colour:
            if pieceWhite and tuple((initialPosition[0] - finalPosition[0], initialPosition[1] - finalPosition[1])) in pawnTakeMove:
                return True
            elif (not pieceWhite) and (tuple(( finalPosition[0] - initialPosition[0], finalPosition[1] - initialPosition[1])) in pawnTakeMove):
                return True
            else:
                return False
    if not(finalPosition[0] in range(0, 8)) or \
        not(finalPosition[1] in range(0, 8)):
        return False
    if pieceWhite and tuple(( initialPosition[0] - finalPosition[0],  initialPosition[1] - finalPosition[1])) not in pawnMoves:
        return False
    elif not pieceWhite and tuple(( finalPosition[0] - initialPosition[0],  finalPosition[1] - initialPosition[1])) not in pawnMoves:
        return False
    
    return True

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
    pieceWhite = piece.white
    #Now, must ascertain if move is possible depending on piece
    #Use switch statement to call correct function
    pieceString = str(piece)

    match pieceString:
        case "R":
            return(validateRook(initialPosition, finalPosition, gameArray,\
                        pieceWhite))
        case "H":
            return(validateKnight(initialPosition, finalPosition, gameArray, \
                pieceWhite))
        case "B":
            return(validateBishop(initialPosition, finalPosition, gameArray, \
                pieceWhite))
        case "K":
            return(validateKing(initialPosition, finalPosition, gameArray, \
                pieceWhite))
        case "Q":
            return(validateQueen(initialPosition, finalPosition, gameArray, \
                pieceWhite))
        case "P":
            return(validatePawn(initialPosition, finalPosition, gameArray, \
                pieceWhite))


def updateBoard(startMove, endMove, board):
    board[endMove[0]][endMove[1]] = board[startMove[0]][startMove[1]]
    board[startMove[0]][startMove[1]] = ' '
    return board