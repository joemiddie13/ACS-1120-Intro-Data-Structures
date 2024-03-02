from flask import Flask, render_template
import markov_chain

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def home():
    """
    Route to render the home page with a randomly generated sentence.

    This function reads the cleaned text of "Treasure Island", builds a Markov chain based on this text,
    and then uses this chain to generate a random sentence. The generated sentence is then passed to the
    'index.html' template for rendering.

    Returns:
        Rendered template 'index.html' with a randomly generated sentence passed as a context variable.
    """
    
    # Read the cleaned text file that was preprocessed to remove unwanted characters and unify spacing.
    # The cleaned text is essential for building an accurate Markov chain without extraneous symbols.
    with open('cleaned_treasure_island.txt', 'r', encoding='utf-8') as file:
        cleaned_text = file.read()

    # Build a Markov chain model from the cleaned text. The 'order' parameter determines the number of
    # preceding words the model will use to predict the next word, with 2 being a common choice for balance
    # between randomness and coherence.
    chain = markov_chain.build_markov_chain(cleaned_text, order=2)
    
    # Use the built Markov chain to generate a random sentence. The 'length' parameter specifies the
    # desired number of words in the generated sentence, providing control over sentence length.
    sentence = markov_chain.generate_sentence(chain, order=2, length=10)

    # Render the 'index.html' template, passing the generated sentence as a context variable to be
    # used within the template. This allows the dynamically generated sentence to be displayed on the web page.
    return render_template('index.html', sentence=sentence)

# The conditional below checks if this script is executed as the "main" program and not imported as a module
# in another script. If it is the main program, the Flask application is run with debugging enabled, which is
# useful during development for automatic reloads and detailed error messages.
if __name__ == "__main__":
    app.run(debug=True)
