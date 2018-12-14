#!/usr/bin/python3

import sys

# Returns True if word contains exactly N occurences of any character, 
# otherwise returns False
def exactlyN(word, n):
  letterCounts = dict()
  for letter in word:
    if letter in letterCounts:
      letterCounts[letter] += 1
    else:
      letterCounts[letter] = 1
  return n in letterCounts.values()

# Central function: takes in a list of strings, and a * b where a is the 
# number of strings with exactly 2 of any letter, and b is the number with
# exactly three
def countTwosThrees(words):
  twos = 0
  threes = 0
  for word in words:
    if(exactlyN(word, 2)):
      twos += 1
    if(exactlyN(word, 3)):
      threes += 1
  return twos*threes

def main(argv):
  filename = argv[1]
  with open(filename) as words:
    print(countTwosThrees(words))

if __name__ == '__main__':
  main(sys.argv)
