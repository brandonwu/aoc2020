#!/usr/bin/env python

def parse(line):
    return line


def main(arr):
    count = 0
    questions = set()
    for row in arr:
        if not row:
            count += len(questions)
            questions = set()
        else:
            for letter in row:
                questions.add(letter)

    if questions:
        count += len(questions)

    return count


if __name__=='__main__':
    with open('input', 'r') as f:
        arr = f.readlines()
        print(main([parse(line.strip()) for line in arr]))
