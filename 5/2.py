#!/usr/bin/env python


def parse(line):
    n = line.replace('F', '0').replace('B', '1') \
        .replace('L', '0').replace('R', '1').strip()
    return int(n, 2)


def gauss(n):
    return n * (n + 1) / 2


def main(arr):
    total = 0
    cur_min = float('inf')
    cur_max = -1

    for line in f:
        n = parse(line)
        if n < cur_min:
            cur_min = n
        if n > cur_max:
            cur_max = n
        total += n

    return gauss(cur_max) - gauss(cur_min - 1) - total


if __name__ == '__main__':
    with open('input', 'r') as f:
        print(main(f))
