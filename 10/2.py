#!/usr/bin/env python


TESTS = [
    ('testinput', 8),
    ('testinput2', 19208),
    ('input', None),
]


def parse(line):
    return int(line)


def dfs(node, graph, memo):
    val, pos = node
    # base case
    if pos == (len(graph) - 1):
        return 1
    # recurse
    elif pos in memo:
        return memo[pos]
    else:
        acc = 0
        for i in range(pos + 1, min(pos + 4, len(graph))):
            testval = graph[i]

            if testval - val <= 3:
                ways = dfs((testval, i), graph, memo)
                acc += ways

                if i not in memo:
                    memo[i] = ways

        return acc


def dfs_help(graph):
    return dfs((0, 0), graph, {})


def main(arr):
    s = [0]
    s.extend(sorted(arr))
    s.append(s[-1] + 3)

    return dfs_help(s)


def run(file):
    arr = file.readlines()
    return main([parse(line.strip()) for line in arr])


def runFile(file, expected=None):
    with open(file, 'r') as f:
        print('\n%s\n%s' % (file, '=' * len(file)))
        result = run(f)

        if expected:
            if result != expected:
                msg = 'FAIL: expected %s got %s' % (expected, result)
            else:
                msg = 'SUCCESS'

            print(msg)
        else:
            print('GOT: %s' % result)


if __name__ == '__main__':
    for file, expect in TESTS:
        runFile(file, expect)
