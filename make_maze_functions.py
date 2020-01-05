from random import randint

def make_maze(x_width, y_width):
    maze = []
    for y in range(y_width):
        row = []
        for x in range(x_width):
            row.append([1 if y == 0 else 0,
                        1 if x == x_width - 1 else 0,
                        1 if y == y_width - 1 else 0,
                        1 if x == 0 else 0])
        maze.append(row)

    maze[0][0] = [1, 0, 0, 0]
    maze[y_width-1][x_width-1] = [0,0,1,0]

    return add_walls(maze, 0, x_width-1, 0, y_width-1)

def add_walls(maze, x0, x1, y0, y1):
    if x1 - x0 == 0 or y1 - y0 == 0:
        return maze
    elif x1 - x0 < y1 - y0:
        direction = 1
    elif x1 - x0 > y1 - y0:
        direction = 0
    else:
        direction = randint(0, 1)
    if direction == 0:
        wall_line = randint(x0+1, x1)
        wall_hole = randint(y0, y1)
        for y in range(y0, y1+1):
            if y != wall_hole:
                maze[y][wall_line - 1][1] = 1
                maze[y][wall_line][3] = 1
        maze = add_walls(maze, x0, wall_line - 1, y0, y1)
        maze = add_walls(maze, wall_line, x1, y0, y1)
    if direction == 1:
        wall_line = randint(y0+1, y1)
        wall_hole = randint(x0, x1)
        for x in range(x0, x1+1):
            if x != wall_hole:
                maze[wall_line - 1][x][2] = 1
                maze[wall_line][x][0] = 1
        maze = add_walls(maze, x0, x1, y0, wall_line - 1)
        maze = add_walls(maze, x0, x1, wall_line, y1)
    return maze

def make_pretty_maze(m):
    pretty = []
    for row in range(len(m) * 2 + 1):
        pretty_row = []
        for col in range(len(m[row//2 - 1]) * 2 + 1):
            if row % 2 == 0 and col % 2 == 0:
                # corners
                pretty_row.append("#")
            elif row % 2 == 1 and col % 2 == 1:
                # spaces
                pretty_row.append("-")
            elif row == len(m) * 2:
                # bottoms [2] at end of rows
                pretty_row.append("-" if m[row//2 - 1][col//2][2] == 0 else "#")
            elif col == len(m[row//2 - 1]) * 2:
                # rights [1] at end of cols
                pretty_row.append("-" if m[row//2][col//2 - 1][1] == 0 else "#")
            elif row % 2 == 0 and col % 2 == 1:
                # tops [0]
                pretty_row.append("-" if m[row//2][col//2][0] == 0 else "#")
            elif row % 2 == 1 and col % 2 == 0:
                # lefts [3]
                test = m[row // 2][col // 2][3]
                pretty_row.append("-" if m[row//2][col//2][3] == 0 else "#")
        pretty.append(pretty_row)
    return pretty

"""
m1 = [[[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,1,0],[1,1,1,0]],
      [[0,1,0,1],[0,1,0,1],[0,0,1,1],[1,0,1,0],[1,1,0,0]],
      [[0,1,0,1],[0,1,0,1],[1,0,0,1],[1,0,1,0],[0,1,1,0]],
      [[0,1,0,1],[0,1,0,1],[0,0,1,1],[1,0,1,0],[1,1,0,0]],
      [[0,1,1,1],[0,0,1,1],[1,0,1,0],[1,1,1,0],[0,0,1,1]]]

m2 = make_maze(10,10)
print_maze(m2)"""