from flask import Flask, render_template, redirect, session, flash, reqeust
from util import import questions

app = Flask(__name__)

# for creating games or redirecting if game already exists in session
@app.route('/', methods=['GET'])
def index():
    # check if game already exists
    if 'game_board' in session:
        return redirect('/play')

    players = []
    categories = []

    # check for form info
    if request.args.get('submit'):
        valid = True
        players = get_players_from_form()
        if len(players) == 0:
            valid = False
            flash('Please enter at least one player name')
        categories = get_categories_from_form()
        if len(categories) != 5:
            valid = False
            flash('Please choose all five categories')
        print 'Received players:', players
        print 'Received categories:', categories
        if valid:
            session['players'] = players
            session['categories'] = categories
            return redirect('/create_game')
    return render_template('base.html', 
            players=players, 
            categories=categories)

def get_players_from_form():
    players = []
    for i in range(1, 6):
        player = eval('request.args.get("player%d")' % i)
        if player:
            players.append(player)
    return players

def get_categories_from_form():
    categories = []
    for i in range(1, 6):
        category = eval('request.args.get("category%d")' % i)
        if category:
            categories.append(category)
    return categories

# send to 'waiting' page until the api responds with game created
# the page itself should redirect to play
@app.route('/create_game')
def create_game_waiting():
    if not 'categories' in session or not 'players' in session:
        return redirect('/')
    if 'game_board' in session:
        return redirect('/play')
    categories = session['categories']
    print 'Creating game with players:', players
    print 'Creating game with categories:', categories
    return 'creating game rn'

# once game is created, redirect to play route
@app.route('/created_game')
def create_game():
    if not 'categories' in session or not 'players' in session:
        return redirect('/')
    categories = session['categories']
    players = session['players']
    game_board = []
    scores = []
    for category in categories:
        game_board.append(questions.questiondict(category))
    for player in players:
        scores.append({'name':player, 'score':0})
    return redirect('/play')

# display game board and scores
@app.route('/play')
def play():
    return 'playing game rn'

if __name__ == '__main__':
    app.run(debug=True)
