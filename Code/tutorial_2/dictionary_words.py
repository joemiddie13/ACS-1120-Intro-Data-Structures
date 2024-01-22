import random
import sys

def read_words(file_path):
  with open(file_path, 'r') as file:
    return file.read().splitlines()

def generate_sentence(words_list, count):
  return ' '.join(random.sample(words_list, count)) + '.'

if __name__ == '__main__':
  if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    print("Usage: python3 dictionary_words.py [number_of_words]")
  else:
    number_of_words = int(sys.argv[1])
    words_file_path = '/usr/share/dict/words'
    words = read_words(words_file_path)
    print(generate_sentence(words, number_of_words))

'''
Pseudo code for dictionary_words.py

1. Start

2. Define a function to read words from a file
   a. Open the file at the given path
   b. Read all lines from the file into a list
   c. Return the list of words

3. Define a function to generate a random sentence
   a. Take two arguments: a list of words and the number of words in the sentence
   b. Randomly select the specified number of words from the list
   c. Join these words into a single string with spaces
   d. Return the string

4. In the main part of the script
   a. Check if the correct number of command-line arguments is provided
   b. If not, display usage information and exit
   c. Convert the number of words argument from a string to an integer
   d. Set the path to the words file (usually /usr/share/dict/words)
   e. Call the function to read words from the file
   f. Call the function to generate a random sentence with the read words
   g. Print the generated sentence

5. End
'''