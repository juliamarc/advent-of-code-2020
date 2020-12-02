import re


def main():
    with open('input') as f:
        lines = f.read().splitlines()

    regexp = r'([0-9]+)-([0-9]+)\s([a-z]):\s([a-z]+)$'
    def match(l): return re.match(regexp, l)
    def explode(m): return (int(m.group(1)), int(m.group(2)), m.group(3), m.group(4))
    passwds = list(map(explode, map(match, lines)))

    def policy_1(p): return p[3].count(p[2]) in range(p[0], p[1] + 1)
    def policy_2(p): return (p[2] == p[3][p[0] - 1]) ^ (p[2] == p[3][p[1] - 1])

    print("--- Part One ---", sum(map(policy_1, passwds)), sep='\n')
    print("--- Part Two ---", sum(map(policy_2, passwds)), sep='\n')


if __name__ == "__main__":
    main()
