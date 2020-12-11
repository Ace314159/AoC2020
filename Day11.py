def one(state):
    while True:
        new_state = [line.copy() for line in state]
        for y, line in enumerate(state):
            for x, seat in enumerate(line):
                if seat == '.':
                    continue
                adj = []
                for y_diff in range(-1, 1 + 1):
                    for x_diff in range(-1, 1 + 1):
                        if x_diff == 0 and y_diff == 0:
                            continue
                        check_x = x + x_diff
                        check_y = y + y_diff
                        if check_x >= 0 and check_x < len(line) and check_y >= 0 and check_y < len(state):
                            adj.append(state[check_y][check_x])

                if seat == 'L' and all((s in ['L', '.'] for s in adj)):
                    new_state[y][x] = '#'
                elif adj.count('#') >= 4:
                    new_state[y][x] = 'L'
        if new_state == state:
            break
        state = new_state
    ans = 0
    for line in state:
        for seat in line:
            if seat == '#':
                ans += 1
    return ans


def two(state):
    while True:
        new_state = [line.copy() for line in state]
        for y, line in enumerate(state):
            for x, seat in enumerate(line):
                if seat == '.':
                    continue
                adj = []
                for y_diff in range(-1, 1 + 1):
                    for x_diff in range(-1, 1 + 1):
                        if x_diff == 0 and y_diff == 0:
                            continue
                        check_x = x + x_diff
                        check_y = y + y_diff
                        while True:
                            if check_x < 0 or check_x >= len(line) or check_y < 0 or check_y >= len(state):
                                break
                            if state[check_y][check_x] == '.':
                                check_x += x_diff
                                check_y += y_diff
                            else:
                                adj.append(state[check_y][check_x])
                                break

                if seat == 'L' and all((s in ['L', '.'] for s in adj)):
                    new_state[y][x] = '#'
                elif adj.count('#') >= 5:
                    new_state[y][x] = 'L'
        if new_state == state:
            break
        state = new_state
    ans = 0
    for line in state:
        for seat in line:
            if seat == '#':
                ans += 1
    return ans


if __name__ == '__main__':
    with open('inputs/11.txt') as f:
        lines = [list(line.strip()) for line in f.readlines()]
    print(one(lines))
    print(two(lines))
