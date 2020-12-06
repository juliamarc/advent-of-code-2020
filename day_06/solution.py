import re

from functools import reduce


def main():
    with open('input') as f:
        lines = f.read().strip().split('\n\n')

    regexp = r'(\s|\u180B|\u200B|\u200C|\u200D|\u2060|\uFEFF)+'
    part_one = sum(map(lambda l: len(set(re.sub(regexp, '', l))), lines))

    ans_sets = map(lambda l: map(set, l.split('\n')), lines)
    part_two = sum(map(lambda a: len(reduce(lambda x, y: x & y, a)), ans_sets))

    print("--- Part One ---", part_one, sep='\n')
    print("--- Part Two ---", part_two, sep='\n')


if __name__ == "__main__":
    main()
