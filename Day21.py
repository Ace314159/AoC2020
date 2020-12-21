from collections import Counter


def one(lines):
    allergen_ingredients = {}
    counter = Counter()
    for line in lines:
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split(' ')
        allergens = allergens[:-1].split(', ')

        for ingredient in ingredients:
            counter[ingredient] += 1
        ingredients = set(ingredients)
        for allergen in allergens:
            if allergen in allergen_ingredients:
                allergen_ingredients[allergen].intersection_update(ingredients)
            else:
                allergen_ingredients[allergen] = ingredients.copy()

    bad_ingredients = set()
    for ingredients in allergen_ingredients.values():
        bad_ingredients = bad_ingredients.union(ingredients)

    ans = 0
    for ingredient, count in counter.items():
        if ingredient not in bad_ingredients:
            ans += count
    return ans


def two(lines):
    allergen_ingredients = {}
    counter = Counter()
    for line in lines:
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split(' ')
        allergens = allergens[:-1].split(', ')

        for ingredient in ingredients:
            counter[ingredient] += 1
        ingredients = set(ingredients)
        for allergen in allergens:
            if allergen in allergen_ingredients:
                allergen_ingredients[allergen].intersection_update(ingredients)
            else:
                allergen_ingredients[allergen] = ingredients.copy()

    final_allergens = {}
    while True:
        changed = False
        new_allergen_ingredients = {}
        for allergen, ingredients in allergen_ingredients.items():
            for ingredient in final_allergens.values():
                if ingredient in ingredients:
                    ingredients.remove(ingredient)
            if len(ingredients) == 1:
                final_allergens[allergen] = next(iter(ingredients))
                changed = True
            else:
                new_allergen_ingredients[allergen] = ingredients
        allergen_ingredients = new_allergen_ingredients
        if not changed:
            break

    ans = []
    for allergen in sorted(final_allergens.keys()):
        ans.append(final_allergens[allergen])
    return ','.join(ans)


if __name__ == '__main__':
    with open('inputs/21.txt') as f:
        lines = f.read().strip().splitlines()
    print(one(lines))
    print(two(lines))
