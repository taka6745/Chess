import tkinter as tk
CELL_SIZE = 50


class AbstractGrid(tk.Canvas):
    """
    The grid upon which the game is played. Will have a specified number of
    columns and rows. Provides base functionality for other view classes.
    """

    def __init__(self, master, rows, cols, width, height, **kwargs):
        """
        Initialised on creation of an AbstractGrid instance.

        Parameters:
            rows: Number of rows
            cols: Number of columns
            width: Widht of grid in pixels
            height: Height of grid in pixels
        """
        super().__init__(master, width=width, height=height, **kwargs)
        self._master = master
        self._rows = rows
        self._cols = cols
        self._width = width
        self._height = height

        self._row_width = self._width / self._rows
        self._col_height = self._height / self._cols

    def get_bbox(self, position):
        """
        Returns the bounding box for the row, column position.

        Parameters:
            position: row and column number

        Returns: (x_min, y_min, x_max, y_max)
        """

        x_min = position[0] * self._row_width
        x_max = (position[0] + 1) * self._row_width
        y_min = position[1] * self._col_height
        y_max = (position[1] + 1) * self._col_height
        box = (x_min, y_min, x_max, y_max)
        return box

    def pixel_to_position(self, pixel):
        """
        Converts pixel position to row, column position.

        Parameters:
            pixel: x and y coordinates.

        Returns:
            position: row and column number
        """
        row_num = pixel.x // self._row_width
        col_num = pixel.y // self._col_height
        position = (row_num, col_num)
        return position

    def get_position_center(self, position):
        """
        Returns the pixel coordinates of the cell's centre.

        Parameters:
            position: row and column number
        """
        x_value = position[0] * self._row_width + self._row_width / 2
        y_value = position[1] * self._col_height + self._col_height / 2
        coordinates = (x_value, y_value)
        return coordinates

    def annotate_position(self, position, text, text_font="White"):
        """
        Annotates the centre of the cell with text.

        Parameters:
            position: row and column number
            text: Text to be annotated
        """
        centre = self.get_position_center(position)
        self.create_text(centre[0], centre[1], text=text, fill=text_font)
        """label = tk.Label(self._master, text = text)
        
        relx = centre[0] / self._width
        rely = centre[1] / self._height
        
        label.place(relx = relx, rely = rely, anchor = 'center')"""


class Board(AbstractGrid):
    def __init__(self, master, **kwargs):
        width = 9 * CELL_SIZE
        super().__init__(master, 9, 9, width, width, **kwargs)

    def draw_pieces(self, gameArray):
        for k in range(8):
            self.annotate_position((k+1, 0), chr(k + 97), 'Brown',)
            self.annotate_position((0, 8-k), str(k + 1), 'Brown')

        j = 0
        while j < 8:
            i = 0
            while i < 8:
                colour = "White"
                text_font = "Black"
                """
                if isinstance(game_grid[(i, j)], White):
                    colour = 'White'
                    text_font = "Black"
                elif isinstance(game_grid[(i, j)], Black):
                    colour = "Black"
                    text_font = "White"
                elif str(game_grid[(i,j)]) == EMPTY: 
                    colour = "Green"
                    text_font = "Black"
                else: 
                    colour = "Blue"
                    text_font = "Black"
                    """
                box = self.get_bbox((j + 1, i + 1))
                self.configure(bg='#B5B28F')
                self.create_rectangle(box[0], box[1], box[2], box[3],
                                      fill=colour)
                self.annotate_position(
                    (j + 1, i + 1), str(gameArray[i][j]), text_font)
                i += 1
            j += 1
        
    def draw_moves(self, sentinalGame, piecePositionString):
        gameArray = sentinalGame.gameArray
        for k in range(8):
            self.annotate_position((k+1, 0), chr(k + 97), 'Brown')
            self.annotate_position((0, 8-k), str(k + 1), 'Brown')
        
        for rowIndex in range(0, 8):
            for colIndex in range(0, 8):
                moveString = piecePositionString + "," + chr(colIndex+65) \
                     + str(8 - rowIndex)
                if sentinalGame.check_moveString(moveString):
                    
                    colour = "Blue"
                else:
                    colour = "White"

                self.configure(bg='#B5B28F')
                text_font = "Black"
                box = self.get_bbox((colIndex+1, rowIndex+1))
                self.create_rectangle(box[0], box[1], box[2], box[3],
                                      fill=colour)
                self.annotate_position((colIndex+1, rowIndex+1), \
                    str(gameArray[rowIndex][colIndex]), text_font)




        #j = 0
        #while j < 8:
            #i = 0
            #while i < 8:
                #moveString = piecePositionString + "," + chr(i+65) + str(j)
                #if sentinalGame.check_moveString(moveString):
                    #colour = "Blue"
                #else:
                    #colour = "White"
                #text_font = "Black"
                #box = self.get_bbox((j + 1, i + 1))
                #self.configure(bg='#B5B28F')
                #self.create_rectangle(box[0], box[1], box[2], box[3],
                                      #fill=colour)
                #self.annotate_position(
                    #(j + 1, i + 1), str(gameArray[i][j]), text_font)
                #i += 1
            #j+=1
        
        input("HELLO")

class boardPrinter():
    def __init__(self, root, gameArray):
        self._root = root
        self._title_label = tk.Label(root, bg="green", text="SentinalChess",
                                     fg="white")
        self._title_label.pack(side=tk.TOP, fill=tk.X)
        self._board = Board(root)
        self._board.pack()
        self.draw(gameArray)
        input("Hello")

    def draw(self, gameArray):
        self._board.delete("all")
        self._board.draw_pieces(gameArray)

class interface(object):
    def __init__(self):
        root = tk.Tk()
        self._title_label = tk.Label(root, bg="green", text="SentinalChess",
                                     fg="white")
        self._title_label.pack(side=tk.TOP, fill=tk.X)
        self.board = Board(root)
        self.board.pack()
        

    def moveMade(self, gameGrid):
        self.board.draw(gameGrid)
    
    def checkPiecesMoves(self, sentinalGame, piecePositionString):
        self.board.draw_moves(sentinalGame, piecePositionString)


def displayBoard(board):
    inter = interface(board)




# if __name__ == "__main__":
#     main()
