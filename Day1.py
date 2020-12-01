def one(nums):
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if i != j and num1 + num2 == 2020:
                return num1 * num2


def two(nums):
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            for k, num3 in enumerate(nums):
                if i != j and j != k and num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3


if __name__ == '__main__':
    with open('inputs/1.txt') as f:
        lines = f.readlines()
    nums = list(map(int, map(str.strip, lines)))
    print(two(nums))
