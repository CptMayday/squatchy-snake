import json

def mySnakeCheck(moveData):
    for snake in moveData['snakes']:
        
        #this is your snake
        if data[snake]['id'] == data['you']:
            
            #return our snake data
            return data[snake]
        
def myHeadCheck(mySnake):
    
    #return the location of our head
    return mySnake['coords'][0]
        
def wallCheck(myHead, width, height):
    moves = []
    
    #if moving would not hit a wall
    if (myHead[0] - 1) > 0: moves.append("left")
    if (myHead[0] + 1) < (width-1): moves.append("right")
    if (myHead[1] - 1) > 0: moves.append("up")
    if (myHead[1] + 1) < (height-1): moves.append("down")
    
    return moves
    
def snakeCheck(myHead, mySnake, notWall, moveData):
    
    moves = []
    
    shouldMove = {'left': True,'right': True, 'up': True, 'down': True}
    
    myLen = len(mySnake['coords'])
    
    locations = [[(myHead[0]-1),myHead[1]],[myHead[0],(myHead[1]-1)],[(myHead[0]+1),myHead[1]],[myHead[0],(myHead[1]+1)]]
    
    locationDict = {'left': locations[0],'right': locations[1], 'up': locations[2], 'down': locations[3]}
    
    #loop through each snake
    for snake in moveData['snakes']:
        
        #loop through each listed coordinate with a snake in it
        for snakehereIndex, snakeHere in enumerate(moveData[snake]['coords']):
        #for snakeHere in data[snake]['coords']:
            
            #loop through the not-wall moves
            for key, direction in locationDict:
                
                #if there is a snake where we are looking to move
                if direction == snakeHere:
                    
                    #if this is not the head of a shorter snake, then it means its the body of a snake
                    if snakeHereIndex != 0 and myLen <= len(moveData[snake]['coords']):
                        shouldMove[key] = False
    
    #prepare list of moves from t/f list of safe moves
    for key, move in shouldMove:
        if move == True:
            moves.append(key)

    #return list of safe move dirrections
    return moves
    
def dontDie(moveData):
    print "hello world"
    
    isSafeMove = []
    
    mySnake = mySnakeCheck(moveData)
    
    #find where our head is
    myHead = myHeadCheck(mySnake)
    
    #do a wall check
    notWall = wallCheck(myHead, data['width'], data['height'])
    
    #do do a snake check
    notSnake = snakeCheck(myHead, mySnake, notWall, moveData)
        
    
    for notWallDir in notWall:
        for notSnakeDir in notSnake:
            
            if notWallDir == notSnakeDir:
                siSafeMove.append(notSnakeDir)
    
    #return a list of moves that wont kill you  
    return isSafeMoves