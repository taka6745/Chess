
class Piece(object):
    def __init__(self):
        pass

class Rook(Piece):
    def __init__(self):
        has_moved = False

class BlackRook(Rook):
    def __init__(self):
        super().__init__()

class WhiteRook(Rook):
    def __init__(self):
        super().__init__()

class Pawn(Piece):
    def __init__(self):
        moved_last_move = False

class BlackPawn(Rook):
    def __init__(self):
        super().__init__()

class WhitePawn(Rook):
    def __init__(self):
        super().__init__()

class Bishop(Piece):
    def __init__(self):
        has_moved = False

class BlackBishop(Rook):
    def __init__(self):
        super().__init__()

class WhiteBishop(Rook):
    def __init__(self):
        super().__init__()

class Queen(Piece):
    def __init__(self):
        moved_last_move = False

class BlackQueen(Rook):
    def __init__(self):
        super().__init__()

class WhiteQueen(Rook):
    def __init__(self):
        super().__init__()

class King(Piece):
    def __init__(self):
        has_moved = False

class BlackKing(Rook):
    def __init__(self):
        super().__init__()

class WhiteKing(Rook):
    def __init__(self):
        super().__init__()

class Knight(Piece):
    def __init__(self):
        has_moved = False

class BlackKnight(Rook):
    def __init__(self):
        super().__init__()

class WhiteKnight(Rook):
    def __init__(self):
        super().__init__()


class sentinalGame(object):

    def __init__(self):
        board = dict()
        for i in range(8):
            board[(1, i)] = WhitePawn()
            board[(6, i)] = BlackPawn()
        

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



