#!/usr/bin/env python

def parse(line):
    return int(line)


def main(arr):
    s = sorted(arr)
    end = len(s)

    ways = 0
    q = [(0, 0)]

    # brute force, too slow!
    while q:
        last, i = q.pop()

        for i in range(i, i + 3):
            if i >= end:
                break

            test = s[i]
            if test - last <= 3:
                if i + 1 >= end:
                    ways += 1
                else:
                    q.append((test, i + 1))
            else:
                break

    return ways


def run(file):
    arr = f.readlines()
    print(main([parse(line.strip()) for line in arr]))


if __name__ == '__main__':
    with open('testinput', 'r') as f:
        run(f)
    with open('testinput2', 'r') as f:
        run(f)
    with open('input', 'r') as f:
        run(f)
