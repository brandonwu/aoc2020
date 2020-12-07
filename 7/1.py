#!/usr/bin/env python

import regex
from collections import defaultdict

def parse(line):
    parse_re = regex.compile(r'(?P<outside>[a-z ]+) bags contain (?: ?(?P<count>(?:\d+)|(?:no)) ?(?P<inside>[a-z ]+) bags?[,\.]?)+')
    return parse_re.fullmatch(line)


# builds the mappings of outside -> insides and inside -> outsides
def mappings(matches):
    # mapping of out -> in
    tree = defaultdict(lambda: defaultdict(dict))
    # structure: dict of outside color -> dict of inside color -> int of count  
    for match in matches:
        outside = match.group('outside')
        insides = match.captures('inside')
        counts = match.captures('count')
        if counts[0] == 'no':
            tree[outside] = {}
        else:
            for inside, count in zip(insides, counts):
                tree[outside][inside] = count

    # turn it to in -> out so we can answer the question =)
    reverse_tree = defaultdict(set)
    for outside, inside_map in tree.items():
        for inside, _ in inside_map.items():
            reverse_tree[inside].add(outside)

    return tree, reverse_tree


def main(matches):
    out2in, in2out = mappings(matches)

    q = list(in2out['shiny gold'])
    visited = {'shiny gold'}

    while q:
        cur = q.pop()
        visited.add(cur)

        for out in in2out[cur]:
            if out not in visited:
                q.append(out)

    return len(visited) - 1 # exclude the original


if __name__=='__main__':
    with open('input', 'r') as f:
        arr = f.readlines()
        print(main([parse(line.strip()) for line in arr]))