import random

# Different Game Taunts, add a feeling to get a random taunt matching this feeling
# Accepted feels
# - MAD
# - SAD
# - HUNGRY

def taunt(feels):

    if feels == "MAD":
        tauntOptions = ['GRRR', 'I\'M MAD BRO', '#TABLEFLIP', '#RAGEQUIT']
    elif feels == "HUNGRY":
        tauntOptions = ['FOOD PLEASE', 'I\'M HANGRY', 'soooooo HANGY!']
    elif feels == "FULL":
        tauntOptions = ['NOM NOM NOM']
    else:
        tauntOptions = ['I\'MMMA WIN, JK', 'LOLOL', 'Come Get Me!']

    return random.choice(tauntOptions)
