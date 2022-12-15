from superClass import *
class Rook(Piece):
    def __init__(self,colour):
        Piece.__init__(self,colour)
        has_moved = False

    def __str__(self):
        return "R"