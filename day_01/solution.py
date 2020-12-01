import sys

from itertools import combinations
from functools import reduce


def main():
    input_file_name = 'input'
    n = int(sys.argv[1])

    with open(input_file_name) as f:
        lines = f.read().splitlines()

    combs = list(combinations(map(int, lines), n))
    for comb in combs:
        if sum(comb) == 2020:
            print(reduce(lambda x, y: x*y, comb))


if __name__ == "__main__":
    main()
