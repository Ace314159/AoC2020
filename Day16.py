def one(lines):
    fields, your, nearby = [l.split('\n') for l in lines.split('\n\n')]
    your = list(map(int, your[1].split(',')))
    nearby = [list(map(int, l.split(','))) for l in nearby[1:-1]]

    ranges = []
    for field in fields:
        _, nums = field.split(': ')
        range1, range2 = [r.split('-') for r in nums.split(' or ')]
        ranges.append(range(int(range1[0]), int(range1[1]) + 1))
        ranges.append(range(int(range2[0]), int(range2[1]) + 1))

    ans = 0
    for ticket in nearby:
        for num in ticket:
            bad = True
            for r in ranges:
                if num in r:
                    bad = False
                    break
            if bad:
                ans += num
    return ans


def two(lines):
    fields, your, nearby = [l.split('\n') for l in lines.split('\n\n')]
    your = list(map(int, your[1].split(',')))
    nearby = [list(map(int, l.split(','))) for l in nearby[1:-1]]

    ranges = []
    names = {}
    for field in fields:
        name, nums = field.split(': ')
        range1, range2 = [r.split('-') for r in nums.split(' or ')]
        names[name] = len(ranges)
        ranges.append([
            range(int(range1[0]), int(range1[1]) + 1),
            range(int(range2[0]), int(range2[1]) + 1),
        ])

    good_tickets = set(range(len(nearby)))
    for i, ticket in enumerate(nearby):
        for num in ticket:
            bad = True
            for r in ranges:
                if num in r[0] or num in r[1]:
                    bad = False
                    break
            if bad:
                good_tickets.remove(i)
                break

    possibilities = []
    for i in range(len(ranges)):
        good = set(range(len(ranges)))
        for ticket_i in good_tickets:
            ticket = nearby[ticket_i]
            new_good = set()
            for range_i in good:
                if ticket[i] in ranges[range_i][0] or ticket[i] in ranges[range_i][1]:
                    new_good.add(range_i)
            good = new_good
        possibilities.append(good)

    order = [None for _ in range(len(ranges))]
    done = False
    while not done:
        done = True
        for i, possibility in enumerate(possibilities):
            if len(possibility) == 1:
                num = possibility.pop()
                order[i] = num
                for p in possibilities:
                    if num in p:
                        p.remove(num)
                        done = False

    ans = 1
    for name, i in names.items():
        if name.startswith('departure'):
            ans *= your[order.index(i)]
    return ans


if __name__ == '__main__':
    with open('inputs/16.txt') as f:
        lines = f.read()
    print(one(lines))
    print(two(lines))
