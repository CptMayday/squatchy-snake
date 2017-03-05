from dontDie import dontDie
import math
# Collect Food Code

# Find food
def myFoodCheck(foodData):

    for food in foodData['food']:

        #return food
        return food

# Determine closes food piece
def myClosestFoodCheck(myFood, data):

    snake = mySnakeCheck(data)
    myHead = myHeadCheck(snake)

    closestDist = 20
    closestFood = []

    #math
    for food in myFood:
        dx = myHead[0] - food[0]
        dy = myHead[1] - food[1]
        distance = abs(dx) + abs(dy)

        if distance < closestDist:
            closestFood = food

            if dx > 0 and dx > dy:
                closestDir = "right"
            if dx < 0 and dx > dy:
                closestDir = "left"
            if dy > 0 and dy > dx:
                closestDir = "down"
            if dy < 0 and dy > dx:
                closestDir = "up"

    #return closes food locations
    return closestDir

# Main Function
def plzEatFood(data):

    foodData = data['food']

    snake = mySnakeCheck(data)
    myHead = myHeadCheck(snake)

    myFood = myFoodCheck(foodData)
    direction = foodDirection(myClosestFoodCheck(myFood, myHead), myHead)

    return
