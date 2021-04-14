from flask import Flask
from flask import jsonify

app = Flask(__name__)
### routes
@app.route('/')
def index():
    return 'Index Page'

@app.route('/books')
def books():
    # Use a breakpoint in the code line below to debug your script.
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
    print('Books')
    print(jsonify(dbooks))
    print()
    return jsonify(dbooks)
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
