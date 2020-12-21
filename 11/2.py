#!/usr/bin/env python


TESTS = [
    ('testinput', 26),
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

    # (x, y) -> [[neighbors]]
    neighbors = {}

    # find chairs
    for y in range(h):
        for x in range(w):
            cur = arr[y][x] >> read_rshift & 0b11
            # print('%d' % cur, end='')
            # floor
            if not cur:
                # print('[*]', end='')
                continue

            neighbors[(x, y)] = []
            # neighbors[(x, y)] = [[None] * 3, [None] * 3, [None] * 3]

    # find chair neighbors
    for ctr, nbr in neighbors.items():
        ctr_x, ctr_y = ctr

        # left
        for x in range(ctr_x, -1, -1):
            if x == ctr_x:
                continue
            cur = arr[ctr_y][x] >> read_rshift & 0b11
            if cur:
                # nbr[1][0] = (x, ctr_y)
                nbr.append((x, ctr_y))
                break

        # right
        for x in range(ctr_x, w):
            if x == ctr_x:
                continue
            cur = arr[ctr_y][x] >> read_rshift & 0b11
            if cur:
                #nbr[1][2] = (x, ctr_y)
                nbr.append((x, ctr_y))
                break

        # top
        for y in range(ctr_y, -1, -1):
            if y == ctr_y:
                continue
            cur = arr[y][ctr_x] >> read_rshift & 0b11
            if cur:
                # nbr[0][1] = (ctr_x, y)
                nbr.append((ctr_x, y))
                break

        # bot
        for y in range(ctr_y, h):
            if y == ctr_y:
                continue
            cur = arr[y][ctr_x] >> read_rshift & 0b11
            if cur:
                # nbr[2][1] = (ctr_x, y)
                nbr.append((ctr_x, y))
                break

        # topleft
        for i in range(min(ctr_x + 1, ctr_y + 1)):
            x, y = ctr_x - i, ctr_y - i
            if x == ctr_x and y == ctr_y:
                continue

            cur = arr[y][x] >> read_rshift & 0b11
            if cur:
                # nbr[0][0] = (x, y)
                nbr.append((x, y))
                break

        # topright
        for i in range(min(w - ctr_x, ctr_y + 1)):
            x, y = ctr_x + i, ctr_y - i
            if x == ctr_x and y == ctr_y:
                continue

            cur = arr[y][x] >> read_rshift & 0b11
            if cur:
                #nbr[0][2] = (x, y)
                nbr.append((x, y))
                break

        # botleft
        for i in range(min(ctr_x + 1, h - ctr_y)):
            x, y = ctr_x - i, ctr_y + i
            if x == ctr_x and y == ctr_y:
                continue

            cur = arr[y][x] >> read_rshift & 0b11
            if cur:
                # nbr[2][0] = (x, y)
                nbr.append((x, y))
                break

        # botright
        for i in range(min(w - ctr_x, h - ctr_y)):
            x, y = ctr_x + i, ctr_y + i
            if x == ctr_x and y == ctr_y:
                continue

            cur = arr[y][x] >> read_rshift & 0b11
            if cur:
                # nbr[2][2] = (x, y)
                nbr.append((x, y))
                break

    # print(neighbors)
    rd = 0
    while True:
        seat_changed = False

        # print('\nRound %d\n========' % rd)
        # rd += 1
        # for row in arr:
        #     for el in row:
        #         cur = el >> read_rshift & 0b11
        #         cur = '.' if not cur else 'L' if cur == 1 else '#'
        #         print(cur, end='')
        #     print()

        for ctr, nbrs in neighbors.items():
            ctr_x, ctr_y = ctr
            cur = arr[ctr_y][ctr_x] >> read_rshift & 0b11

            adj_occu = 0
            for nbr in nbrs:
                nbr_x, nbr_y = nbr
                adj = arr[nbr_y][nbr_x] >> read_rshift & 0b11

                if adj == OCCUP:
                    adj_occu += 1

            arr[ctr_y][ctr_x] &= write_mask
            if cur == EMPTY and adj_occu == 0:
                    arr[ctr_y][ctr_x] |= (OCCUP << write_lshift)
                    seat_changed = True
                    occupied += 1
            # empty this seat if more than 4 occupied
            elif cur == OCCUP and adj_occu >= 5:
                arr[ctr_y][ctr_x] |= (EMPTY << write_lshift)
                seat_changed = True
                occupied -= 1
            # copy the seat over if no change
            else:
                arr[ctr_y][ctr_x] |= (cur << write_lshift)

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
