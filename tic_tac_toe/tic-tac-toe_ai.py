import random
import os
import subprocess

# variables
d = {11:"11", 12:"12", 13:"13",
     21:"21", 22:"22", 23:"23",
     31:"31", 32:"32", 33:"33"}
gameover = False

def counter():
    pass
def print_board():
	pass
def clear_screen():
	pass
def check_game_over():
	pass
def computer_move():
	pass
def user_move():
	pass
def game_loop():
	while not gameover:
        print_board()
        user_move()
        computer_move()
        check_game_over()
if __name__ == '__main__':
    game_loop()