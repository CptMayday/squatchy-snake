import json
import random

def combineMoves(dontDieMoves, foodMove):
    for dontDieMove in dontDieMoves:
        if dontDieMove == foodMove:
            return foodMove
        else:
            return dontDieMove