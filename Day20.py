from collections import Counter
import math


def one(lines):
    tiles = lines.split('\n\n')
    tile_sides = {}
    all_sides = Counter()
    for tile in tiles:
        tile_lines = tile.splitlines()
        tile_num = int(tile_lines[0].split(' ')[1][:-1])
        tile_lines = [list(line) for line in tile_lines[1:]]
        tile_sides[tile_num] = Counter()
        for i in [0, -1]:
            side1 = tile_lines[i].copy()
            side2 = [line[i] for line in tile_lines]
            for c in [tile_sides[tile_num], all_sides]:
                c[tuple(side1.copy())] += 1
                c[tuple(side2.copy())] += 1
                c[tuple(reversed(side1.copy()))] += 1
                c[tuple(reversed(side2.copy()))] += 1

    num_unique = {}
    for tile_num, sides in tile_sides.items():
        num_unique[tile_num] = 0
        for side in sides:
            if all_sides[side] - sides[side] == 0:
                num_unique[tile_num] += 1
    ans = 1
    for tile_num, count in num_unique.items():
        if count == 4:
            ans *= tile_num
    return ans


def two(lines):
    tiles = lines.split('\n\n')
    tile_sides = {}
    all_sides = Counter()
    tiles_by_num = {}
    for tile in tiles:
        tile_lines = tile.splitlines()
        tile_num = int(tile_lines[0].split(' ')[1][:-1])
        tile_lines = [list(line) for line in tile_lines[1:]]
        tile_sides[tile_num] = Counter()
        for i in [0, -1]:
            side1 = tile_lines[i].copy()
            side2 = [line[i] for line in tile_lines]
            for c in [tile_sides[tile_num], all_sides]:
                c[tuple(side1.copy())] += 1
                c[tuple(side2.copy())] += 1
                c[tuple(reversed(side1.copy()))] += 1
                c[tuple(reversed(side2.copy()))] += 1
        tiles_by_num[tile_num] = tile_lines.copy()

    corner = None
    for tile_num, sides in tile_sides.items():
        num_unique = 0
        for side in sides:
            if all_sides[side] - sides[side] == 0:
                num_unique += 1
        if num_unique == 4:
            corner = tile_num
            break

    def rotate(lines):
        new_lines = []
        for col_i in range(len(lines)):
            new_lines.append([line[col_i] for line in reversed(lines)])
        return new_lines

    def flip(lines):
        for line in lines:
            line.reverse()

    size = int(math.sqrt(len(tiles_by_num)))
    tiles_by_num[corner].reverse()
    map = []
    for y in range(size):
        map.append([])
        for x in range(size):
            if x == 0 and y == 0:
                map[y].append(tiles_by_num.pop(corner))
                continue
            found = False
            for tile_num in tiles_by_num:
                for _ in range(2):
                    for _ in range(4):
                        tile = tiles_by_num[tile_num]
                        fits = True
                        if y != 0 and map[y - 1][x][-1] != tile[0]:
                            fits = False
                        if fits and x != 0 and [line[-1] for line in map[y][x - 1]] != [line[0] for line in tile]:
                            fits = False
                        if fits:
                            found = True
                            map[y].append(tiles_by_num.pop(tile_num))
                            break
                        else:
                            tiles_by_num[tile_num] = rotate(tiles_by_num[tile_num])
                    if found:
                        break
                    flip(tiles_by_num[tile_num])
                if found:
                    break
            if not found:
                print('Missing', x, y)

    tile_size = len(map[0][0]) - 2
    map_lines = [[] for _ in range(size * tile_size)]
    for tile_y, y_tiles in enumerate(map):
        y_offset = tile_size * tile_y
        for tile in y_tiles:
            for y, line in enumerate(tile[1:-1]):
                map_lines[y_offset + y].extend(line[1:-1])

    sea_monster = ["                  # ",
                   "#    ##    ##    ###",
                   " #  #  #  #  #  #   ",
                   ]

    num_mon = 0
    for _ in range(2):
        for _ in range(4):
            for mon_y in range(len(map_lines) - len(sea_monster)):
                for mon_x in range(len(map_lines[0]) - len(sea_monster[0])):
                    is_mon = True
                    for y, mon_line in enumerate(sea_monster):
                        for x, mon_char in enumerate(mon_line):
                            if mon_char == '#' and map_lines[mon_y + y][mon_x + x] != '#':
                                is_mon = False
                    if is_mon:
                        num_mon += 1
            if num_mon == 0:
                map_lines = rotate(map_lines)
            else:
                break
        if num_mon == 0:
            flip(map_lines)
        else:
            break

    mon_count = 0
    for line in sea_monster:
        mon_count += line.count('#')
    total_count = 0
    for line in map_lines:
        total_count += line.count('#')
    return total_count - mon_count * num_mon


if __name__ == '__main__':
    with open('inputs/20.txt') as f:
        lines = f.read().strip()
    print(one(lines))
    print(two(lines))
