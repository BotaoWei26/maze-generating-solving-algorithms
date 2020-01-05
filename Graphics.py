from tkinter import *
from make_maze_functions import make_maze, make_pretty_maze

class Graphics:
    def __init__(self, window):
        self.ts = 4
        self.window = window

        self.window.title("Maze")
        self.window.geometry(str(1200) + "x" + str(1200))

        self.blank_sprite = PhotoImage("sprites/blank.gif")

        self.width = 100
        self.height = 100
        self.maze = make_maze(self.width, self.height)
        self.pretty_maze = make_pretty_maze(self.maze)

        self.canvas = Canvas(self.window, width=1000, height=1000)
        self.canvas.grid(row=0, column=0)

        self.new_button = Button(self.window, text="new maze", command=self.new_maze)
        self.new_button.grid(row=1, column=1)

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(self.width * 2 + 1):
            for j in range(self.height * 2 + 1):
                if self.pretty_maze[i][j] == "#":
                    color = '#000'
                elif self.pretty_maze[i][j] == "-":
                    color = '#fff'
                self.canvas.create_rectangle(j*self.ts+self.ts,
                                             i*self.ts+self.ts,
                                             j*self.ts+self.ts*2,
                                             i*self.ts+self.ts*2, fill=color, outline='')

    def new_maze(self):
        self.maze = make_maze(self.width, self.height)
        self.pretty_maze = make_pretty_maze(self.maze)
        self.draw_board()
