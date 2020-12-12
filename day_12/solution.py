from itertools import starmap


def main():
    directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    faces, change_facing = ('N', 'E', 'S', 'W'), ('L', 'R')

    with open('input') as f:
        lines = f.read().strip().splitlines()

    instr = list(map(lambda l: (l[0], int(l[1:])), lines))

    x, y, facing = 0, 0, 1

    def navigate_part_one(action, value):
        nonlocal x, y, facing
        if action in faces:
            x += directions[action][0] * value
            y += directions[action][1] * value
        elif action in change_facing:
            value = (value % 360) // 90
            if action == 'L':
                facing = (facing + 4 - value) % 4
            elif action == 'R':
                facing = (facing + value) % 4
        elif action == 'F':
            x += directions[faces[facing]][0] * value
            y += directions[faces[facing]][1] * value

    list(starmap(navigate_part_one, instr))
    part_one = abs(x) + abs(y)

    rotations = ((1, 1), (1, -1), (-1, -1), (-1, 1))
    quadrants = [[0, 1], [3, 2]]
    x, y, w_x, w_y, quadrant = 0, 0, 10, 1, 0

    def navigate_part_two(action, value):
        nonlocal x, y, w_x, w_y, quadrant
        if action in faces:
            w_x += directions[action][0] * value
            w_y += directions[action][1] * value
        elif action in change_facing:
            quadrant = quadrants[w_x < 0][w_y < 0]
            value = (value % 360) // 90
            if action == 'L':
                quadrant = (quadrant + 4 - value) % 4
            elif action == 'R':
                quadrant = (quadrant + value) % 4
            if value % 2:
                w_x, w_y = w_y, w_x
            w_x = abs(w_x) * rotations[quadrant][0]
            w_y = abs(w_y) * rotations[quadrant][1]
        elif action == 'F':
            x += w_x * value
            y += w_y * value

    list(starmap(navigate_part_two, instr))
    part_two = abs(x) + abs(y)

    print("--- Part One ---", part_one, sep='\n')
    print("--- Part Two ---", part_two, sep='\n')


if __name__ == "__main__":
    main()
