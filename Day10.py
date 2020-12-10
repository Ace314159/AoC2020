def one(lines):
    lines.sort()
    lines.sort()
    lines.append(lines[-1] + 3)
    num1 = 0
    num3 = 0

    cur = 0
    for jolt in lines:
        diff = jolt - cur
        if diff == 1:
            num1 += 1
        elif diff == 3:
            num3 += 1
        cur = jolt
    return num1 * num3


def two(lines):
    lines.sort()
    lines.append(lines[-1] + 3)
    mem = {}

    def count(start_index, start_jolt):
        if (start_index, start_jolt) in mem:
            return mem[(start_index, start_jolt)]
        ans = 0
        for i, jolt in enumerate(lines[start_index:], start_index):
            if jolt - start_jolt <= 3:
                if i + 1 < len(lines):
                    ans += count(i + 1, jolt)
                else:
                    ans += 1
            else:
                mem[(start_index, start_jolt)] = ans
                return ans
        mem[(start_index, start_jolt)] = ans
        return ans

    return count(0, 0)


if __name__ == '__main__':
    with open('inputs/10.txt') as f:
        lines = [int(line.strip()) for line in f.readlines()]
    print(one(lines))
    print(two(lines))
