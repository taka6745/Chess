from pieces import *
from helper import *
from interface import *
class sentinalGame(object):

    def __init__(self):
        numColumns = 8
        numRows = 8
        self.gameArray = [[" " for _ in range(numColumns)] for _ in range(numRows)]
        self.gameArray[7][0] = Rook("White")
        self.gameArray[7][1] = Knight("White")
        self.gameArray[7][2] = Bishop("White")
        self.gameArray[7][3] = Queen("White")
        self.gameArray[7][4] = King("White")
        self.gameArray[7][5] = Bishop("White")
        self.gameArray[7][6] = Knight("White")
        self.gameArray[7][7] = Rook("White")
        self.gameArray[0][0] = Rook("Black")
        self.gameArray[0][1] = Knight("Black")
        self.gameArray[0][2] = Bishop("Black")
        self.gameArray[0][3] = Queen("Black")
        self.gameArray[0][4] = King("Black")
        self.gameArray[0][5] = Bishop("Black")
        self.gameArray[0][6] = Knight("Black")
        self.gameArray[0][7] = Rook("Black")
        for i in range(8):
            self.gameArray[6][i] = Pawn("White")
            self.gameArray[1][i] = Pawn("Black")
        self.gameArray[3][5] = Pawn("White") 
        self.gameArray[3][3] = Pawn("Black") 
        self.gameArray[3][4] = Queen("White") 
        
        #With that above, A1 is (7, 0), A8 is (0, 0)
        #H1 is (7, 7) and H8 is (0,7)
        
        #displayBoard(self.gameArray)
        #input("Hi")
        #self.gameArray = updateBoard((1,0),(3,0),self.gameArray)
        #displayBoard(self.gameArray)
        #input("Hello")
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
        return validateMove(moveString, self.gameArray)

def main():
    sentinal = sentinalGame() 
    inter = interface()
    inter.checkPiecesMoves(sentinal, "E5") #pawns can play checkers with their double moves
    print(sentinal.check_moveString("E5,E6"))
 
    

if __name__ == "__main__":
    main()


