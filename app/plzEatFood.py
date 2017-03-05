from dontDie import dontDie
import math
# Collect Food Code

# Find food
def myFoodCheck(foodData):

    for food in foodData['food']:

        #return food
        return food

# Determine closes food piece
def myClosestFoodCheck(myFood, myHead):
    closestDist = 20
    closestFood = []

    #math
    for food in myFood:
        dx = abs(myHead[0] - food[0])
        dy = abs(myHead[1] - food[1])
        distance = dx + dy

        if distance < closestDist:
            closestFood = food


    #return closes food locations
    return closestFood

def moveToFood():


# Main Function
def plzEatFood(foodData, myHead):


    myFood = myFoodCheck(foodData)

    myClosestFoodCheck(myFood, myHead)

    # Do a Food Check

    return getzThemFood
