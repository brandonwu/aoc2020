#!/usr/bin/env python

def parse(line):
    return int(line)


def main(arr, preamble):

    weak_n = None

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
            weak_n = n
            break

    # find the contiguous subarray of arr that sums to weak_n
    start, end = 0, 1

    cur_sum = arr[0] + arr[1]

    # i'm not convinced this works reliably in cases where the subarray
    # contains the preamble
    while cur_sum != weak_n:
        if cur_sum < weak_n:
            end += 1
            cur_sum += arr[end]
        else:
            cur_sum -= arr[start]
            start += 1

    sub = arr[start:end + 1:]

    return min(sub) + max(sub)


def run(file, preamble):
    arr = f.readlines()
    print(main([parse(line.strip()) for line in arr], preamble))


if __name__ == '__main__':
    with open('testinput', 'r') as f:
        run(f, 5)
    with open('input', 'r') as f:
        run(f, 25)
