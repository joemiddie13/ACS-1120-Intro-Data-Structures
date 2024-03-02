import re

def clean_text(text):
    """
    Cleans the given text by removing punctuation, converting to lowercase, and normalizing whitespace.

    This function is designed to prepare text data for further processing, such as tokenization or analysis,
    by removing elements that are often irrelevant for such tasks, like punctuation and casing, and by ensuring
    consistency in whitespace.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    
    # Remove punctuation from the text. This is achieved by substituting any character that is NOT
    # a word character (\w) or whitespace (\s) with nothing (''), effectively removing them.
    text = re.sub(r'[^\w\s]', '', text)

    # Convert the text to lowercase to standardize it. This helps in reducing the variability
    # of the text and is especially useful in tasks like text comparison or analysis where
    # case differences are not relevant.
    text = text.lower()

    # Normalize whitespace in the text by replacing one or more whitespace characters (\s+)
    # with a single space (' '), and then stripping leading and trailing whitespace.
    # This step ensures that tokens in the text are consistently separated by exactly
    # one space and that there are no leading or trailing spaces in the cleaned text.
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def main():
    """
    The main function for the text cleanup script. It reads text from an input file,
    cleans it using the clean_text function, and writes the cleaned text to an output file.
    """
    
    # Define the paths for the input and output files.
    input_file_path = 'treasure_island_book.txt'
    output_file_path = 'cleaned_treasure_island.txt'

    # Open the input file, read its content, and store it in the 'content' variable.
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Clean the read content using the clean_text function.
    cleaned_content = clean_text(content)

    # Open the output file and write the cleaned content to it.
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

    # Print a confirmation message to the console indicating the output file path.
    print(f'Cleaned book saved to {output_file_path}')

# Check if the script is being run directly (as opposed to being imported as a module)
# and if so, execute the main function.
if __name__ == '__main__':
    main()
