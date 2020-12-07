import collections


def one(lines):
    # Bag --> What bags contain it
    bags = collections.defaultdict(set)
    for rule in lines:
        outer, inner = rule[:-1].split(' contain ')
        outer = outer[:-5]
        for bag in inner.split(', '):
            if 'no other bags' in bag:
                continue
            color = ' '.join(bag.split(' ')[1:-1])
            bags[color].add(outer)

    def count_bags_in(bag):
        count = 0
        for bag_in in bags[bag]:
            if bag_in not in counted:
                counted.add(bag_in)
                count += 1 + count_bags_in(bag_in)
        return count

    counted = set()
    return count_bags_in('shiny gold')


def two(lines):
    # Bag --> What bags it contains
    bags = collections.defaultdict(set)
    for rule in lines:
        outer, inner = rule[:-1].split(' contain ')
        outer = outer[:-5]
        for bag in inner.split(', '):
            s = bag.split(' ')
            color = ' '.join(s[1:-1])
            if 'no other bags' not in bag:
                bags[outer].add((int(s[0]), color))

    def count_bags(bag):
        count = 1
        for num, contained_bag in bags[bag]:
            count += num * count_bags(contained_bag)
        return count

    return count_bags('shiny gold') - 1


if __name__ == '__main__':
    with open('inputs/7.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(one(lines))
    print(two(lines))
