#!/usr/bin/env python

def parse(line):
    return line.replace('F', '0').replace('B', '1') \
        .replace('L', '0').replace('R', '1')


def main(arr):
    return max([int(n, 2) for n in arr])


if __name__ == '__main__':
    with open('input', 'r') as f:
        arr = f.readlines()
        print(main([parse(line.strip()) for line in arr]))
