def one(lines):
    ans = 0
    for line in lines:
        id = int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)
        ans = max(ans, id)
    return ans


def two(lines):
    full_seats = [False for _ in range(1024)]
    for line in lines:
        id = int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)
        full_seats[id] = True
    for i, is_full in enumerate(full_seats):
        if not is_full and full_seats[i - 1] and full_seats[i + 1]:
            return i


if __name__ == '__main__':
    with open('inputs/5.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(one(lines))
    print(two(lines))
