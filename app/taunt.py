import random

# Different Game Taunts, add a feeling to get a random taunt matching this feeling
# Accepted feels
# - MAD
# - SAD
# - HUNGRY

def taunt(feels):

    if feels == "MAD":
        tauntOptions = ['GRRR', 'I\'M MAD BRO', '#TABLEFLIP', '#RAGEQUIT']
    elif feels == "SAD":
        tauntOptions = ['SAD', 'WHY YOU DO THIS']
    elif feels == "HUNGRY":
        tauntOptions = ['FOOD PLEASE', 'I\'M HANGRY', 'I\'m HANGY!]
    else:
        tauntOptions = ['I\'MMMA WIN, JK', 'LOLOL', 'Come Get Me!']

    return random.choice(tauntOptions)
