#!/usr/bin/env python

def main(arr):
  num_to_idx = set()
  for i, num in enumerate(arr):
    num = int(num)
    diff = 2020 - num
    if diff in num_to_idx:
      return diff * num
    else:
      num_to_idx.add(num)


if __name__=='__main__':
  with open('input', 'r') as f:
    arr = f.readlines()
    print(main(arr))
