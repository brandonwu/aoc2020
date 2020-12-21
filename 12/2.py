#!/usr/bin/env python


TESTS = [
    ('testinput', 286),
    ('testinput2', None),
    ('input', None),
]


DIRS = ['N', 'E', 'S', 'W']


def parse(line):
    return (line[0], int(line[1:]))


def rotate(way_x, way_y, val):
    # do the change of basis rotation thing
    pass


def main(arr):
    pos_x, pos_y = 0, 0
    way_x, way_y = -10, 1

    for ins, val in arr:
        if ins == 'F':
            pos_x += way_x
            pos_y += way_y
        elif ins == 'N':
            way_y += val
        elif ins == 'S':
            way_y -= val
        elif ins == 'E':
            way_x -= val
        elif ins == 'W':
            way_x += val
        elif ins == 'L' or 'R':
            way_x, way_y = rotate(way_x, way_y, val)

    return abs(pos_x) + abs(pos_y)


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
