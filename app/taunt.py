# Different Game Taunts
def taunt();
    
    data = bottle.request.json
    taunt = ['GRRR', 'I\'MMMA WIN, JK', 'LOLOL', 'Come Get Me!']
    
    return random.choice(taunt)