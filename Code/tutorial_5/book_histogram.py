from collections import Counter
import string

# Function to open the "Treasure Island" book, ignore punctuation, and to lowercase all words.

def histogram(filename):
  with open(filename, 'r', encoding='utf-8') as file:
    content = file.read().lower()
    translator = str.maketrans('', '', string.punctuation)
    filter_punctuation = content.translate(translator)
    words = filter_punctuation.split()
    word_count = Counter(words)
    return word_count

if __name__ == "__main__":
  word_count = histogram('treasure_island_book.txt')
  print(word_count)