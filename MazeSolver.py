class MazeSolver:
    def __init__(self, maze):
        self.maze = maze

    def solve_generator(self):
        path_q = [(0,0)]
        direction_q = [-1]
        while True:
            place = path_q.pop()
            direction = direction_q.pop() + 1
            if direction == 4:
                continue
            if self.maze[place[0]][place[1]][direction] == -1:
                path_q.append(place)
                yield path_q
                return
            elif self.maze[place[0]][place[1]][direction] == 0:
                path_q.append(place)
                direction_q.append(direction)
                if direction == 0 and (place[0] - 1, place[1]) not in path_q:
                    path_q.append((place[0] - 1, place[1]))
                    direction_q.append(-1)
                elif direction == 1 and (place[0], place[1] + 1) not in path_q:
                    path_q.append((place[0], place[1] + 1))
                    direction_q.append(-1)
                elif direction == 2 and (place[0] + 1, place[1]) not in path_q:
                    path_q.append((place[0] + 1, place[1]))
                    direction_q.append(-1)
                elif direction == 3 and (place[0], place[1] - 1) not in path_q:
                    path_q.append((place[0], place[1] - 1))
                    direction_q.append(-1)
                yield path_q
            elif self.maze[place[0]][place[1]][direction] == 1:
                path_q.append(place)
                direction_q.append(direction)



