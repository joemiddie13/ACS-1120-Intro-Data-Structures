import re

def tokenize(text):
    """
    Tokenizes the given text into individual words and punctuation marks.
    
    This function uses regular expressions to handle edge cases such as punctuation attached to words,
    multiple consecutive spaces, and the need to maintain punctuation as separate tokens. It also converts
    all tokens to lowercase to standardize the output, facilitating further text processing tasks like
    frequency analysis or input to machine learning models.
    
    Args:
        text (str): The text to be tokenized.

    Returns:
        list: A list of tokens extracted from the text.
    """
    
    # Use regular expressions to handle edge cases:
    # 1. Separate punctuation from words by adding spaces around punctuation marks.
    #    This is crucial for ensuring punctuation is treated as separate tokens.
    text = re.sub(r'([.,;!?()"])', r' \1 ', text)

    # 2. Replace multiple consecutive spaces with a single space to avoid empty tokens
    #    when splitting the text. This can occur after separating punctuation or from
    #    formatting inconsistencies in the source text.
    text = re.sub(r'\s{2,}', ' ', text)

    # Split the text into tokens based on whitespace. At this point, punctuation marks
    # are surrounded by spaces and will be treated as separate tokens.
    tokens = text.split()

    # Convert all tokens to lowercase to standardize them. This is a common practice in
    # text processing to reduce the variability between tokens that are the same except
    # for their casing (e.g., "The" vs. "the").
    tokens = [token.lower() for token in tokens]

    return tokens

# Example usage of the tokenizer with a sample text from "Treasure Island".
if __name__ == '__main__':
    sample_text = """
    "The Man of the Island

    FROM the side of the hill, which was here steep and stony, a spout of
    gravel was dislodged and fell rattling and bounding through the trees.
    ...
    ...
    "Now, Jim, you tell me true: that ain't Flint's ship?" he asked.
    """

    # Tokenize the sample text and print the resulting tokens.
    tokens = tokenize(sample_text)
    print(tokens)
