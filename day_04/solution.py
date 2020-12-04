import re

from itertools import compress


def main():
    def val_byr(b): return len(b) == 4 and int(b) >= 1920 and int(b) <= 2002
    def val_iyr(i): return len(i) == 4 and int(i) >= 2010 and int(i) <= 2020
    def val_eyr(e): return len(e) == 4 and int(e) >= 2020 and int(e) <= 2030

    def val_hgt(h):
        m = re.match(r'([0-9]+)(cm|in)', h)
        if not m:
            return False

        num, unit = int(m.group(1)), m.group(2)
        cm_valid = unit == 'cm' and 150 <= num <= 193
        in_valid = unit == 'in' and 59 <= num <= 76
        if cm_valid or in_valid:
            return True
        else:
            return False

    def val_hcl(h): return bool(re.match(r'^#[0-9a-f]{6}$', h))
    def val_ecl(e): return e in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    def val_pid(p): return bool(re.match(r'^[0-9]{9}$', p))
    def val_cid(c): return True

    with open('input') as f:
        lines = f.read().split('\n\n')

    fields = {'byr': val_byr, 'iyr': val_iyr, 'eyr': val_eyr, 'hgt': val_hgt,
              'hcl': val_hcl, 'ecl': val_ecl, 'pid': val_pid, 'cid': val_cid}
    req_fields = list(fields.keys())[:-1]

    regexp = r'([\S]{3}):(\S+)[\n\s]*?'
    passports = list(map(lambda l: re.findall(regexp, l), lines))

    keys_only = list(map(lambda p: list(map(lambda f: f[0], p)), passports))
    def fields_present(k): return set(req_fields).issubset(set(k))
    are_fields_present = list(map(lambda k: fields_present(k), keys_only))

    passports_fields_present = compress(passports, are_fields_present)
    def fields_valid(f): return all(map(lambda kv: fields[kv[0]](kv[1]), f))
    are_fields_valid = map(lambda p: fields_valid(p), passports_fields_present)

    print("--- Part One ---", sum(are_fields_present), sep='\n')
    print("--- Part Two ---", sum(are_fields_valid), sep='\n')


if __name__ == "__main__":
    main()
