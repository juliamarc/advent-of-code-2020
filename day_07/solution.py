import re

from collections import deque


def main():
    my_bag = 'shiny gold'

    with open('input') as f:
        lines = f.read().splitlines()

    re_bag = re.compile(r'(\w+\s\w+)\sbags\scontain')
    re_rules = re.compile(r'(\d+)\s(\w+\s\w+) bags?')

    def parse(line):
        bag, rules = re_bag.match(line).group(1), re_rules.findall(line)
        bag_dict = {}
        deque(map(lambda r: bag_dict.update({r[1]: int(r[0])}), rules))

        return bag, bag_dict

    rules_dict = {}
    deque(map(lambda r: rules_dict.update({r[0]: r[1]}), map(parse, lines)))

    def can_carry(bag, searched_bag=my_bag):
        bag_dict = rules_dict[bag]
        if not bool(bag_dict):
            return False
        elif searched_bag in bag_dict:
            return True
        else:
            return any(map(lambda kv: can_carry(kv[0], searched_bag), bag_dict.items()))

    part_one = sum(map(lambda kv: can_carry(kv[0]), rules_dict.items()))

    def capacity(bag=my_bag):
        bag_dict = rules_dict[bag]
        if not bool(bag_dict):
            return 0
        else:
            return sum(map(lambda kv: kv[1] + kv[1] * capacity(kv[0]), bag_dict.items()))

    part_two = capacity()

    print("--- Part One ---", part_one, sep='\n')
    print("--- Part Two ---", part_two, sep='\n')


if __name__ == "__main__":
    main()
