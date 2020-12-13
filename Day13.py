def one(lines):
    time = int(lines[0])
    min_time_wait = None
    min_id = None
    for id in lines[1].split(','):
        if id == 'x':
            continue
        id = int(id)
        time_wait = id - time % id
        if not min_time_wait or time_wait < min_time_wait:
            min_time_wait = time_wait
            min_id = id
    return min_id * min_time_wait


def two(lines):
    nums = []
    for i, id in enumerate(lines[1].split(',')):
        if id == 'x':
            continue
        nums.append((-i, int(id)))

    ans, modulo_prod = nums[0]
    for num, modulo in nums[1:]:
        # Extended GCD of modulo_prod and modulo
        s = 0
        old_s = 1
        r = modulo
        old_r = modulo_prod

        while r != 0:
            quotient = old_r // r
            (old_r, r) = (r, old_r - quotient * r)
            (old_s, s) = (s, old_s - quotient * s)

        bezout_t = (old_r - old_s * modulo_prod) // modulo
        bezout = (old_s, bezout_t)
        # Construct solution
        ans = num * bezout[0] * modulo_prod + ans * bezout[1] * modulo
        modulo_prod *= modulo
        ans %= modulo_prod
    return ans


if __name__ == '__main__':
    with open('inputs/13.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(one(lines))
    print(two(lines))
