import random

# Function to build a Markov chain from a given corpus
def build_markov_chain(corpus):
  # Initialize an empty dictionary to hold the Markov chain
  markov_chain = {}
  # Split the corpus into individual words
  corpus_words = corpus.split()
  # Iterate through each word in the corpus, except the last word
  for i in range(len(corpus_words) - 1):
    curr_word = corpus_words[i]  # Current word
    next_word = corpus_words[i + 1]  # Next word
    # If the current word is not already a key in the Markov chain, add it
    if curr_word not in markov_chain:
      markov_chain[curr_word] = {}
    # If the next word is not already associated with the current word, add it
    if next_word not in markov_chain[curr_word]:
      markov_chain[curr_word][next_word] = 1
    else:
      # Increment the count for the next word
      markov_chain[curr_word][next_word] += 1

  # Convert counts to probabilities for each next-word in the chain
  for curr_word, next_words in markov_chain.items():
    total_counts = sum(next_words.values())
    markov_chain[curr_word] = {word: count / total_counts for word, count in next_words.items()}

  return markov_chain

# Function to get starting words for sentence generation based on their frequency
def get_starting_words(corpus, threshold=0.005):
  sentences = corpus.split('.')  # Split the corpus into sentences
  starting_words = {}  # Initialize an empty dictionary for starting words
  # Iterate through each sentence
  for sentence in sentences:
    words = sentence.strip().split()  # Split the sentence into words
    if words:
      first_word = words[0]  # Get the first word of the sentence
      # Increment the count for the first word
      starting_words[first_word] = starting_words.get(first_word, 0) + 1

  total_starts = sum(starting_words.values())  # Get the total number of sentence starts
  # Filter out starting words that are below the threshold frequency
  starting_words = {word: count / total_starts for word, count in starting_words.items() if count / total_starts > threshold}

  return starting_words

# Function to generate a sentence from a Markov chain
def generate_sentence(markov_chain, length=21):
  start_word = random.choice(list(markov_chain.keys()))  # Randomly choose a starting word
  current_word = start_word
  sentence = [current_word]  # Initialize the sentence with the starting word

  # Generate the rest of the sentence
  for _ in range(length - 1):
    next_words = markov_chain.get(current_word, None)  # Get the next possible words
    if not next_words:
      break
    # Randomly choose the next word based on the current word's probabilities
    next_word = random.choices(list(next_words.keys()), weights=next_words.values())[0]
    sentence.append(next_word)  # Add the next word to the sentence
    current_word = next_word  # Update the current word

  return ' '.join(sentence)  # Return the sentence as a string
