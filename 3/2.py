#!/usr/bin/env python

from functools import reduce

def parse(line):
    return line


def main(arr):
    counter = lambda slope: count_trees(arr, slope[0], slope[1])

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    return reduce(lambda a, b: a * b, map(counter, slopes))


def count_trees(trees, x_inc, y_inc):
    tree_count = 0
    width = 0
    horiz_mult = 1

    first = True
    for i in range(0, len(trees), y_inc):
        row = trees[i]
        if first:
            first = False
            width = len(row)
        else:
            x = horiz_mult * x_inc

            if row[x % width] == '#':
                tree_count += 1

            horiz_mult += 1

    return tree_count


if __name__ == '__main__':
    with open('input', 'r') as f:
        arr = f.readlines()
        print(main([parse(line.strip()) for line in arr]))
