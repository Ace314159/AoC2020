import collections


def one(lines):
    active = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                active.add((x, y, 0))

    for _ in range(6):
        new_active = set()
        check = collections.deque(active.copy())
        checked = set()
        while len(check) > 0:
            pos = check.popleft()
            x, y, z = pos
            checked.add(pos)
            is_active = pos in active
            neighbors_active = 0
            for x_diff in range(-1, 1 + 1):
                for y_diff in range(-1, 1 + 1):
                    for z_diff in range(-1, 1 + 1):
                        if x_diff == 0 and y_diff == 0 and z_diff == 0:
                            continue
                        check_pos = (x + x_diff, y + y_diff, z + z_diff)
                        if pos in active and check_pos not in checked:
                            check.append(check_pos)
                        if check_pos in active:
                            neighbors_active += 1
            if is_active and neighbors_active in [2, 3] or not is_active and neighbors_active == 3:
                new_active.add(pos)
        active = new_active

    return len(active)


def two(lines):
    active = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                active.add((x, y, 0, 0))

    for _ in range(6):
        new_active = set()
        check = collections.deque(active.copy())
        checked = set()
        while len(check) > 0:
            pos = check.popleft()
            x, y, z, w = pos
            checked.add(pos)
            is_active = pos in active
            neighbors_active = 0
            for x_diff in range(-1, 1 + 1):
                for y_diff in range(-1, 1 + 1):
                    for z_diff in range(-1, 1 + 1):
                        for w_diff in range(-1, 1 + 1):
                            if x_diff == 0 and y_diff == 0 and z_diff == 0 and w_diff == 0:
                                continue
                            check_pos = (x + x_diff, y + y_diff, z + z_diff, w + w_diff)
                            if pos in active and check_pos not in checked:
                                check.append(check_pos)
                            if check_pos in active:
                                neighbors_active += 1
            if is_active and neighbors_active in [2, 3] or not is_active and neighbors_active == 3:
                new_active.add(pos)
        active = new_active

    return len(active)


if __name__ == '__main__':
    with open('inputs/17.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(one(lines))
    print(two(lines))
