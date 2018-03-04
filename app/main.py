import bottle
import os
import random
import json
 
@bottle.route('/')
def static():
    return "the server is running"
 
 
 
@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')
 

#def end(): 
#    game id
#    winner id
#    turns completed
   
 
@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data.get('game_id')
    board_width = data.get('width')
    board_height = data.get('height')
 
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )
 
    return {
        'color': '##C5B358',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': 'fang',
        'tail_url': 'fat-rattle',
        'name': 'Snakes on a Board'
    }
 
 
 
@bottle.post('/move')
def move():
#choosing a safe move
#live
#not wall
#not other snake
    data = bottle.request.json
 
    goalFood = data['food']['data'][0]
 
    currPosHeadX = data['you']['body']['data'][0]['x']
    currPosHeadY = data['you']['body']['data'][0]['y']
 
    directions = ['up', 'down', 'left', 'right']
    #direction = random.choice(directions)
        
    if(goalFood['x'] < currPosHeadX):
        direction = 'left'
 
    if(goalFood['x'] > currPosHeadX):
        direction = 'right'
 
    if(goalFood['y'] < currPosHeadY):
        direction = 'up'
 
    if(goalFood['y'] > currPosHeadY):
        direction = 'down'
 
    return {
        'move': direction,
        'taunt': 'Suck a bag of Snakes!'
    }
 
 
 
# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug = True)