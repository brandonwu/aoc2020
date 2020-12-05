#!/usr/bin/env python

import re

def parse(line):
    return line


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

    valid_count = 0
    for passport in passports:
        check = [field in passport for field in req_fields]
        if all(check):
            valid_count += 1
        else:
            print(passport, [x for x in filter(lambda f: not f[1], zip(req_fields, check))])

    return valid_count

if __name__=='__main__':
    with open('input', 'r') as f:
        arr = f.readlines()
        print(main([parse(line.strip()) for line in arr]))
