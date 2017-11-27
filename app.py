from flask import Flask, render_template, redirect, session, flash, request
from util import questions
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

# decorator for checking if user is in a game before continuing
def in_game(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'game_board' in session:
            return func(*args, **kwargs)
        return redirect('/')
    return wrapper

# for creating games or redirecting if game already exists in session
@app.route('/')
def index():
    print "\n*** / ***"
    # check if game already exists
    if 'game_board' in session:
        return redirect('/play')

    players = []
    categories = []

    # check for form info
    if request.args.get("submit"):
        valid = True
        players = get_players_from_form()
        if len(players) != 2:
            valid = False
            flash('Please enter two player names')
        categories = get_categories_from_form()
        if len(categories) != 5:
            valid = False
            flash('Please choose exactly five categories')
        print 'Received players:', players
        print 'Received categories:', categories
        if valid:
            session['players'] = players
            session['categories'] = categories
            return redirect('/create_game')
    return render_template('home.html',
            players=players,
            categories=enumerate(questions.get_categories()))

def get_players_from_form():
    players = []
    if request.args.get('player1'):
        players.append(request.args.get('player1'))
    if request.args.get('player2'):
        players.append(request.args.get('player2'))
    return players

def get_categories_from_form():
    categories = []
    for i in range(1, 20):
        category = eval('request.args.get("category%d")' % i)
        if category:
            categories.append(category)
    return categories

# send to 'waiting' page until the api responds with game created
# the page itself should redirect to '/created_game'
@app.route('/create_game')
def create_game_waiting():
    print "\n*** /create_game ***"
    if not 'categories' in session or not 'players' in session:
        return redirect('/')
    if 'game_board' in session:
        return redirect('/play')
    categories = session['categories']
    players = session['players']
    print 'Creating game with players:', players
    print 'Creating game with categories:', categories
    return 'creating game rn'

# once game is created, redirect to play route
@app.route('/created_game')
def create_game():
    print "\n*** /created_game ***"
    if not 'categories' in session or not 'players' in session:
        return redirect('/')
    categories = session['categories']
    players = session['players']
    game_board = {}
    scores = {}
    for category in categories:
        game_board[category] = questions.questiondict(category)
    for player in players:
        scores[player] = 0
    session['game_board'] = game_board
    session['scores'] = scores
    return redirect('/play')

# display game board and scores
@app.route('/play')
@in_game
def play():
    game_board = session['game_board']
    categories = session['categories']
    scores = session['scores']
    players = session['players']
    print '=============CURRENT GAME STATUS============='
    print 'Categories: ', categories
    print 'Game board: ', game_board
    print 'Players: ', players
    print 'Scores: ', scores
    print
    return 'playing game rn'

# display a question and expect an answer
@app.route('/question/<category>/<moolah>')
@in_game
def question(category, moolah):
    categories = session['categories']
    game_board = session['game_board']
    if not category in categories or not moolah in game_board[category]:
        return redirect('/play')
    return 'displaying question: %s' % game_board[category][moolah][0]

# checks given answer and redirects back to question or displays correct answer
@app.route('/answer/<category>/<moolah>')
@in_game
def answer(category, moolah):
    if not request.args.get('answer'):
        return redirect('/question/%s/%s' % (category, moolah))
    given_answer = request.args.get('answer')
    actual_answer = session['game_board'][category][moolah][1]
    return 'given: %s<br>actual: %s' % (given_answer, actual_answer)

# clears game_board to restart
@app.route('/new_game')
@in_game
def new_game():
    session.pop('game_board')
    session.pop('categories')
    session.pop('players')
    session.pop('scores')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
