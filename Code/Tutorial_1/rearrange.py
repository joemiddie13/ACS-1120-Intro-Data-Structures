import random
import sys

def rearrange(words):
  random.shuffle(words)
  return ' '.join(words)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    words = sys.argv[1:]
    print(rearrange(words))
  else:
    print("Please enter some words in the command line!")