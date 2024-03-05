#Name: Jack Chou
#Date: 10/07/2023
#Purpose: Create pong game

from cs1lib import *
PH = 80
PW = 20
N = 400
OFFSET = 5

BR = 10
BALLXOFFSET = 1
BALLYOFFSET = 1

LEFTUP = "a"
LEFTDOWN = "z"
RIGHTUP = "k"
RIGHTDOWN = "m"
START = " "
QUIT = "q"

ball_x = N / 2
ball_y = N / 2

x1 = 0
y1 = 0
x2 = N - PW
y2 = N - PH


a = False
z = False
k = False
m = False
startgame = False
quitgame = False




def draw_ball():
    global BR, ball_x, ball_y
    draw_circle(ball_x, ball_y , BR)

def draw_paddle():
    global x1, y1, x2, y2
    draw_rectangle(x1, y1, PW, PH)
    draw_rectangle(x2, y2, PW, PH)
    set_stroke_color(1, 1, 1)
    set_fill_color(1, 1, 1)

def start_screen():
    global x1, y1, x2, y2, ball_x, ball_y
    draw_ball()
    draw_paddle()




def paddle_movement():
    global x1, x2, y1, y2, a, z, k, m
    if (y1 > 0) and a:
        y1 = y1 - OFFSET
    if (y1 < (N - PH)) and z:
        y1 = y1 + OFFSET
    if (y2 > 0) and k:
        y2 = y2 - OFFSET
    if (y2 < (N - PH)) and m:
        y2 = y2 + OFFSET


def ball_movement():
    global ball_x, ball_y
    ball_x = ball_x + BALLXOFFSET
    ball_y = ball_y - (BALLYOFFSET * 2)

def check_wall_collision():
    global BR, ball_y, ball_x, BALLYOFFSET
    if (ball_y - BR) <= 0 or (ball_y + BR) >= N:
        BALLYOFFSET = -BALLYOFFSET * 1.1

def vert_wall_collision():
    global BR, ball_x, N, quitgame, startgame, BALLXOFFSET, BALLYOFFSET

    if (ball_x + BR) == N:
        reset()
    elif (ball_x - BR) == 0:
        BALLXOFFSET = -BALLXOFFSET
        BALLYOFFSET = - BALLYOFFSET
        reset()



def check_paddle_collision():
    global x1, y1, x2, y2, ball_x, BALLXOFFSET, BALLYOFFSET, PW, PH, BR
    if ((ball_x + BR) >= (N - PW)) and (y2 <= ball_y <= y2 + PH):
        BALLXOFFSET = -BALLXOFFSET
    elif ((ball_x - BR) <= (x1 + PW)) and (y1 <= ball_y <= y1 + PH):
        BALLXOFFSET = -BALLXOFFSET



def reset():
    global PW, PH, x1, x2, y1, y2, ball_x, ball_y, startgame, BALLYOFFSET
    x1 = 0
    y1 = 0
    x2 = N - PW
    y2 = N - PH
    ball_x = N / 2
    ball_y = N / 2
    BALLYOFFSET = 1

    startgame = False



def my_kpress(value):
    global a, z, k, m, startgame, quitgame

    if value == LEFTUP: #left paddle moves up
        a = True
    if value == LEFTDOWN: #left paddle moves down
        z = True
    if value == RIGHTUP: #right paddle moves up
        k = True
    if value == RIGHTDOWN: #right paddle moves down
        m = True
    if value == START:
        startgame = True
    if value == QUIT:
        quitgame = True



def my_krelease(value):
    global a, z, k, m
    if value == LEFTUP:
        a = False
    if value == LEFTDOWN:
        z = False
    if value == RIGHTUP:
        k = False
    if value == RIGHTDOWN:
        m = False

def set_background():
    set_clear_color(0, 0, 0)
    clear()


def canvas():
    global startgame, quitgame
    set_background()
    start_screen()

    if startgame:
        ball_movement()
        paddle_movement()
        check_wall_collision()
        check_paddle_collision()
        vert_wall_collision()
    if quitgame:
        cs1_quit()





start_graphics(canvas, width=N, height=N, key_press=my_kpress, key_release=my_krelease)