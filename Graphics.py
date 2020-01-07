from tkinter import *
from make_maze_functions import make_maze, make_pretty_maze, make_pretty_path
from MazeSolver import MazeSolver


class Graphics:
    def __init__(self, window):
        self.ts = 2
        self.window = window

        self.window.title("Maze")
        self.window.geometry(str(1200) + "x" + str(1200))

        self.blank_sprite = PhotoImage("sprites/blank.gif")

        self.width = 200
        self.height = 200
        self.maze = make_maze(self.width, self.height)
        self.pretty_maze = make_pretty_maze(self.maze)

        self.canvas = Canvas(self.window, width=1000, height=1000)
        self.canvas.grid(row=0, column=0)

        self.new_button = Button(self.window, text="new maze", command=self.new_maze)
        self.new_button.grid(row=1, column=1)
        self.solve_button = Button(self.window, text="solve", command=self.solve)
        self.solve_button.grid(row=2, column=1)

        self.solver = MazeSolver(self.maze)
        self.path_generator = self.solver.solve_generator()

        self.old_path = []

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(self.width * 2 + 1):
            for j in range(self.height * 2 + 1):
                if self.pretty_maze[i][j] == "#":
                    color = '#000'
                elif self.pretty_maze[i][j] == "-":
                    color = '#fff'
                elif self.pretty_maze[i][j] == "+":
                    color = '#0f0'
                self.canvas.create_rectangle(j*self.ts+self.ts,
                                             i*self.ts+self.ts,
                                             j*self.ts+self.ts*2,
                                             i*self.ts+self.ts*2, fill=color, outline='')

    def draw_path(self, path):
        p_path = make_pretty_path(path)

        for i in range(len(p_path), len(self.old_path)):
            self.canvas.create_rectangle(self.old_path[i][1]*self.ts+self.ts,
                                         self.old_path[i][0]*self.ts+self.ts,
                                         self.old_path[i][1]*self.ts+self.ts*2,
                                         self.old_path[i][0]*self.ts+self.ts*2, fill='#ff0')

        for i in range(len(self.old_path), len(p_path)):
            self.canvas.create_rectangle(p_path[i][1]*self.ts+self.ts,
                                         p_path[i][0]*self.ts+self.ts,
                                         p_path[i][1]*self.ts+self.ts*2,
                                         p_path[i][0]*self.ts+self.ts*2, fill='#f00')
        self.old_path = p_path



    def solve(self):
        try:
            path = next(self.path_generator)
            self.draw_path(path)
            self.window.after_idle(self.solve)
        except StopIteration:
            pass

    def new_maze(self):
        self.maze = make_maze(self.width, self.height)
        self.pretty_maze = make_pretty_maze(self.maze)
        self.draw_board()
        self.solver = MazeSolver(self.maze)
        self.path_generator = self.solver.solve_generator()
        self.old_path = []
