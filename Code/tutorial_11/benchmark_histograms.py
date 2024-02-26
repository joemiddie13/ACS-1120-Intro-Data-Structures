"""
Benchmarking Script for Dictogram and Listogram Performance Analysis

Analysis:
- Dictogram shows superior performance in both initialization and frequency retrieval compared to Listogram.
- The optimized hashing mechanism of Python's dictionaries, which Dictogram extends, provides faster insertion and lookup.
- Listogram's list-based structure requires iteration for frequency retrieval, leading to slower performance.

This script benchmarks the initialization time and frequency retrieval time for both Dictogram and Listogram implementations using a sample text file.

"""

import timeit
from dictogram import Dictogram
from listogram import Listogram

def read_words_from_file(file_path):
    """Read words from a file and return them as a list."""
    with open(file_path, 'r') as f:
        words = f.read().split()
    return words

def generate_word_list(words, size):
    """Generate a list of words of a specified size from the given list."""
    return words[:size]

def benchmark_histogram_init(histogram_class, word_list_name):
    """Benchmark the initialization time of a histogram class with a given word list."""
    setup_code = f'''
from __main__ import {histogram_class.__name__}, {word_list_name}
'''
    test_code = f'{histogram_class.__name__}({word_list_name})'
    # Measure the time taken to initialize the histogram multiple times and calculate the average
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=3, number=10, globals=globals())
    print(f'Average Initialization time for {histogram_class.__name__}: {sum(times) / len(times)} seconds')

def benchmark_frequency_method(histogram_class, word_list_name, word):
    """Benchmark the frequency retrieval time of a histogram class for a given word."""
    setup_code = f'''
from __main__ import {histogram_class.__name__}, {word_list_name}
histogram = {histogram_class.__name__}({word_list_name})
word = '{word}'
'''
    test_code = 'histogram.frequency(word)'
    # Measure the time taken to retrieve the frequency of a word multiple times and calculate the average
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=3, number=1000, globals=globals())
    print(f'Average frequency retrieval time for {histogram_class.__name__} with "{word}": {sum(times) / len(times)} seconds')

if __name__ == '__main__':
    file_path = 'treasure_island_book.txt'
    all_words = read_words_from_file(file_path)

    # Generate word lists of different sizes for benchmarking
    word_list_small = generate_word_list(all_words, 100)
    word_list_medium = generate_word_list(all_words, 1000)
    word_list_large = generate_word_list(all_words, 10000)

    # Benchmarking Dictogram with a small word list
    print("Benchmarking Dictogram...")
    benchmark_histogram_init(Dictogram, 'word_list_small')
    dictogram_small = Dictogram(word_list_small)
    benchmark_frequency_method(Dictogram, 'word_list_small', 'the')

    # Benchmarking Listogram with the same small word list
    print("\nBenchmarking Listogram...")
    benchmark_histogram_init(Listogram, 'word_list_small')
    benchmark_frequency_method(Listogram, 'word_list_small', 'the')

