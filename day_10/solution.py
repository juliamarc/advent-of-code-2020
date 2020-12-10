import re

from collections import Counter
from itertools import combinations, starmap, chain
from functools import reduce


def get_chain_diffs(ch):
    idx = zip(range(1, len(ch)), range(0, len(ch) - 1))
    diffs = starmap(lambda i, j: ch[i] - ch[j], idx)

    return list(diffs)


def is_chain_valid(ch):
    return all(map(lambda d: d < 4, get_chain_diffs(ch)))


def main():
    with open('input') as f:
        lines = f.read().splitlines()

    numbers = sorted(map(int, lines))
    numbers = [0, *numbers, numbers[-1] + 3]

    diffs = get_chain_diffs(numbers)
    diffs_cntr = Counter(diffs)

    part_one = diffs_cntr[1] * diffs_cntr[3]

    diffs_str = ''.join(map(str, diffs))
    diffs_repl = re.sub(r'[3]+.?', lambda m: len(m.group()) * 'x', diffs_str)
    diffs_repl = 'x' + diffs_repl[1:]
    diffs_ranges = map(lambda s: s.span(), re.finditer('[12]+', diffs_repl))

    def valid_combs(i, j):
        comb_nums, l_n, r_n = numbers[i:j], numbers[i-1], numbers[j]
        comb_range = range(0, j - i + 1)
        combs = map(lambda c: combinations(comb_nums, c), comb_range)
        to_check = map(lambda c: [l_n, *c, r_n], map(sorted, chain(*combs)))

        return sum(map(is_chain_valid, to_check))

    part_two = reduce(lambda x, y: x * y, starmap(valid_combs, diffs_ranges))

    print("--- Part One ---", part_one, sep='\n')
    print("--- Part Two ---", part_two, sep='\n')


if __name__ == "__main__":
    main()
