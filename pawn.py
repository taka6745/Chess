from superClass import *
class Pawn(Piece):
    def __init__(self,colour):
        Piece.__init__(self,colour)
        moved_last_move = False