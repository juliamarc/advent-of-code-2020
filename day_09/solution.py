from collections import deque

from itertools import islice, combinations, tee


def main():
    with open('input') as f:
        lines = f.read().splitlines()

    numbers, n = tee(map(int, lines)), 25
    prev = deque(islice(numbers[0], n), n)

    def not_sum(num):
        sum_found = num in map(sum, combinations(prev, 2))
        prev.append(num)
        return not sum_found

    part_one = next(filter(not_sum,  numbers[0]))

    cont = deque(islice(numbers[1], 2))

    def slide(num):
        if sum(cont) == part_one:
            return True

        while sum(cont) > part_one and len(cont) > 2:
            cont.popleft()
            if sum(cont) == part_one:
                return True
            elif sum(cont) < part_one:
                break

        cont.append(num)
        return False

    next(filter(slide, numbers[1]))
    part_two = min(cont) + max(cont)

    print("--- Part One ---", part_one, sep='\n')
    print("--- Part Two ---", part_two, sep='\n')


if __name__ == "__main__":
    main()
