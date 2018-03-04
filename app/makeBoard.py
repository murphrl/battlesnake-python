def makeBoard(data):
    '''Converts data to a board array.
    Board is a 2d array of cells. A cell will be available by the turn
    equal to it's contents. Food = -1. A cell with value turn+1 should be
    safe to move into. (unless someone else moves there at the same time.)
    '''
    WIDTH = data['width']
    HEIGHT = data['height']
    turnNum = data["turn"]
    board = [[0]*WIDTH for _ in range(HEIGHT)]
    
    for food in data["food"]["data"]:
        board[food["x"]][food["y"]] = -1
    for snake in data['snakes']['data']:
        #heads.append((snake['positions'][0],snake['length'],False))
        for i,d in enumerate(snake['body']['data'][::-1]):
            #overwrites in reverse order to handle tail extensions
            print(d)
            x = d['x']
            y = d['y']
            board[x][y]=turnNum+i
    return board