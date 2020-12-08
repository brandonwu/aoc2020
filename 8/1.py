#!/usr/bin/env python

def parse(line):
    ins, val_str = line.split()
    val = int(val_str)
    return (ins, val)


def main(arr):
    acc = 0
    pc = 0
    visited = set()

    while pc < len(arr):
        if pc in visited:
            return acc

        ins, val = arr[pc]
        visited.add(pc)

        if ins == 'acc':
            acc += val
            pc += 1
        elif ins == 'jmp':
            pc += val
        elif ins == 'nop':
            pc += 1

    return acc


def run(file):
    arr = f.readlines()
    print(main([parse(line.strip()) for line in arr]))


if __name__=='__main__':
    with open('testinput', 'r') as f:
        run(f)
    with open('input', 'r') as f:
        run(f)
