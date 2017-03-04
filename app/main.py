import bottle
import os
import random


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    # Different Start Taunts
    taunt = ['EZ MID EZ GAME', 'LOLOLOLOL', 'GG GOOD GAME!', '#same']

    head_url = '%s://%s/static/RS.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#003b45',
        'taunt': random.choice(taunt),
        'head_url': head_url,
        'head_type': 'fang',
        "tail_type": "small-rattle",
        'name': 'Squatchy'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    # Different Game Taunts
    taunt = ['GRRR', 'I\'MMMA WIN, JK', 'LOLOL', 'Come Get Me!']

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    return {
        'move': random.choice(directions),
        'taunt': random.choice(taunt)
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
