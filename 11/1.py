#!/usr/bin/env python

from collections import defaultdict


TESTS = [
    ('testinput', 37),
    ('testinput2', None),
    ('input', None),
]

FLOOR, EMPTY, OCCUP = 0, 1, 2


def parse(line):
    # use it as a bitmask
    # 00 == floor, 01 == empty chair, 10 == filled chair
    # we will store the mutations in the next left two bits
    # and mask them off when checking occupancy; this way
    # we don't need another array to store the modification
    # at the end of each rshift right 2
    return [1 if ch == 'L' else 0 for ch in line]


def main(arr):
    occupied = 0
    h, w = len(arr), len(arr[0]) if arr else 0

    read_rshift, write_lshift = 0, 2
    write_mask = 0b0011

    seats = []

    neighbors = defaultdict(list)

    for y in range(h):
        for x in range(w):
            val = arr[y][x]

            if val:
                seats.append((x, y))

                for adj_y in range(max(0, y - 1), min(y + 2, h)):
                    for adj_x in range(max(0, x - 1), min(x + 2, w)):
                        if x == adj_x and y == adj_y:
                            continue
                        adj = arr[adj_y][adj_x]
                        if arr:
                            neighbors[(x, y)].append((adj_x, adj_y))

    while True:
        seat_changed = False

        for seat in seats:
            x, y = seat
            cur = arr[y][x] >> read_rshift & 0b11

            adj_occu = 0

            for neighbor in neighbors[(x, y)]:
                adj_x, adj_y = neighbor

                if adj_occu >= 4:
                    break

                adj = arr[adj_y][adj_x] >> read_rshift & 0b11

                # occupied chair
                if adj == OCCUP:
                    adj_occu += 1
            # print('[%d]' % adj_occu, end='')

            arr[y][x] &= write_mask
            # occupy this seat if adj unoccupied
            if cur == EMPTY and adj_occu == 0:
                arr[y][x] |= (OCCUP << write_lshift)
                seat_changed = True
                occupied += 1
            # empty this seat if more than 4 occupied
            elif cur == OCCUP and adj_occu >= 4:
                arr[y][x] |= (EMPTY << write_lshift)
                seat_changed = True
                occupied -= 1
            # copy the seat over if no change
            else:
                arr[y][x] |= (cur << write_lshift)
            # print('>%d' % arr[y][x], end='')

            # print()

        # swap shifts and mask
        read_rshift, write_lshift = write_lshift, read_rshift
        write_mask ^= 0b1111

        if not seat_changed:
            return occupied


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
