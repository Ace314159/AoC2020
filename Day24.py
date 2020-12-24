from collections import defaultdict
import itertools


def one(lines):
    is_black = defaultdict(lambda: False)
    for line in lines:
        line = iter(line)
        pos = [0, 0, 0]
        try:
            while True:
                char = next(line)
                if char == 'e':
                    pos[0] += 1
                    pos[1] -= 1
                elif char == 'w':
                    pos[0] -= 1
                    pos[1] += 1
                elif char == 'n':
                    char = next(line)
                    if char == 'e':
                        pos[0] += 1
                        pos[2] -= 1
                    elif char == 'w':
                        pos[1] += 1
                        pos[2] -= 1
                elif char == 's':
                    char = next(line)
                    if char == 'e':
                        pos[1] -= 1
                        pos[2] += 1
                    elif char == 'w':
                        pos[0] -= 1
                        pos[2] += 1
        except StopIteration:
            pass
        pos = tuple(pos)
        is_black[pos] = not is_black[pos]
    ans = 0
    for val in is_black.values():
        if val:
            ans += 1
    return ans


def two(line):
    is_black = defaultdict(lambda: False)
    for line in lines:
        line = iter(line)
        pos = [0, 0, 0]
        try:
            while True:
                char = next(line)
                if char == 'e':
                    pos[0] += 1
                    pos[1] -= 1
                elif char == 'w':
                    pos[0] -= 1
                    pos[1] += 1
                elif char == 'n':
                    char = next(line)
                    if char == 'e':
                        pos[0] += 1
                        pos[2] -= 1
                    elif char == 'w':
                        pos[1] += 1
                        pos[2] -= 1
                elif char == 's':
                    char = next(line)
                    if char == 'e':
                        pos[1] -= 1
                        pos[2] += 1
                    elif char == 'w':
                        pos[0] -= 1
                        pos[2] += 1
        except StopIteration:
            pass
        pos = tuple(pos)
        if pos in is_black:
            is_black[pos] = not is_black[pos]
        else:
            is_black[pos] = True

    for _ in range(100):
        new_is_black = defaultdict(lambda: False)
        poses = {pos for pos, is_black in is_black.items() if is_black}
        neighbors = set()
        for pos in poses:
            for diff_x, diff_y, diff_z in itertools.permutations([-1, 0, 1]):
                check_pos = (pos[0] + diff_x, pos[1] + diff_y, pos[2] + diff_z)
                neighbors.add(check_pos)
        poses = poses.union(neighbors)
        for pos in poses:
            is_b = is_black[pos]
            num_black = 0
            for diff_x, diff_y, diff_z in itertools.permutations([-1, 0, 1]):
                check_pos = (pos[0] + diff_x, pos[1] + diff_y, pos[2] + diff_z)
                if is_black[check_pos]:
                    num_black += 1
            if is_b and (num_black == 0 or num_black > 2):
                new_is_black[pos] = False
            elif not is_b and num_black == 2:
                new_is_black[pos] = True
            else:
                new_is_black[pos] = is_black[pos]
        is_black = new_is_black
    ans = 0
    for val in is_black.values():
        if val:
            ans += 1
    return ans


if __name__ == '__main__':
    with open('inputs/24.txt') as f:
        lines = f.read().strip().splitlines()
    print(one(lines))
    print(two(lines))
