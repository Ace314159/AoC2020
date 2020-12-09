import collections


def one(nums):
    preamble = collections.deque(nums[:25])
    for num in nums[25:]:
        found = False
        for i, a in enumerate(preamble):
            for j, b in enumerate(preamble):
                if i != j and a + b == num:
                    found = True
                    break
            if found:
                break
        if not found:
            return num
        preamble.popleft()
        preamble.append(num)


def two(nums, check):
    for i in range(len(nums)):
        for j in range(len(nums)):
            slice = nums[i:j + 1]
            if sum(slice) == check:
                return min(slice) + max(slice)


if __name__ == '__main__':
    with open('inputs/9.txt') as f:
        lines = [int(line.strip()) for line in f.readlines()]
    ans1 = one(lines)
    print(ans1)
    print(two(lines, ans1))
