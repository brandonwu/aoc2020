#!/usr/bin/env python

def parse(line):
  a = line.split(': ')
  pwd = a[1]
  rule = a[0].split()
  range = rule[0].split('-')
  char = rule[1]
  return (int(range[0]) - 1, int(range[1]) - 1, char, pwd)


def main(arr):
  valid_count = 0

  for entry in arr:
    first, second, char, pwd = entry
    valid_count += (pwd[first] == char) ^ (pwd[second] == char)

  return valid_count


if __name__=='__main__':
  with open('input', 'r') as f:
    arr = f.readlines()
    print(main([parse(line.strip()) for line in arr]))
