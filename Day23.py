def one(line):
    start = None
    cups = {}
    prev = None
    for cup in map(int, list(line)):
        if not start:
            start = cup
            prev = start
        cups[prev] = cup
        prev = cup
    cups[prev] = start
    cur = start
    min_cups = min(cups)
    max_cups = max(cups)
    for _ in range(100):
        first_removed = cups[cur]
        middle = cups[first_removed]
        last_removed = cups[middle]
        after_removed = cups[last_removed]
        removed = set([first_removed, middle, last_removed])
        dest = cur - 1
        while dest < min_cups or dest in removed:
            dest -= 1
            if dest < min_cups:
                dest = max_cups
        end = cups[dest]
        cups[dest] = first_removed
        cups[last_removed] = end
        cups[cur] = after_removed
        cur = cups[cur]

    ans = ''
    cur = cups[1]
    while cur != 1:
        ans += str(cur)
        cur = cups[cur]
    return ans


def two(line):
    start = None
    cups = {}
    prev = None
    for cup in map(int, list(line)):
        if not start:
            start = cup
            prev = start
        cups[prev] = cup
        prev = cup
    cur = start
    for i in range(max(cups) + 1, 1000000 + 1):
        cups[prev] = i
        prev = i
    cups[prev] = start
    min_cups = 1
    max_cups = 1000000
    for i in range(10000000):
        first_removed = cups[cur]
        middle = cups[first_removed]
        last_removed = cups[middle]
        after_removed = cups[last_removed]
        removed = set([first_removed, middle, last_removed])
        dest = cur - 1
        while dest < min_cups or dest in removed:
            dest -= 1
            if dest < min_cups:
                dest = max_cups
        end = cups[dest]
        cups[dest] = first_removed
        cups[last_removed] = end
        cups[cur] = after_removed
        cur = cups[cur]

    return cups[1] * cups[cups[1]]


if __name__ == '__main__':
    with open('inputs/23.txt') as f:
        lines = f.read().strip()
    print(one(lines))
    print(two(lines))
