from p5 import *
import random

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

players = ('X', 'O')
currentPlayer = random.randint(0,1)
ai = 1
human = 0
# 0 -> human ......... 1-> ai

width = 400
height = 400
w = width/3
h = height/3


def setup():
    size(width, height)
    


scores = {'X': -10, 'O': 10, 'tie': 0}


def wincheck():
    global win_index
    res = 2
    match = 'tie'
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
    for i in range(3):
        for j in range(3):
            if board[i][j]=='':
                res=0
                match=None
                break
        # return res, match
    return res, match

def minimax(depth, toMaxi):
    global board
    res, match = wincheck()
    if res != 0:
        return scores[match]-(depth/10)
    if toMaxi:
        bestscore = -10**9
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = players[ai]
                    score = minimax(depth+1, False)
                    board[i][j] = ''
                    bestscore = max(score, bestscore)
        return bestscore
    else:
        bestscore = 10**9
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = players[human]
                    score = minimax(depth+1, True)
                    board[i][j] = ''
                    bestscore = min(score, bestscore)
        return bestscore


def bestmove():
    global board
    '''
    for every empty pos, put O their and call minimax and get score for that move
    O paka au minimax pakeiki score update kare jadi seta higher
    '''
    bestscore = -10**9
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = players[ai]
                score = minimax(0, False)
                board[i][j] = ''
                if score > bestscore:
                    bestscore = score
                    bi = i
                    bj = j
    nextTurn(bi, bj)


def nextTurn(i, j):
    global currentPlayer
    if board[i][j] == "":
        board[i][j] = players[currentPlayer]
        currentPlayer = int(not currentPlayer)


win_index = []


def draw():
    res, match = wincheck()
    if res == 1 or res == 2:
        if res == 1:
            print(f"{match} wins")
        else:
            print("draw")
        no_loop()
        # return

    if currentPlayer == human and res == 0:
        if mouse_is_pressed:
            i = floor(mouse_x/w)
            j = floor(mouse_y/h)
            nextTurn(j, i)
    elif currentPlayer == ai and res == 0:
        bestmove()

    background(0)
    if res==2:
        stroke(Color(255,0,102))
    else:
        stroke(Color(0,255,153))
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

            if res == 1 and f'{j}{i}' in win_index:
                stroke(Color(0, 100, 255))
            else:
                stroke(Color(0,255,153))

            if spot == players[1]:
                no_fill()
                circle((x, y), w/2)
            elif spot == players[0]:
                xr = w/4
                line((x-xr, y-xr), (x+xr, y+xr))
                line((x+xr, y-xr), (x-xr, y+xr))


if __name__ == '__main__':
    run()
