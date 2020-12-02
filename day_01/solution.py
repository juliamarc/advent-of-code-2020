from itertools import combinations
from functools import reduce


def combination_product(numbers, n):
    combs = combinations(numbers, n)
    filtered = list(filter(lambda c: sum(c) == 2020, combs))
    return reduce(lambda x, y: x*y, filtered[0])


def main():
    with open('input') as f:
        lines = f.read().splitlines()

    numbers = list(map(int, lines))

    print("--- Part One ---", combination_product(numbers, 2), sep='\n')
    print("--- Part Two ---", combination_product(numbers, 3), sep='\n')


if __name__ == "__main__":
    main()
