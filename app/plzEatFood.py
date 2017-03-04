# Collect Food Code

# Find snake ID
def mySnakeCheck(snakeData):

    for snake in snakeData['snakes']:

        #this is your snake
        if snake['id'] == snakeData['you']:

            #return the location of our head
            return snake

# Collect food data
def foodCheck(foodData):

    for food in foodData['food']:

        return food

# Determine closes food piece
