def one(lines):
    ran = set()
    acc = 0
    pc = 0

    while True:
        if pc in ran:
            return acc
        ran.add(pc)
        op, arg = lines[pc]
        arg = int(arg)
        if op == 'acc':
            acc += arg
            pc += 1
        elif op == 'nop':
            pc += 1
        elif op == 'jmp':
            pc += arg


def two(lines):
    swap = {'jmp': 'nop', 'nop': 'jmp'}
    for i, (old_op, old_arg) in enumerate(lines):
        if old_op not in swap:
            continue
        new_lines = lines.copy()
        new_lines[i] = [swap[old_op], old_arg]

        ran = set()
        acc = 0
        pc = 0
        looped = False
        while pc < len(lines):
            if pc in ran:
                looped = True
                break
            ran.add(pc)
            op, arg = new_lines[pc]
            arg = int(arg)
            if op == 'acc':
                acc += arg
                pc += 1
            elif op == 'nop':
                pc += 1
            elif op == 'jmp':
                pc += arg
        if not looped:
            return acc


if __name__ == '__main__':
    with open('inputs/8.txt') as f:
        lines = [line.strip().split(' ') for line in f.readlines()]
    print(one(lines))
    print(two(lines))
