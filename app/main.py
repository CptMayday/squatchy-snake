from plzEatFood import *

import bottle
import os
import random
import math
import json
import taunt


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    print "Hello"
    
    # Different Start Taunts
    taunt = ['EZ MID EZ GAME', 'LOLOLOLOL', 'GOOD GAME!', '#same', 'REKT', 'GG WP']

    head_url = '%s://%s/static/RS.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        "secondary_color": "#65DB60",
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
    
    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    return {
        'move': random.choice(directions),
        'taunt': taunt
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
