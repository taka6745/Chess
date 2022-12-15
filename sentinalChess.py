from init import *
"""
class Piece(object):
    def __init__(self):
        pass

class Rook(Piece):
    def __init__(self):
        has_moved = False
    
    def __str__(self):
        return "R"

class BlackRook(Rook):
    def __init__(self):
        super().__init__()

class WhiteRook(Rook):
    def __init__(self):
        super().__init__()

class Pawn(Piece):
    def __init__(self):
        moved_last_move = False
    
    def __str__(self):
        return "P"

class BlackPawn(Pawn):
    def __init__(self):
        super().__init__()

class WhitePawn(Pawn):
    def __init__(self):
        super().__init__()

class Bishop(Piece):
    def __init__(self):
        has_moved = False
        
    def __str__(self):
        return "B"

class BlackBishop(Bishop):
    def __init__(self):
        super().__init__()

class WhiteBishop(Bishop):
    def __init__(self):
        super().__init__()

class Queen(Piece):
    def __init__(self):
        moved_last_move = False

    def __str__(self):
        return "Q"

class BlackQueen(Queen):
    def __init__(self):
        super().__init__()

class WhiteQueen(Queen):
    def __init__(self):
        super().__init__()

class King(Piece):
    def __init__(self):
        has_moved = False

    def __str__(self):
        return "K"

class BlackKing(King):
    def __init__(self):
        super().__init__()

class WhiteKing(King):
    def __init__(self):
        super().__init__()

class Knight(Piece):
    def __init__(self):
        has_moved = False

    def __str__(self):
        return "H"

class BlackKnight(Knight):
    def __init__(self):
        super().__init__()

class WhiteKnight(Knight):
    def __init__(self):
        super().__init__()
"""

class sentinalGame(object):

    def __init__(self):
        numColumns = 8
        numRows = 8
        self.gameArray = [[" " for _ in range(numColumns)] for _ in range(numRows)]
        self.gameArray[0][0] = Rook()
        self.gameArray[0][1] = Knight()
        self.gameArray[0][2] = Bishop()
        self.gameArray[0][3] = Queen()
        self.gameArray[0][4] = King()
        self.gameArray[0][5] = Bishop()
        self.gameArray[0][6] = Knight()
        self.gameArray[0][7] = Rook()
        self.gameArray[7][0] = Rook()
        self.gameArray[7][1] = Knight()
        self.gameArray[7][2] = Bishop()
        self.gameArray[7][3] = Queen()
        self.gameArray[7][4] = King()
        self.gameArray[7][5] = Bishop()
        self.gameArray[7][6] = Knight()
        self.gameArray[7][7] = Rook()
        for i in range(8):
            self.gameArray[1][i] = Pawn()
            self.gameArray[6][i] = Pawn()

    
    
    




    
        

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



