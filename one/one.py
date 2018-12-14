#!/usr/bin/python3

import sys

def main(argv):
  filename = argv[1]
  with open(filename) as numbers:
    nums = [int(line) for line in numbers]
    print(sum(nums))

if __name__ == '__main__':
  main(sys.argv)
