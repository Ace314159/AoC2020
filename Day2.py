def one(lines):
    ans = 0
    for line in lines:
        r, char, password = line.split(' ')
        r = list(map(int, r.split('-')))
        char = char[0]
        count = password.count(char)
        if count >= r[0] and count <= r[1]:
            ans += 1
    return ans


def two(nums):
    ans = 0
    for line in lines:
        [r, char, password] = line.split(' ')
        r = list(map(int, r.split('-')))
        char = char[0]
        correct = 0
        for val in r:
            if password[val - 1] == char:
                correct += 1
        if correct == 1:
            ans += 1
    return ans


if __name__ == '__main__':
    with open('inputs/2.txt') as f:
        lines = list(map(lambda x: x[:-1], f.readlines()))
    print(two(lines))
