import os
import subprocess
import random


def available_spots():
    avail_spots = []
    for i in range(1, 10, 1):
        if board[i] == i:
            avail_spots.append(i)
    return avail_spots


def filled_spots():
    o_spots = []
    x_spots = []
    for i in range(1, 10, 1):
        if board[i] == 'o':
            o_spots.append(i)
        if board[i] == 'x':
            x_spots.append(i)
    return o_spots, x_spots


def print_board(board_in):
    print(f'''{board_in[1]}|{board_in[2]}|{board_in[3]}
{board_in[4]}|{board_in[5]}|{board_in[6]}
{board_in[7]}|{board_in[8]}|{board_in[9]}''')


def update_board(board_in):
    board_in[user_move()] = 'o'
    if len(available_spots()) != 0:
        board_in[computer_move(board_in)] = 'x'


def clear_screen():
    subprocess.run('clear.bat')


def computer_move(board_in):
    avail_spots = available_spots()
    if (9 - len(avail_spots)) < 3:
        computer_output = random.choice(avail_spots)
        return computer_output if computer_output in avail_spots else computer_output + 1
    else:
        for i in (1, 4, 7):
            o_count = 0
            for j in (i, i + 1, i + 2):
                if board_in[j] == 'o':
                    o_count += 1
                    if o_count == 2:
                        computer_output = j + 1
                        return computer_output if computer_output in avail_spots else random.choice(avail_spots)
                else:
                    o_count = 0
        for i in (1, 2, 3):
            o_count = 0
            for j in (i, i + 3, i + 6):
                if board_in[j] == 'o':
                    o_count += 1
                    if o_count == 2:
                        computer_output = j + 1
                        return computer_output if computer_output in avail_spots else random.choice(avail_spots)
                else:
                    o_count = 0


def user_move():
    while True:
        print('select a spot')
        print(available_spots())
        try:
            user_input = int(input('enter a spot in available spots: '))
            if user_input in available_spots() or len(available_spots()) == 0:
                break
            else:
                print('not a valid spot')
        except ValueError as v:
            print('raised an error due to invalid input: ', v)
    return user_input


def check_game_over(board_in):
    for i in [1, 4, 7]:
        o_count = 0
        x_count = 0
        for j in (i, i + 1, i + 2):
            if board_in[j] == 'o':
                o_count += 1
                if o_count == 3:
                    print('you won')
                    return True
            if board_in[j] == 'x':
                x_count += 1
                if x_count == 3:
                    print('you lose')
                    return True
    for i in (1, 2, 3):
        o_count = 0
        x_count = 0
        for j in (i, i + 3, i + 6):
            if board_in[j] == 'o':
                o_count += 1
                if o_count == 3:
                    print('you won')
                    return True
            if board_in[j] == 'x':
                x_count += 1
                if x_count == 3:
                    print('you lose')
                    return True
    for i in [[1, 5, 9], [3, 5, 7]]:
        d_o_count = 0
        d_x_count = 0
        for j in i:
            if board_in[j] == 'o':
                d_o_count += 1
                if d_o_count == 3:
                    print('you win')
                    return True
            if board_in[j] == 'x':
                d_x_count += 1
                if d_x_count == 3:
                    print('you lose')
                    return True
    if len(available_spots()) == 0:
        print("it's a tie")
    return True if len(available_spots()) == 0 else False


def main(end_game):
    while not end_game:
        print_board(board)
        update_board(board)
        # clear_screen()
        if (9 - len(available_spots())) > 4:
            end_game = check_game_over(board)
            if check_game_over(board):
                print_board(board)
                os.remove('clear.bat')


if __name__ == '__main__':
    board = {1: 1, 2: 2, 3: 3,
             4: 4, 5: 5, 6: 6,
             7: 7, 8: 8, 9: 9}
    game_over = False
    clear = open('clear.bat', 'w')
    clear.write('cls')
    clear.close()
    main(game_over)
