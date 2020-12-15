def one(line):
    nums = {}
    for i, num in enumerate(line[:-1]):
        nums[num] = i
    said = line.copy()
    for i in range(len(line) - 1, 2020):
        prev_num = said[-1]
        if prev_num in nums:
            num = i - nums[prev_num]
        else:
            num = 0
        nums[prev_num] = i
        said.append(num)
    return said[2019]


def two(line):
    nums = {}
    for i, num in enumerate(line[:-1]):
        nums[num] = i
    said = line.copy()
    for i in range(len(line) - 1, 30000000):
        prev_num = said[-1]
        if prev_num in nums:
            num = i - nums[prev_num]
        else:
            num = 0
        nums[prev_num] = i
        said.append(num)
    return said[30000000 - 1]


if __name__ == '__main__':
    with open('inputs/15.txt') as f:
        line = list(map(int, f.read().strip().split(',')))
    print(one(line))
    print(two(line))
