from flask import Flask, render_template
import book_histogram
import sample

app = Flask(__name__)

@app.route('/')
def home():
    histogram = book_histogram.histogram('treasure_island_book.txt')
    word = sample.weighted_sample(histogram)
    return render_template('index.html', word=word)

if __name__ == "__main__":
    app.run(debug=True)
