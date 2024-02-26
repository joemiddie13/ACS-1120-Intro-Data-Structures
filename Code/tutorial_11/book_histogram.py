from collections import Counter
import string

def histogram(filename):
    """
    Generates a histogram (frequency distribution) of words from a text file.

    Args:
    - filename: The path to the text file.

    Returns:
    - A Counter object containing the word frequencies.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().lower()
        translator = str.maketrans('', '', string.punctuation)
        filtered_content = content.translate(translator)
        words = filtered_content.split()
        word_count = Counter(words)
        return word_count

def unique_words(histogram):
    """
    Calculates the number of unique words in a histogram.

    Args:
    - histogram: The histogram containing word frequencies.

    Returns:
    - An integer representing the number of unique words.
    """
    return len(histogram)

def frequency(word, histogram):
    """
    Retrieves the frequency of a specific word from a histogram.

    Args:
    - word: The word to retrieve the frequency for.
    - histogram: The histogram containing word frequencies.

    Returns:
    - The frequency count of the word.
    """
    return histogram[word]
