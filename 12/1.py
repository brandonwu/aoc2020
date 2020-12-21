#!/usr/bin/env python


TESTS = [
    ('testinput', 25),
    ('testinput2', None),
    ('input', None),
]


DIRS = ['N', 'E', 'S', 'W']


def parse(line):
    return (line[0], int(line[1:]))


def rotate(current_dir, turn, amount):
    cur_i = 0
    for i, dire in enumerate(DIRS):
        if dire == current_dir:
            cur_i = i
            break
    sign = 1 if turn == 'R' else -1
    return DIRS[(cur_i + sign * amount // 90) % 4]


def main(arr):
    pos_x, pos_y = 0, 0
    face = 'E'

    for ins, val in arr:
        if ins == 'F':
            ins = face

        if ins == 'N':
            pos_y += val
        elif ins == 'S':
            pos_y -= val
        elif ins == 'E':
            pos_x -= val
        elif ins == 'W':
            pos_x += val
        elif ins == 'L' or 'R':
            face = rotate(face, ins, val)

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
