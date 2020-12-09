#!/usr/bin/env python

def parse(line):
    return line


def main(arr):
    pass


def run(file):
    arr = f.readlines()
    print(main([parse(line.strip()) for line in arr]))


if __name__ == '__main__':
    with open('testinput', 'r') as f:
        run(f)
    with open('input', 'r') as f:
        run(f)
