from init import *
from helper import *

class sentinalGame(object):

    def __init__(self):
        numColumns = 8
        numRows = 8
        self.gameArray = [[" " for _ in range(numColumns)] for _ in range(numRows)]
        self.gameArray[0][0] = Rook("White")
        self.gameArray[0][1] = Knight("White")
        self.gameArray[0][2] = Bishop("White")
        self.gameArray[0][3] = Queen("White")
        self.gameArray[0][4] = King("White")
        self.gameArray[0][5] = Bishop("White")
        self.gameArray[0][6] = Knight("White")
        self.gameArray[0][7] = Rook("White")
        self.gameArray[7][0] = Rook("Black")
        self.gameArray[7][1] = Knight("Black")
        self.gameArray[7][2] = Bishop("Black")
        self.gameArray[7][3] = Queen("Black")
        self.gameArray[7][4] = King("Black")
        self.gameArray[7][5] = Bishop("Black")
        self.gameArray[7][6] = Knight("Black")
        self.gameArray[7][7] = Rook("Black")
        for i in range(8):
            self.gameArray[1][i] = Pawn("White")
            self.gameArray[6][i] = Pawn("Black")

    def attemptMove(self):
        moveString = input("Your move: ")
        validateMove(moveString, self.gameArray)


    def check_moveString(self, moveString: str):
        """
        check_move()
        -----------------------
        moveString: String of form "a1b1" signifying the move to be checked
        Returns: True if move is possible, false otherwise
        -----------------------
        Function seperates moveString into moveFrom and moveTo, and using moveFrom finds the piece object
        at that position. Using this piece object, the check_move method is called with the moveFrom and 
        moveTo string.
        """
        pass

    def check_move(self, rook: Rook, moveFrom: str, moveTo: str):
        pass

    def check_move(self, bishop: Bishop, moveFrom: str, moveTo: str):
        pass

    def check_move(self, pawn: Pawn, moveFrom: str, moveTo: str):
        pass

    def check_move(self, knight: Knight, moveFrom: str, moveTo: str):
        pass

    def check_move(self, queen: Queen, moveFrom: str, moveTo: str):
        pass

    def check_move(self, king: King, moveFrom: str, moveTo: str):
        pass



