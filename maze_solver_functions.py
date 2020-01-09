direction_dict = {
    "up": 0,
    "right": 1,
    "down": 2,
    "left": 3
}


def solve_generator_depth_first(maze, pref="right", memory=True):
    dir_pref = direction_dict[pref]
    path_q = [(0,0)]
    all_path = [(0,0)]
    direction_q = [0]
    while True:
        yield path_q
        place = path_q[-1]
        direction = direction_q[-1]

        # all directions checked
        if direction == 4:
            path_q.pop()
            direction_q.pop()
            continue

        # end reached
        if maze[place[0]][place[1]][direction] == -1:
            yield path_q
            return

        # no wall in direction
        direction_q[-1] += 1
        if maze[place[0]][place[1]][(direction + dir_pref) % 4] == 0:
            if (direction + dir_pref) % 4 == 0 and (place[0] - 1, place[1]) not in path_q and \
                    (not memory or (place[0] - 1, place[1]) not in all_path):
                path_q.append((place[0] - 1, place[1]))
                direction_q.append(0)
                if memory:
                    all_path.append(path_q[-1])
            elif (direction + dir_pref) % 4 == 1 and (place[0], place[1] + 1) not in path_q and \
                    (not memory or (place[0], place[1] + 1) not in all_path):
                path_q.append((place[0], place[1] + 1))
                direction_q.append(0)
                if memory:
                    all_path.append(path_q[-1])
            elif (direction + dir_pref) % 4 == 2 and (place[0] + 1, place[1]) not in path_q and \
                    (not memory or (place[0] + 1, place[1]) not in all_path):
                path_q.append((place[0] + 1, place[1]))
                direction_q.append(0)
                if memory:
                    all_path.append(path_q[-1])
            elif (direction + dir_pref) % 4 == 3 and (place[0], place[1] - 1) not in path_q and \
                    (not memory or (place[0], place[1] - 1) not in all_path):
                path_q.append((place[0], place[1] - 1))
                direction_q.append(0)
                if memory:
                    all_path.append(path_q[-1])






