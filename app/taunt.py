import random

# Different Game Taunts, add a feeling to get a random taunt matching this feeling
# Accepted feels
# - MAD
# - SAD
# - HUNGRY

def taunt(feels):

    

    if taunt(feels) == "MAD":
        tauntOptions = ['GRRR', 'I\'M MAD BRO', '#TABLEFLIP', '#RAGEQUIT']
    elif taunt(feels) == "SAD":
        tauntOptions = ['SAD', 'WHY YOU DO THIS', ':\'(']
    elif taunt(feels) == "HUNGRY":
        tauntOptions = ['FOOD PLEASE', 'I\'M HANGRY']
    else:
        tauntOptions = ['I\'MMMA WIN, JK', 'LOLOL', 'Come Get Me!']

    #return random.choice(tauntOptions)
    return "hi dom!!"
