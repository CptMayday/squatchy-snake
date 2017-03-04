import random

# Different Game Taunts, add a feeling to get a random taunt matching this feeling
# Accepted feels
# - MAD
# - SAD
# - HUNGRY

def taunt(feels):
    
    if taunt(feels) == "MAD":
        taunt = ['GRRR', 'I\'M MAD BRO', '#TABLEFLIP', '#RAGEQUIT']
    elif taunt(feels) == "SAD":
        taunt = ['SAD', 'WHY YOU DO THIS', ':\'(']
    elif taunt(feels) == "HUNGRY":
        taunt = ['FOOD PLEASE', 'I\'M HANGRY']
    else:
        taunt = ['I\'MMMA WIN, JK', 'LOLOL', 'Come Get Me!']
    
    return random.choice(taunt)