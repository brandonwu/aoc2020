#!/usr/bin/env python

import re

def parse(line):
    return line


def valid(p):
    byr = int(p['byr'])
    iyr = int(p['iyr'])
    eyr = int(p['eyr'])
    hgt = p['hgt']
    hcl = p['hcl']
    ecl = p['ecl']
    pid = p['pid']

    if byr < 1920 or byr > 2002:
        return False
    elif iyr < 2010 or iyr > 2020:
        return False
    elif eyr < 2020 or eyr > 2030:
        return False

    h = re.fullmatch(r'(?P<height>\d+)(?P<unit>(?:in)|(?:cm))', hgt)
    if not h:
        return False
    height = int(h.group('height'))
    unit = h.group('unit')
    units = ['cm', 'in']

    if unit not in units:
        return False

    if unit == 'cm' and (height < 150 or height > 193):
        return False
    elif unit == 'in' and (height < 59 or height > 76):
        return False

    hc = re.fullmatch(r'#[0-9a-f]{6}', hcl)
    if not hc:
        return False

    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    p = re.fullmatch(r'\d{9}', pid)
    if not p:
        return False

    return True


def main(arr):
    req_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        #'cid'
    ]

    field_pattern = r'(?P<field>\w+):(?P<value>[\w#]+)'
    field_re = re.compile(field_pattern)

    passports = []
    cur_passport = {}
    for row in arr:
        # blank line means passport complete
        if not row:
            passports.append(cur_passport)
            cur_passport = {}
            continue

        matches = field_re.findall(row)
        for field, val in matches:
            cur_passport[field] = val

    # blank line at end gets stripped
    if cur_passport:
        passports.append(cur_passport)

    valid_count = 0
    for passport in passports:
        check = [field in passport for field in req_fields]
        if all(check) and valid(passport):
            valid_count += 1

    return valid_count

if __name__=='__main__':
    with open('input', 'r') as f:
        arr = f.readlines()
        print(main([parse(line.strip()) for line in arr]))
