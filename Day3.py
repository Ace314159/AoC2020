def one(lines):
    pos = [0, 0]
    count = 0
    while pos[1] < len(lines):
        if lines[pos[1]][pos[0]] == '#':
            count += 1
        pos[0] = (pos[0] + 3) % len(lines[0])
        pos[1] += 1
    return count


def two(lines):
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    ans = 1
    for slope in slopes:
        count = 0
        pos = [0, 0]
        while pos[1] < len(lines):
            if lines[pos[1]][pos[0]] == '#':
                count += 1
            pos[0] = (pos[0] + slope[0]) % len(lines[0])
            pos[1] += slope[1]
        ans *= count
    return ans


if __name__ == '__main__':
    with open('inputs/3.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(one(lines))
    print(two(lines))
