def one(lines):
    mem = {}
    clear = None
    set = None
    for line in lines:
        if 'mask' in line:
            mask = line.split(' ')[-1]
            clear = int(mask.replace('X', '1'), 2)
            set = int(mask.replace('X', '0'), 2)
        elif 'mem' in line:
            addr = int(line[line.index('[') + 1:line.index(']')])
            val = int(line.split(' ')[-1])
            mem[addr] = (val | set) & clear
    return sum(mem.values())


def two(lines):
    mem = {}
    floating = []
    format_str = None
    set = None

    def write(floating, addr, val):
        if len(floating) > 0:
            i = floating.pop()
            write(floating.copy(), addr[:i] + '0' + addr[i + 1:], val)
            write(floating.copy(), addr[:i] + '1' + addr[i + 1:], val)
        else:
            mem[int(addr, 2)] = val

    for line in lines:
        if 'mask' in line:
            floating.clear()
            mask = line.split(' ')[-1]
            format_str = "{:0" + str(len(mask)) + "b}"
            for i, c in enumerate(mask):
                if c == 'X':
                    floating.append(i)
            set = int(mask.replace('X', '0'), 2)
        elif 'mem' in line:
            addr = int(line[line.index('[') + 1:line.index(']')]) | set
            addr = format_str.format(addr)
            val = int(line.split(' ')[-1])
            write(floating.copy(), addr, val)
    return sum(mem.values())


if __name__ == '__main__':
    with open('inputs/14.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(one(lines))
    print(two(lines))
