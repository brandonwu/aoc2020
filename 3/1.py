#!/usr/bin/env python

def parse(line):
    return line


def main(arr):
    tree_count = 0
    width = 0
    horiz_mult = 1

    first = True
    for row in arr:
        if first:
            first = False
            width = len(row)
        else:
            x = horiz_mult * 3

            if row[x % width] == '#':
                tree_count += 1

            horiz_mult += 1

    return tree_count


if __name__ == '__main__':
    with open('input', 'r') as f:
        arr = f.readlines()
        print(main([parse(line.strip()) for line in arr]))
