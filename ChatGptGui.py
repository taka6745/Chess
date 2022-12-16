import tkinter as tk

# Chessboard colors
colors = ["#ffffff", "#4a4a4a"]


def create_chessboard(board):
    # Create the root window
    root = tk.Tk()

    # Create a canvas to draw the chessboard on
    canvas = tk.Canvas(root, width=512, height=512)
    canvas.pack()

    # Draw the squares of the chessboard
    for i in range(8):
        for j in range(8):
            x1, y1 = (7 - j) * 64, i * 64
            x2, y2 = x1 + 64, y1 + 64
            color = colors[(i + j) % 2]
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    # Draw the pieces on the chessboard
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != "":
                x, y = ((7 - j) * 64) + 32, (i * 64) + 32
                canvas.create_text(
                    x, y, text=piece, font=("Arial", 32), fill="RED")

    # Run the main loop
    root.mainloop()


# Example usage
board = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"],
]
