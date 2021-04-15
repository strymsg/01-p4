from flask import Flask
from flask import jsonify

app = Flask(__name__)


dbooks = [
        {
            'id': 0,
            'title': 'A Fire Upon the Deep',
            'author': 'Vernor Vinge',
            'first_sentence': 'The coldsleep itself was dreamless.',
            'year_published': '1992'
        },
        {
            'id': 1,
            'title': 'The Ones Who Walk Away From Omelas',
            'author': 'Ursula K. Le Guin',
            'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
            'published': '1973'
        },
        {
            'id': 2,
            'title': 'Dhalgren',
            'author': 'Samuel R. Delany',
            'first_sentence': 'to wound the autumnal city.',
            'published': '1975'
        }
]

def get_book(key='id', value=1):
    for book in dbooks:
        got = book.get(key, None)
        if  got is not None and got == value:
            return book
    return {}

## routes
@app.route('/')
def index():
    return 'Index Page'

@app.route('/books')
def books():
    # Use a breakpoint in the code line below to debug your script.
    print('Books')
    print(jsonify(dbooks))
    print()
    return jsonify(dbooks)

@app.route('/book/<book_id>')
def book(book_id):
    return jsonify(get_book(key='id', value=int(book_id)))