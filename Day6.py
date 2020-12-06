def one(lines):
    ans = 0
    for group in lines.split('\n\n'):
        answers = set()
        for person in group.split('\n'):
            answers.update(list(person))
        ans += len(answers)
    return ans


def two(lines):
    ans = 0
    for group in lines.split('\n\n'):
        answers = set(list(group.split('\n')[0]))
        for person in group.strip().split('\n'):
            answers.intersection_update(list(person))
        ans += len(answers)
    return ans


if __name__ == '__main__':
    with open('inputs/6.txt') as f:
        lines = f.read()
    print(one(lines))
    print(two(lines))
