#!/usr/bin/python3

import sys

def main(argv):
  filename = argv[1]
  frequencyset = set()
  frequencyset.add(0)
  with open(filename) as numbers:
    numberlist = [int(line) for line in numbers]
    frequency = 0
    indx = 0
    # Only manually break the loop once we find a duplicate
    # Assumes that all input WILL eventually produce an answer
    while(True):
      frequency += numberlist[indx]
      if(frequency in frequencyset):
        break
      else:
        frequencyset.add(frequency)
        indx = (indx + 1) % len(numberlist)
    # frequency is now the first duplicate frequency
    print(frequency)

if __name__ == '__main__':
  main(sys.argv)
