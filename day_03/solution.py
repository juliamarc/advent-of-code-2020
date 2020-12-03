from itertools import count
from functools import reduce


def trees_on_slope(tree_map, slope):
    height, width = len(tree_map), len(tree_map[0])
    x_coord_cnt, y_coords = count(0, slope[0]), range(0, height, slope[1])
    xy_coords = map(lambda y: (next(x_coord_cnt) % width, y), y_coords)

    return sum(map(lambda xy: tree_map[xy[1]][xy[0]] == '#', xy_coords))


def main():
    with open('input') as f:
        lines = f.read().splitlines()

    tree_map = lines
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    part_one = trees_on_slope(tree_map, slopes[1])
    part_two = map(lambda s: trees_on_slope(tree_map, s), slopes)
    part_two = reduce(lambda x, y: x*y, part_two)

    print("--- Part One ---", part_one, sep='\n')
    print("--- Part Two ---", part_two, sep='\n')


if __name__ == "__main__":
    main()
