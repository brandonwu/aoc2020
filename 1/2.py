#!/usr/bin/env python

def main(arr):
  diffs = [ 2020 - int(n) for n in arr ]
  for diff in diffs:
    seen = set()
    for n in arr:
      n = int(n)
      diff2 = diff - n
      if diff2 in seen:
        return diff2 * n * (2020 - diff)
      else:
        seen.add(n)

if __name__=='__main__':
  with open('input', 'r') as f:
    arr = f.readlines()
    print(main(arr))
