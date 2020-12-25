def one(lines):
    keys = list(map(int, lines))
    loop_sizes = []
    for key in keys:
        loop_size = 1
        value = 1
        while True:
            value *= 7
            value %= 20201227
            if value == key:
                break
            loop_size += 1
        loop_sizes.append(loop_size)
    if loop_sizes[0] < loop_sizes[1]:
        i = 0
    else:
        i = 1
    value = 1
    for _ in range(loop_sizes[i]):
        value *= keys[1 - i]
        value %= 20201227
    return value


if __name__ == '__main__':
    with open('inputs/25.txt') as f:
        lines = f.read().strip().splitlines()
    print(one(lines))
