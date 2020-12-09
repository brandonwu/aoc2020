#!/usr/bin/env python

def parse(line):
    return int(line)


def main(arr, preamble):

    for i, n in enumerate(arr[preamble::]):
        diffs = set()

        valid = False
        for test in arr[i:i + preamble:]:
            if n - test in diffs:
                valid = True
                break
            else:
                diffs.add(test)

        if not valid:
            return n


def run(file, preamble):
    arr = f.readlines()
    print(main([parse(line.strip()) for line in arr], preamble))


if __name__ == '__main__':
    with open('testinput', 'r') as f:
        run(f, 5)
    with open('input', 'r') as f:
        run(f, 25)
