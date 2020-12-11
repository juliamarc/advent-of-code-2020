import copy

from itertools import starmap, chain, repeat


def get_adj_count(layout, idx, dirs):
    cnt_layout = copy.deepcopy(layout)

    def count_at_position(i, j):
        cnt_layout[i][j] = sum(
            starmap(lambda x, y: layout[i+x][j+y] == '#', dirs.values()))

    list(starmap(count_at_position, idx))

    return cnt_layout


def get_visible_count(layout, idx, dirs):
    cnt_layout = copy.deepcopy(layout)

    def is_occupied_visible(layout, i, j, direction):
        i += dirs[direction][0]
        j += dirs[direction][1]
        if layout[i][j] == '_' or layout[i][j] == 'L':
            return False
        elif layout[i][j] == '#':
            return True
        else:
            return is_occupied_visible(layout, i, j, direction)

    def count_at_position(i, j):
        cnt_layout[i][j] = sum(
            map(lambda d: is_occupied_visible(layout, i, j, d), dirs.keys()))

    list(starmap(count_at_position, idx))

    return cnt_layout


def stabilize_chaos(layout, idx, directions, count_func, empty_rule):
    current_layout = copy.deepcopy(layout)

    while True:
        adj_cnt = count_func(current_layout, idx, directions)
        new_layout = copy.deepcopy(current_layout)
        for i, j in idx:
            if current_layout[i][j] == 'L' and not adj_cnt[i][j]:
                new_layout[i][j] = '#'
            elif current_layout[i][j] == '#' and adj_cnt[i][j] > empty_rule:
                new_layout[i][j] = 'L'
        if new_layout == current_layout:
            break
        else:
            current_layout = new_layout

    return current_layout


def sum_taken_seats(layout):
    return sum(map(lambda x: sum(map(lambda y: y == '#', x)), layout))


def main():
    directions = {
        'left': (0, -1),
        'right': (0, 1),
        'top': (1, 0),
        'down': (-1, 0),
        'top_left': (1, -1),
        'top_right': (1, 1),
        'bottom_left': (-1, -1),
        'bottom_right': (-1, 1),
    }

    with open('input') as f:
        lines = f.read().splitlines()

    layout = list(map(list, lines))
    padding = [['_'] * (len(layout[0]) + 2)]
    def pad_row(r): return ['_'] + r + ['_']
    padded_layout = padding + list(map(pad_row, layout)) + padding

    row_range = range(1, len(padded_layout[0]) - 1)
    col_range = range(1, len(padded_layout) - 1)
    idx = map(lambda y: list(zip(repeat(y), row_range)), col_range)
    idx = list(filter(lambda idx: padded_layout[idx[0]][idx[1]] != '.', chain(*idx)))

    part_one_layout = stabilize_chaos(
        padded_layout, idx, directions, get_adj_count, 3)
    part_one = sum_taken_seats(part_one_layout)

    part_two_layout = stabilize_chaos(
        padded_layout, idx, directions, get_visible_count, 4)
    part_two = sum_taken_seats(part_two_layout)

    print("--- Part One ---", part_one, sep='\n')
    print("--- Part Two ---", part_two, sep='\n')


if __name__ == "__main__":
    main()
