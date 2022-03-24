import tkinter as tk
import game

class grid_class:

    def __init__(self, N):
        self.N = N

    def start(self):
        N = self.N
        size = 600
        # Create a grid of None to store the references to the tiles
        self.tiles = [[None for _ in range(N)] for _ in range(N)]
        self.sq_size = int(size / N)
        root = tk.Tk()
        self.c = tk.Canvas(root, width=size, height=size, borderwidth=0, background='white')
        self.b = tk.Button(text="    Next    ", command=self.click_next, bg="yellow")
        for x in range(N):
            self.c.create_line(self.sq_size * x, 0, self.sq_size * x, size, fill='gray', width=1)
            self.c.create_line(0, self.sq_size * x, size, self.sq_size * x, fill='gray', width=1)
        self.c.bind("<Button-1>", self.callback)
        self.c.pack()
        self.b.pack()
        root.mainloop()

    def callback(self, event):
        col_width = self.sq_size
        row_height = self.sq_size
        # Calculate column and row number
        col = int(event.x//col_width)
        row = int(event.y//row_height)
        # If the tile is not filled, create a rectangle
        if not self.tiles[row][col]:
            self.tiles[row][col] = self.c.create_rectangle(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="black" )

        # If the tile is filled, delete the rectangle and clear the reference
        else:
            self.c.delete(self.tiles[row][col])
            self.tiles[row][col] = None

    # Create the window, a canvas and the mouse click event binding
    def click_next(self):
        grid = [[255 if (self.tiles[row][col] != None) else 0 for col in range(self.N)] for row in range(self.N)]
        game.game_class(self.N).execute(grid)






