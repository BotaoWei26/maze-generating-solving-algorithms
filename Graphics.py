from tkinter import *
from make_maze_functions import make_maze_recursive_division, make_maze_depth_first, make_pretty_maze, make_pretty_path
from maze_solver_functions import solve_generator_depth_first

class Graphics:
    def __init__(self, window):
        self.window = window

        self.window.title("Maze")
        self.window.geometry(str(1400) + "x" + str(800))
        self.blank_sprite = PhotoImage("sprites/blank.gif")

        self.width = 10
        self.height = 10
        self.ts = min(1000 / (self.width * 2 + 3), 800 / (self.height * 2 + 3))
        self.maze = make_maze_recursive_division(self.width, self.height)
        self.pretty_maze = make_pretty_maze(self.maze)

        self.canvas = Canvas(self.window, width=1000, height=800)
        self.canvas.grid(row=0, column=0, rowspan=1000)

        self.make_maze_button = Button(self.window, text="Make Maze", command=self.new_maze)
        self.make_maze_button.grid(row=0, column=1)

        self.type_var = IntVar()
        self.type_var.set(1)
        self.type_recursive_division_radiobutton = Radiobutton(self.window, text="Recursive Division", variable=self.type_var, value=1)
        self.type_recursive_division_radiobutton.grid(row=1, column=1)
        self.type_recursive_depth_first = Radiobutton(self.window, text="Depth First", variable=self.type_var, value=2)
        self.type_recursive_depth_first.grid(row=2, column=1)

        self.even_var = IntVar()
        self.even_checkbox = Checkbutton(self.window, text="Even", variable=self.even_var)
        self.even_checkbox.grid(row=3, column=1)
        self.holes_label = Label(self.window, text="Number of Holes:")
        self.holes_label.grid(row=4, column=1)
        self.holes_entry = Entry(self.window)
        self.holes_entry.grid(row=5, column=1)
        self.height_label = Label(self.window, text="Height:")
        self.height_label.grid(row=6, column=1)
        self.height_entry = Entry(self.window)
        self.height_entry.grid(row=7, column=1)
        self.width_label = Label(self.window, text="Width:")
        self.width_label.grid(row=8, column=1)
        self.width_entry = Entry(self.window)
        self.width_entry.grid(row=9, column=1)

        self.solve_button = Button(self.window, text="solve", command=self.solve)
        self.solve_button.grid(row=0, column=2)
        self.memory_var = IntVar()
        self.memory_checkbox = Checkbutton(self.window, text="Memory", variable=self.memory_var)
        self.memory_checkbox.grid(row=1, column=2)
        self.direction_choices = {'1', '2', '3', '4'}
        self.direction_vars = [StringVar(self.window) for i in range(4)]
        self.direction_labels = [Label(self.window, text="{} priority:".format(d)) for d in ["Up", "Right", "Down", "Left"]]
        self.direction_options = [OptionMenu(self.window, self.direction_vars[i], *self.direction_choices) for i in range(4)]
        for i in range(4):
            self.direction_vars[i].set('{}'.format(i+1))
            self.direction_labels[i].grid(row=i*2+2, column=2)
            self.direction_options[i].grid(row=i*2+3, column=2)

        self.path_generator = None
        self.old_path = []
        self.path_generator_setup()

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for j in range(self.width * 2 + 1):
            for i in range(self.height * 2 + 1):
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
        self.draw_board()
        self.path_generator_setup()
        self.solve_cont()

    def path_generator_setup(self):
        priority = {"up": int(self.direction_vars[0].get()),
                    "right": int(self.direction_vars[1].get()),
                    "down": int(self.direction_vars[2].get()),
                    "left": int(self.direction_vars[3].get())
                    }
        priority_sorted = [k for k, v in sorted(priority.items(), key=lambda item: item[1])]
        self.path_generator = solve_generator_depth_first(self.maze, priority_sorted, self.memory_var.get())
        self.old_path = []

    def solve_cont(self):
        try:
            path = next(self.path_generator)
            self.draw_path(path)
            self.window.after_idle(self.solve_cont)
        except StopIteration:
            pass

    def new_maze(self):
        # test hole_num isdigit and > 0
        try:
            num_holes = int(self.holes_entry.get())
            if num_holes <= 0:
                raise ValueError
        # default to 1
        except ValueError:
            num_holes = 1

        # test height isdigit and <= 0 and > 500
        try:
            self.height = int(self.height_entry.get())
            if self.height <= 0 or self.height > 200:
                raise ValueError
        # default to 10
        except ValueError:
            self.height = 10

        # test width isdigit and <= 0 and > 500
        try:
            self.width = int(self.width_entry.get())
            if self.width <= 0 or self.width > 200:
                raise ValueError
        # default to 10
        except ValueError:
            self.width = 10

        self.ts = min(1000 / (self.width * 2 + 3), 800 / (self.height * 2 + 3))
        # choice of algorithm
        if self.type_var.get() == 1:
            self.new_maze_maze_recursive_division(num_holes)
        elif self.type_var.get() == 2:
            self.new_maze_maze_depth_first()

        self.pretty_maze = make_pretty_maze(self.maze)
        self.draw_board()
        self.path_generator_setup()
        self.old_path = []

    def new_maze_maze_recursive_division(self, num_holes):
        self.maze = make_maze_recursive_division(self.width, self.height, num_holes, self.even_var.get())

    def new_maze_maze_depth_first(self):
        self.maze = make_maze_depth_first(self.width, self.height)
