from superClass import *
class Queen(Piece):
    def __init__(self,colour):
        Piece.__init__(self,colour)
        moved_last_move = False

    def __str__(self):
        return "Q"
