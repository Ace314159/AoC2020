required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def one(lines):
    ans = 0
    for passport in lines.split('\n\n'):
        present = set()
        for entry in passport.strip().replace('\n', ' ').split(' '):
            key, value = entry.split(':')
            present.add(key)
        if required_fields.issubset(present):
            ans += 1
    return ans


def two(lines):
    ans = 0
    for passport in lines.split('\n\n'):
        present = set()
        valid = True
        for entry in passport.strip().replace('\n', ' ').split(' '):
            key, value = entry.split(':')
            if key == 'byr':
                if not (value.isdigit() and 1920 <= int(value) <= 2002):
                    valid = False
            elif key == 'iyr':
                if not (value.isdigit() and 2010 <= int(value) <= 2020):
                    valid = False
            elif key == 'eyr':
                if not (value.isdigit() and 2020 <= int(value) <= 2030):
                    valid = False
            elif key == 'hgt':
                if value[-2:] in {'in', 'cm'}:
                    isCm = value[-2:] == 'cm'
                    num = value[:-2]
                    if num.isdigit():
                        if isCm and 150 <= int(num) <= 193:
                            pass
                        elif not isCm and 59 <= int(num) <= 76:
                            pass
                        else:
                            valid = False
                    else:
                        valid = False
                else:
                    valid = False
            elif key == 'hcl':
                if value[0] == '#' and len(value) == 7:
                    try:
                        int(value[1:], 16)
                    except ValueError:
                        valid = False
                else:
                    valid = False
            elif key == 'ecl':
                if value not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                    valid = False
            elif key == 'pid':
                if not (value.isdigit() and len(value) == 9):
                    valid = False
            present.add(key)
        if required_fields.issubset(present) and valid:
            ans += 1
    return ans


if __name__ == '__main__':
    with open('inputs/4.txt') as f:
        lines = f.read()
    print(one(lines))
    print(two(lines))
