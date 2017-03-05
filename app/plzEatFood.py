# Collect Food Code

# Find snake
def mySnakeCheck(snakeData):

    for snake in snakeData['snakes']:

        #this is your snake
        if snake['id'] == snakeData['you']:

            #return snake
            return snake

# Find snake head location
def myHeadCheck(mySnake):

    #return snake head location
    return mysnake['coords'][0]

# Find food
def myFoodCheck(foodData):

    for food in foodData['food']:

        #return food
        return food

# Find food location
def myFoodLocationCheck(myFood):

    #return food location
    return food['coords']

# Determine closes food piece
def myClosesFoodCheck(myHead, findFood):

    #return closes food locations
    return location

# Main Function
def plzEatFood(moveData):

    # Snake
    mySnake = mySnakeCheck(snakeData)
    myHead = myHeadCheck(mySnake)

    # Food
    myFood = myFoodCheck(foodData)
    findFood = myFoodLocationCheck(myFood)

    # Do a Food Check

    return getzThemFood
