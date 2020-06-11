from p5 import *
import random

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

available = []
players = ('X', 'O')
currentPlayer = 0
ai = 1
human = 0
# 0 -> human ......... 1-> ai

width = 400
height = 400
w = width/3
h = height/3


def setup():
    size(width, height)
    for i in range(3):
        for j in range(3):
            available.append((j, i))


def nextTurn(i, j):
    global available, currentPlayer
    if board[i][j] == "":
        available.remove((i, j))
        board[i][j] = players[currentPlayer]
        currentPlayer = int(not currentPlayer)


win_index = []


def wincheck():
    global win_index
    res = 0
    match = None
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '':
            win_index = [f'0{i}', f'1{i}', f'2{i}']
            res = 1
            match = board[0][i]
            return res, match
        if board[i][0] == board[i][1] == board[i][2] != '':
            win_index = [f'{i}0', f'{i}1', f'{i}2']
            res = 1
            match = board[i][0]
            return res, match
    if board[0][0] == board[1][1] == board[2][2] != '':
        win_index = ['00', '11', '22']
        res = 1
        match = board[0][0]
        return res, match
    if board[2][0] == board[1][1] == board[0][2] != '':
        win_index = ['20', '11', '02']
        res = 1
        match = board[2][0]
        return res, match
    if len(available) == 0:
        res = 2
        # return res, match
    return res, match


def draw():
    res, match = wincheck()
    if res == 1 or res == 2:
        if res == 1:
            print(f"{match} wins")
        else:
            print("draw")
        no_loop()
        # return

    # user
    if mouse_is_pressed:
        i = floor(mouse_x/w)
        j = floor(mouse_y/h)
        nextTurn(j, i)
    # ai

    background(255)
    stroke(0)
    line((w, 0), (w, height))
    line((w*2, 0), (w*2, height))
    line((0, h), (width, h))
    line((0, h*2), (width, h*2))
    for i in range(3):  # i should be j maybe
        for j in range(3):  # j sould be i maybe
            spot = board[j][i]
            x = w*i + w/2
            y = h*j + h/2
            stroke_weight(4)
            # print(win_index)

            if f'{j}{i}' in win_index:
                stroke(Color(0, 0, 255))
            else:
                stroke(0)

            if spot == players[1]:
                no_fill()
                circle((x, y), w/2)
            elif spot == players[0]:
                xr = w/4
                line((x-xr, y-xr), (x+xr, y+xr))
                line((x+xr, y-xr), (x-xr, y+xr))


if __name__ == '__main__':
    run()
