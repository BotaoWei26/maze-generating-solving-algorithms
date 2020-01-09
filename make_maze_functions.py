from random import randint, sample

def make_maze_recursive_division(x_width, y_width, num_holes=1, even=True):
    maze = []
    for y in range(y_width):
        row = []
        for x in range(x_width):
            row.append([1 if y == 0 else 0,
                        1 if x == x_width - 1 else 0,
                        1 if y == y_width - 1 else 0,
                        1 if x == 0 else 0])
        maze.append(row)

    maze[0][0] = [1, 0, 0, -1]
    maze[y_width-1][x_width-1] = [0,-1,1,0]
    return add_walls_recursive_division(maze, 0, x_width - 1, 0, y_width - 1, num_holes, even)


def add_walls_recursive_division(maze, x0, x1, y0, y1, num_holes, even):
    # end condition, if not size of 1x1
    if x1 - x0 == 0 or y1 - y0 == 0:
        return maze

    # direction picker
    if x1 - x0 < y1 - y0:
        direction = 1
    elif x1 - x0 > y1 - y0:
        direction = 0
    else:
        direction = randint(0, 1)

    # adds wall horz
    if direction == 0:
        wall_line = (x0+x1+1)//2 if even else randint(x0+1, x1)
        num_holes = min(y1 - y0, num_holes)
        wall_hole = sample(range(y0, y1 + 1), num_holes)
        for y in range(y0, y1+1):
            if y not in wall_hole:
                maze[y][wall_line - 1][1] = 1
                maze[y][wall_line][3] = 1
        maze = add_walls_recursive_division(maze, x0, wall_line - 1, y0, y1, num_holes, even)
        maze = add_walls_recursive_division(maze, wall_line, x1, y0, y1, num_holes, even)

    # adds wall vert
    if direction == 1:
        wall_line = (y0+y1+1)//2 if even else randint(y0+1, y1)
        num_holes = min(x1 - x0, num_holes)
        wall_hole = sample(range(x0, x1 + 1), num_holes)
        for x in range(x0, x1+1):
            if x not in wall_hole:
                maze[wall_line - 1][x][2] = 1
                maze[wall_line][x][0] = 1
        maze = add_walls_recursive_division(maze, x0, x1, y0, wall_line - 1, num_holes, even)
        maze = add_walls_recursive_division(maze, x0, x1, wall_line, y1, num_holes, even)
    return maze


maze_dict ={
    -1: "+",
    0: "-",
    1: "#"
}


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
                pretty_row.append(maze_dict[m[row//2 - 1][col//2][2]])
            elif col == len(m[row//2 - 1]) * 2:
                # rights [1] at end of cols
                pretty_row.append(maze_dict[m[row//2][col//2 - 1][1]])
            elif row % 2 == 0 and col % 2 == 1:
                # tops [0]
                pretty_row.append(maze_dict[m[row//2][col//2][0]])
            elif row % 2 == 1 and col % 2 == 0:
                # lefts [3]
                test = m[row // 2][col // 2][3]
                pretty_row.append(maze_dict[m[row//2][col//2][3]])
        pretty.append(pretty_row)
    return pretty


def make_pretty_path(p):
    if len(p) == 0:
        return []
    p_path = []
    p_path.append((p[0][0]*2 + 1, p[0][1]*2 + 1))
    for i in range(1, len(p)):
        p_path.append((p[i][0]*2 + 1, p[i][1]*2 + 1))
        p_path.append((p[i][0] + p[i-1][0] + 1, p[i][1] + p[i-1][1] + 1))
    return p_path

"""
m1 = [[[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,1,0],[1,1,1,0]],
      [[0,1,0,1],[0,1,0,1],[0,0,1,1],[1,0,1,0],[1,1,0,0]],
      [[0,1,0,1],[0,1,0,1],[1,0,0,1],[1,0,1,0],[0,1,1,0]],
      [[0,1,0,1],[0,1,0,1],[0,0,1,1],[1,0,1,0],[1,1,0,0]],
      [[0,1,1,1],[0,0,1,1],[1,0,1,0],[1,1,1,0],[0,0,1,1]]]

m2 = make_maze(10,10)
print_maze(m2)"""