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

# word_count = histogram('treasure_island_book.txt')
# print(word_count)
  
# Function that takes a histogram argument and returns the total number of unique words

def unique_words(histogram):
  return len(histogram)

# word_count = histogram('treasure_island_book.txt')
# unique_word_count = unique_words(word_count)
# print(unique_word_count)

# Function that takes a word and histogram argument, and returns the number of times that word appears in the text.

def frequency(word, histogram):
  return histogram[word]

word_count = histogram('treasure_island_book.txt')

user_input = input('Want to know how often a word appears in the book, "Treasure Island"? Please type in a word: ')
word_frequency = frequency(user_input, word_count)
print(f"The word '{user_input}' appears {word_frequency} times in the book, Treasure Island'.")