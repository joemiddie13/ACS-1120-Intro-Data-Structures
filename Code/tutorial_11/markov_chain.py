import random
from collections import defaultdict, deque

def build_markov_chain(corpus, order=2):
    """
    Builds a Markov chain from a given text corpus.

    Args:
    - corpus: The text corpus from which to build the Markov chain.
    - order: The order of the Markov chain, which indicates how many previous tokens to consider for the state.

    Returns:
    - A dictionary representing the Markov chain, where each key is a state (tuple of tokens),
      and each value is a dictionary of following tokens and their probabilities.
    """
    markov_chain = defaultdict(lambda: defaultdict(int))
    corpus_words = corpus.split()
    state_queue = deque(maxlen=order)

    for word in corpus_words:
        if len(state_queue) == order:
            state = tuple(state_queue)
            markov_chain[state][word] += 1
        state_queue.append(word)

    for state, next_words in markov_chain.items():
        total_counts = sum(next_words.values())
        markov_chain[state] = {word: count / total_counts for word, count in next_words.items()}

    return dict(markov_chain)

def get_starting_state(markov_chain):
    """
    Selects a random starting state from the Markov chain.

    Args:
    - markov_chain: The Markov chain from which to select the starting state.

    Returns:
    - A tuple representing the starting state.
    """
    return random.choice(list(markov_chain.keys()))

def generate_sentence(markov_chain, order=2, starting_state=None, length=21):
    """
    Generates a sentence using the provided Markov chain.

    Args:
    - markov_chain: The Markov chain used for sentence generation.
    - order: The order of the Markov chain.
    - starting_state: Optional. The starting state for the sentence. If None, a random state will be chosen.
    - length: The desired length of the generated sentence.

    Returns:
    - A string representing the generated sentence.
    """
    current_state = starting_state if starting_state is not None else get_starting_state(markov_chain)
    sentence = list(current_state)

    for _ in range(length - len(current_state)):
        next_word_choices = markov_chain.get(current_state, None)
        if not next_word_choices:
            break
        next_word = random.choices(list(next_word_choices.keys()), weights=next_word_choices.values())[0]
        sentence.append(next_word)
        current_state = tuple(sentence[-order:])

    return ' '.join(sentence)

if __name__ == '__main__':
    corpus = "I went left, you went right, I went left, I went right,"
    chain = build_markov_chain(corpus, order=2)
    sentence = generate_sentence(chain, order=2, length=10)
    print(sentence)
