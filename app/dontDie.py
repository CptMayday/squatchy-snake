import json

def mySnakeCheck(moveData):
    for snake in moveData['snakes']:
        
        #this is your snake
        if snake['id'] == moveData['you']:
            
            #return our snake data
            return snake
        
def myHeadCheck(mySnake):
    
    #return the location of our head
    return mySnake['coords'][0]
        
def wallCheck(myHead, width, height):
    moves = []
    
    #if moving would not hit a wall
    if (myHead[0] - 1) >= 0: moves.append("left")
    if (myHead[0] + 1) <= (width-1): moves.append("right")
    if (myHead[1] - 1) >= 0: moves.append("up")
    if (myHead[1] + 1) <= (height-1): moves.append("down")
    
    print "moves"
    print moves
    
    return moves
    
def snakeCheck(myHead, mySnake, notWall, moveData):
    
    moves = []
    
    shouldMove = {'left': True,'right': True, 'up': True, 'down': True}
    
    myLen = len(mySnake['coords'])
    
    locations = [[(myHead[0]-1),myHead[1]],[myHead[0],(myHead[1]-1)],[(myHead[0]+1),myHead[1]],[myHead[0],(myHead[1]+1)]]
    print "locations"
    print locations
    
    locationDict = {'left': locations[0],'right': locations[1], 'up': locations[2], 'down': locations[3]}
    
    #loop through each snake
    for snake in moveData['snakes']:
        
        #loop through each listed coordinate with a snake in it
        for snakeHereIndex, snakeHere in enumerate(snake['coords']):
        #for snakeHere in data[snake]['coords']:
            
            #loop through the not-wall moves
            #for key, direction in locationDict:
            for key, direction in locationDict.iteritems():
                
                #if there is a snake where we are looking to move
                if direction == snakeHere:
                    
                    #if this is not the head of a shorter snake, then it means its the body of a snake
                    if snakeHereIndex != 0 and myLen <= len(snake['coords']):
                        print key
                        print "False"
                        shouldMove[key] = False
    
    #prepare list of moves from t/f list of safe moves
    #for key, move in shouldMove:
    for key, move in shouldMove.iteritems():
        if move == True:
            moves.append(key)

    #return list of safe move dirrections
    return moves
    
def dontDie(moveData):
    #print "hello world"
    
    isSafeMove = []
    
    mySnake = mySnakeCheck(moveData)
    
    #find where our head is
    myHead = myHeadCheck(mySnake)
    
    #do a wall check
    notWall = wallCheck(myHead, moveData['width'], moveData['height'])
    
    print "notWall"
    print notWall
    
    #do do a snake check
    notSnake = snakeCheck(myHead, mySnake, notWall, moveData)
    
    print "notSnake"
    print notSnake
        
    
    for notWallDir in notWall:
        for notSnakeDir in notSnake:
            
            if notWallDir == notSnakeDir:
                isSafeMove.append(notSnakeDir)
    
    print "isSafeMove"
    print isSafeMove
    #return a list of moves that wont kill you  
    return isSafeMove