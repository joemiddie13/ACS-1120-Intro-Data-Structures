from flask import Flask, render_template
import book_histogram
from markov_chain import build_markov_chain, generate_sentence, get_starting_words

app = Flask(__name__)

# Generate the histogram, Markov chain, and starting words from the corpus
histogram = book_histogram.histogram('treasure_island_book.txt')
corpus = ' '.join(histogram.keys())
markov_chain = build_markov_chain(corpus)
starting_words = get_starting_words(corpus)

@app.route('/')
def home():
  # Generate a random sentence using the Markov chain
  sentence = generate_sentence(markov_chain, length=21)
  # Render the home page template with the generated sentence
  return render_template('index.html', sentence=sentence)

# Run the Flask application if this script is executed directly
if __name__ == "__main__":
  app.run(debug=True)
