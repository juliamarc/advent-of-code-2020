def decode(s):
    binary = s.translate(str.maketrans('FBLR', '0101'))
    return int(binary[:7], 2), int(binary[7:], 2)


def main():
    with open('input') as f:
        lines = f.read().splitlines()

    ids = list(map(lambda s: s[0] * 8 + s[1], map(lambda s: decode(s), lines)))
    my_id = sorted(set(range(min(ids), max(ids) + 1)).difference(ids))[0]

    print("--- Part One ---", max(ids), sep='\n')
    print("--- Part Two ---", my_id, sep='\n')


if __name__ == "__main__":
    main()
