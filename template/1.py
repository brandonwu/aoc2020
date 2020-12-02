#!/usr/bin/env python

def parse(line):
  pass


def main(arr):
  pass


if __name__=='__main__':
  with open('input', 'r') as f:
    arr = f.readlines()
    print(main([parse(line.strip()) for line in arr]))
