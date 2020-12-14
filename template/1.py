#!/usr/bin/env python


TESTS = [
    ('testinput', None),
    ('testinput2', None),
    ('input', None),
]


def parse(line):
    return line


def main(arr):
    pass


def run(file):
    arr = file.readlines()
    return main([parse(line.strip()) for line in arr])


def runFile(file, expected=None):
    with open(file, 'r') as f:
        print('\n%s\n%s' % (file, '=' * len(file)))
        result = run(f)

        if expected:
            if result != expected:
                msg = 'FAIL: expected %s got %s' % (expected, result)
            else:
                msg = 'SUCCESS'

            print(msg)
        else:
            print('GOT: %s' % result)


if __name__ == '__main__':
    for file, expect in TESTS:
        runFile(file, expect)
