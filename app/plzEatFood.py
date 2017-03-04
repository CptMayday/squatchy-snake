# Collect Food Code

# Find snake ID
def myHeadCheck(data):

    for snake in data['snakes']:

        #this is your snake
        if snake['id'] == data['you']:

            #return the location of our head
            return snake['coords'][0, 1]

# Collect food data
def foodCheck(data):

    for food in data['food']:

        return food['coords'][0, 1]

# Determine closes food piece
