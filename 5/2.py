#!/usr/bin/env python

def parse(line):
    return line.replace('F', '0').replace('B', '1') \
        .replace('L', '0').replace('R', '1')


def main(arr):
    nums = [int(n, 2) for n in arr]
    r = set(range(min(nums), max(nums) + 1))

    for n in nums:
        r.remove(n)

    for n in r:
        return n


if __name__ == '__main__':
    with open('input', 'r') as f:
        arr = f.readlines()
        print(main([parse(line.strip()) for line in arr]))
