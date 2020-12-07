#!/usr/bin/env python

from collections import defaultdict

def parse(line):
    return line


def main(arr):
    count = 0

    people = 0
    #question letter -> count of people in this group answered
    questions = defaultdict(int)
    for row in arr:
        if not row:
            count += sum(1 for _ in filter(lambda tup: tup[1] == people, questions.items()))
            questions = defaultdict(int)
            people = 0
        else:
            people += 1
            for letter in row:
                questions[letter] += 1

    if questions:
        count += sum(1 for _ in filter(lambda tup: tup[1] == people, questions.items()))

    return count


if __name__=='__main__':
    with open('input', 'r') as f:
        arr = f.readlines()
        print(main([parse(line.strip()) for line in arr]))
