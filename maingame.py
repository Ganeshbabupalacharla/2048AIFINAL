from random import randint
import time
from tkinter import Frame, Label, CENTER
from boarddesign import BoardDesign
from expectimax import Expectimax

GRID_LEN = 4 #length of the grid
GRID_PADDING = 5        #padding in between the grids
SIZE = 500
BACKGROUND_COLOR_GAME = "#92877d"               #background color for game
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"         #when the cell is empty
BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563", \
                         32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61", \
                         512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}

CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2", \
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2", \
                   512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}

FONT = ("Helvetica", 25, "bold")
class Game(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title('Ganesh-2048')
        self.grid_cells = []
        self.initialise_grid()
        self.initilaise_matrix()
        self.update_grid_cells()
        self.AI = Expectimax()
        self.start_game()
        self.mainloop()

    def start_game(self):

        while True:
            self.board.move(self.AI.retrievemove(self.board))
            self.update_grid_cells()
            self.add_random_number()
            self.update_grid_cells()
            if len(self.board.get_available_moves()) == 0:
                self.game_over_display()
                break
            self.update()

    def game_over_display(self):

        for i in range(4):

            for j in range(4):
                self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
        self.grid_cells[0][0].configure(text="best", bg=BACKGROUND_COLOR_CELL_EMPTY)
        top_4 = list(map(int, reversed(sorted(list(self.board.grid.flatten())))))
        self.grid_cells[0][1].configure(text=str(top_4[0]), bg=BACKGROUND_COLOR_DICT[2048], fg=CELL_COLOR_DICT[2048])

        self.update()

    def initialise_grid(self):
        background = Frame(self, bg=BACKGROUND_COLOR_GAME, width=SIZE, height=SIZE)
        background.grid()
        for i in range(GRID_LEN):
            grid_row = []
            for j in range(GRID_LEN):
                cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY, width=SIZE / GRID_LEN, height=SIZE / GRID_LEN)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                # font = Font(size=FONT_SIZE, family=FONT_FAMILY, weight=FONT_WEIGHT)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=4,
                          height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def gen(self):
        return randint(0, GRID_LEN - 1)

    def initilaise_matrix(self):
        self.board = BoardDesign()
        self.add_random_number()
        self.add_random_number()

    def update_grid_cells(self):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):

                new_number = int(self.board.grid[i][j])
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)

                else:
                    n = new_number
                    if new_number > 2048:
                        c = 2048
                    else:
                        c = new_number
                    self.grid_cells[i][j].configure(text=str(n), bg=BACKGROUND_COLOR_DICT[c], fg=CELL_COLOR_DICT[c])

        self.update_idletasks()

    def add_random_number(self):

        if randint(0, 99) < 90:     #90% of times we will get 2
            value = 2
        else:                       #10 % of times we will get 4
            value = 4
        cells = self.board.get_available_cells()
        pos = cells[randint(0, len(cells) - 1)] if cells else None
        if pos is None:
            return None
        else:
            self.board.insert_number(pos, value)
            return pos


game = Game()
