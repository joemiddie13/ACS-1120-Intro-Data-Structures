from flask import Flask, render_template
import book_histogram
import sample

app = Flask(__name__)

@app.route('/')
def home():
    histogram = book_histogram.histogram('treasure_island_book.txt')
    sentence = sample.generate_sentence(histogram, word_count=13)
    return render_template('index.html', sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True)
