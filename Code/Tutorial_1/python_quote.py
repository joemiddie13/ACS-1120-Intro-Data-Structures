import random

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")


def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)

# 1. Import the random module.
# 2. Define a tuple of quotes.
# 3. Define a function random_python_quote:
  # Generate a random index within the range of the quotes tuple.
  # Return the quote at the randomly generated index.
# 4. Check if the script is being run directly (not imported as a module):
  # If true, call the random_python_quote function and store the returned quote.
  # Print the quote.