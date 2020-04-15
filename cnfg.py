import os
# screen size to pass to pygame display screen
SCREENSIZE = [640, 640]

# color data to pass to maintanance unit
BACKGROUND = (0, 0, 0)
FONT_COLOR = (0, 255, 255)

# image paths to pass to main game unit(game_start.py)
player_IMAGE_PATH = os.path.join(os.getcwd(), 'resources/you.jpg')

DESTINATION_IMAGE_PATH = os.path.join(os.getcwd(), 'resources/me.jpg')

OBSTACLE_IMAGE_PATH = [os.path.join(os.getcwd(), 'resources/r.jpg'),
                       os.path.join(os.getcwd(), 'resources/x.jpg'),
                       os.path.join(os.getcwd(), 'resources/y.jpg'),
                       os.path.join(os.getcwd(), 'resources/p.jpg')
                       ]
