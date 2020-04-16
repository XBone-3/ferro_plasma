import os
# screen size to pass to game display screen
SCREENSIZE = [640, 640]

# color data to pass to game world
BACKGROUND_BLACK = (0, 0, 0)

BACKGROUND_START_SCREEN = (60, 60, 60)

TITLE_FONT_COLOR = (0, 255, 255)

CONTENT_FONT_COLOR = (255, 255, 0)

# frame rate of the game
FRAME_RATE = 30

# font path to pass to start screen interface
TITLE_FONT_PATH = os.path.join(os.getcwd(), 'resources/fonts/OpenSans-Bold.ttf')

CONTENT_FONT_PATH = os.path.join(os.getcwd(), 'resources/fonts/OpenSans-Italic.ttf')


# image paths to pass to main game unit(game_start.py)
player_IMAGE_PATH = os.path.join(os.getcwd(), 'resources/png/you.png')

DESTINATION_IMAGE_PATH = os.path.join(os.getcwd(), 'resources/png/me.png')

OBSTACLE_IMAGE_R_PATH = os.path.join(os.getcwd(), 'resources/png/r.png')

OBSTACLE_IMAGE_X_PATH = os.path.join(os.getcwd(), 'resources/png/x.png')

OBSTACLE_IMAGE_Y_PATH = os.path.join(os.getcwd(), 'resources/png/y.png')

OBSTACLE_IMAGE_P_PATH = os.path.join(os.getcwd(), 'resources/png/p.png')

OBSTACLE_IMAGE_F_PATH = os.path.join(os.getcwd(), 'resources/png/f.png')
