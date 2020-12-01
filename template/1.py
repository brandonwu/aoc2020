#!/usr/bin/env python

def main(arr):
  pass


if __name__=='__main__':
  with open('input', 'r') as f:
    arr = f.readLines()
    print(main([int(n) for n in arr]))
