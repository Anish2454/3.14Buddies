from flask import Flask, render_template, redirect, session, flash, reqeust
from util import import questions

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # check if game already exists
    if reqeust.args.get('players'):
        return redirect('/play')

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
        if valid:
            session['players'] = players
            session['categories'] = categories
            return redirect('/create_game')
    return render_template('base.html')

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

@app.route('/create_game')
def create_game():
    if not session['categories']:
        return redirect('/')
    categories = session['categories']
    return 'creating game rn'

@app.route('/play')
def play():
    return 'playing game rn'

if __name__ == '__main__':
    app.run(debug=True)
