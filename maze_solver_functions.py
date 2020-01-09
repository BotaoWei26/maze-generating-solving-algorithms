def solve_generator_depth_first(maze, pref=("right", "down", "left", "up"), memory=True):
    direction_pref = {
        "up": 0,
        "right": 1,
        "down": 2,
        "left": 3
    }
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
        if maze[place[0]][place[1]][direction_pref[pref[direction]]] == -1:
            yield path_q
            return

        # no wall in direction
        direction_q[-1] += 1
        new_path_added = False
        if maze[place[0]][place[1]][direction_pref[pref[direction]]] == 0:
            if pref[direction] == "up" and (place[0] - 1, place[1]) not in path_q and \
                    (not memory or (place[0] - 1, place[1]) not in all_path):
                path_q.append((place[0] - 1, place[1]))
                direction_q.append(0)
                new_path_added = True
            elif pref[direction] == "right" and (place[0], place[1] + 1) not in path_q and \
                    (not memory or (place[0], place[1] + 1) not in all_path):
                path_q.append((place[0], place[1] + 1))
                direction_q.append(0)
                new_path_added = True
            elif pref[direction] == "down" and (place[0] + 1, place[1]) not in path_q and \
                    (not memory or (place[0] + 1, place[1]) not in all_path):
                path_q.append((place[0] + 1, place[1]))
                direction_q.append(0)
                new_path_added = True
            elif pref[direction] == "left" and (place[0], place[1] - 1) not in path_q and \
                    (not memory or (place[0], place[1] - 1) not in all_path):
                path_q.append((place[0], place[1] - 1))
                direction_q.append(0)
                new_path_added = True
        if new_path_added:
            all_path.append(path_q[-1])





