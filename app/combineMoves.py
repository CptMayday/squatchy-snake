import json
import random

def move(dontDieMoves, foodMove):
    for dontDieMove in dontDieMoves:
        if dontDieMove == foodMove:
            return foodMove
        else return random.choice(dontDieMoves)