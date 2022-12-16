class Piece(object):
    def __init__(self, colour):
        self.colour = colour
        self.white = True if colour == "White" else False

class Bishop(Piece):
    def __init__(self,colour):
        Piece.__init__(self,colour)
        has_moved = False

    def __str__(self):
        return "B"

class King(Piece):
    def __init__(self,colour):
        Piece.__init__(self,colour)
        has_moved = False

    def __str__(self):
        return "K"

class Knight(Piece):
    def __init__(self,colour):
        Piece.__init__(self,colour)
        has_moved = False

    def __str__(self):
        return "H"

class Pawn(Piece):
    def __init__(self,colour):
        Piece.__init__(self,colour)
        moved_last_move = False

    def __str__(self):
        return "P"

class Queen(Piece):
    def __init__(self,colour):
        Piece.__init__(self,colour)
        moved_last_move = False

    def __str__(self):
        return "Q"


class Rook(Piece):
    def __init__(self,colour):
        Piece.__init__(self,colour)
        has_moved = False

    def __str__(self):
        return "R"




