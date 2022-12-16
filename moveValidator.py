from helper import *
from ChatGptGui import create_chessboard


def init():
    numColumns = 8
    numRows = 8
    gameArray = [[" " for _ in range(numColumns)] for _ in range(numRows)]
    gameArray[0][0] = Rook("White")
    gameArray[0][1] = Knight("White")
    gameArray[0][2] = Bishop("White")
    gameArray[0][3] = Queen("White")
    gameArray[0][4] = King("White")
    gameArray[0][5] = Bishop("White")
    gameArray[0][6] = Knight("White")
    gameArray[0][7] = Rook("White")
    gameArray[7][0] = Rook("Black")
    gameArray[7][1] = Knight("Black")
    gameArray[7][2] = Bishop("Black")
    gameArray[7][3] = Queen("Black")
    gameArray[7][4] = King("Black")
    gameArray[7][5] = Bishop("Black")
    gameArray[7][6] = Knight("Black")
    gameArray[7][7] = Rook("Black")
    for i in range(8):
        gameArray[1][i] = Pawn("White")
        gameArray[6][i] = Pawn("Black")

    return gameArray


def removePiece(pos, board):
    board[pos[0]][pos[1]] = " "


def movePiece(startMove, endMove, board):
    board[endMove[0]][endMove[1]] = board[startMove[0]][startMove[1]]
    board[startMove[0]][startMove[1]] = ' '
    return board


if __name__ == "__main__": # will work on to take an array of moves as strings for batch testing, init() will reset board, need enable_visiual for GUI, currently just close the tkinter for next move
    print("Starting...")
    board = init()

    # Here add bits to check
    create_chessboard(board)


    if validateMove("A2,A4", board):
        print("Valid, Moving Piece")
        movePiece((1, 0), (3, 0), board)
        create_chessboard(board)
    else:
        print("Invalid")

    if validateMove("A4,A5", board):
        print("Valid, Moving Piece")
        movePiece((3, 0), (4, 0), board)
        create_chessboard(board)
    else:
        print("Invalid")
