from collections import Counter
import sys
import book_histogram
import random

# In the terminal, pass in the Treasure Island Book
# Example: python3 sample.py treasure_island_book.txt

'''
Perform weighted random sampling from the Treasure Island histogram,
where the probability of each item being selected is proportional to its frequency.
'''
def weighted_sample(histogram):
  words, frequencies = zip(*histogram.items())
  return random.choices(words, weights=frequencies, k=1)[0]

def generate_sentence(histogram, word_count=13):
   return ' '.join(weighted_sample(histogram) for _ in range(word_count))
  
if __name__ == "__main__":
  histogram = book_histogram.histogram('treasure_island_book.txt')

  # Generate a random sentence from Treasure Island with 13 words
  sentence = generate_sentence(histogram, word_count=13)
  print(sentence)
  
  # Test the weighted sampling function
  samples = [weighted_sample(histogram) for _ in range(10000)]
  sample_counts = Counter(samples)

  # Print the word frequencies and their experimental probabilities
  for word, count in sample_counts.items():
      percentage = (count / 10000) * 100 
      print(f"'{word}': {count / 10000:.2f}%")
