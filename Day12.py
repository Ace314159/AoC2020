def one(lines):
    pos = [0, 0]
    dir = [1, 0]
    for instr in lines:
        action = instr[0]
        num = int(instr[1:])
        if action == 'N':
            pos[1] += num
        elif action == 'S':
            pos[1] -= num
        elif action == 'E':
            pos[0] += num
        elif action == 'W':
            pos[0] -= num
        elif action == 'L':
            num %= 360
            while num > 0:
                dir = [-dir[1], dir[0]]
                num -= 90
        elif action == 'R':
            num %= 360
            num = 360 - num
            while num > 0:
                while num > 0:
                    dir = [-dir[1], dir[0]]
                    num -= 90
        elif action == 'F':
            pos = [pos[0] + dir[0] * num, pos[1] + dir[1] * num]
    return abs(pos[0]) + abs(pos[1])


def two(lines):
    way_pos = [10, 1]  # Relative pos
    ship_pos = [0, 0]
    for instr in lines:
        action = instr[0]
        num = int(instr[1:])
        if action == 'N':
            way_pos[1] += num
        elif action == 'S':
            way_pos[1] -= num
        elif action == 'E':
            way_pos[0] += num
        elif action == 'W':
            way_pos[0] -= num
        elif action == 'L':
            num %= 360
            while num > 0:
                way_pos = [-way_pos[1], way_pos[0]]
                num -= 90
        elif action == 'R':
            num %= 360
            num = 360 - num
            while num > 0:
                while num > 0:
                    way_pos = [-way_pos[1], way_pos[0]]
                    num -= 90
        elif action == 'F':
            ship_pos = [ship_pos[0] + way_pos[0] * num, ship_pos[1] + way_pos[1] * num]
    return abs(ship_pos[0]) + abs(ship_pos[1])


if __name__ == '__main__':
    with open('inputs/12.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(one(lines))
    print(two(lines))
