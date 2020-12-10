#!/usr/bin/env python

def parse(line):
    return int(line)


def main(arr):
    s = sorted(arr)
    s.append(s[-1] + 3)

    diffs = [0, 0, 0, 0]
    for i in range(len(s) - 1):
        diff = s[i + 1] - s[i]
        diffs[diff] += 1
    diffs[s[0]] += 1

    return diffs[1] * diffs[3]


def run(file):
    arr = f.readlines()
    print(main([parse(line.strip()) for line in arr]))


if __name__ == '__main__':
    with open('testinput', 'r') as f:
        run(f)
    with open('input', 'r') as f:
        run(f)
