from superClass import *
class Bishop(Piece):
    def __init__(self,colour):
        Piece.__init__(self,colour)
        has_moved = False