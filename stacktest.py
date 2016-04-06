# coding: utf-8
import random

# const param
# board
WIDTH = 10
HEIGHT = 10
FIELD_SIZE = HEIGHT * WIDTH
# move
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# food
food = [3, 3]
foodnum = 0

# snake
snake_head = [1, 1]
snake_len = 1
snake = [tuple(snake_head)]

# initialize board
board = [[0] * WIDTH, [0] * WIDTH, [0] * WIDTH, [0] * WIDTH, [0] * WIDTH, [0] * WIDTH, [0] * WIDTH, [0] * WIDTH,
         [0] * WIDTH, [0] * WIDTH]

# temp board mapping
tempboard = [[0] * WIDTH, [0] * WIDTH, [0] * WIDTH, [0] * WIDTH, [0] * WIDTH, [0] * WIDTH, [0] * WIDTH, [0] * WIDTH,
             [0] * WIDTH, [0] * WIDTH]


def calcutmpboard(mFood):
    for ti in range(0, HEIGHT):
        for tj in range(0, WIDTH):
            if ti == 0 or tj == 0 or ti == HEIGHT - 1 or tj == WIDTH - 1:
                tempboard[ti][tj] = 255
            elif board[ti][tj] == 254:
                tempboard[ti][tj] = 254
            else:
                dist = abs(ti - mFood[0]) + abs(tj - mFood[1])
                tempboard[ti][tj] = dist
    print tempboard


def cleanboard():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if i == 0 or j == 0 or i == HEIGHT - 1 or j == WIDTH - 1:
                board[i][j] = 255
            else:
                board[i][j] = 0


# print board
def printboard(msnake, mfood):
    cleanboard()
    setsnake(msnake)
    putfood(mfood)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if board[i][j] == 255:
                print "# ",
            elif board[i][j] == 254:
                print "* ",
            elif board[i][j] == 253:
                print "Q ",
            elif board[i][j] == 252:
                print "@ ",
            elif board[i][j] == 0:
                print "  ",
            else:
                pass
        print ' '


# recreate food
def randomfood():
    foodx = random.randint(1, WIDTH - 2)
    foody = random.randint(1, WIDTH - 2)
    if board[foodx][foody] == 0:
        food[0] = foodx
        food[1] = foody
    else:
        randomfood()


# put food into board
def putfood(mfood):
    board[mfood[0]][mfood[1]] = 252


# put the snake into board
def setsnake(msnake):
    for s in msnake:
        board[s[0]][s[1]] = 254


def move(direc):
    if direc == UP:
        if board[snake_head[0] - 1][snake_head[1]] == 0:
            snake.pop()
            snake_head[0] -= 1
            snake.insert(0, tuple(snake_head))
        elif board[snake_head[0] - 1][snake_head[1]] == 252:
            snake_head[0] -= 1
            snake.insert(0, tuple(snake_head))
            randomfood()
    elif direc == DOWN:
        if board[snake_head[0] + 1][snake_head[1]] == 0:
            snake.pop()
            snake_head[0] += 1
            snake.insert(0, tuple(snake_head))
        elif board[snake_head[0] + 1][snake_head[1]] == 252:
            snake_head[0] += 1
            snake.insert(0, tuple(snake_head))
            randomfood()
    elif direc == LEFT:
        if board[snake_head[0]][snake_head[1] - 1] == 0:
            snake.pop()
            snake_head[1] -= 1
            snake.insert(0, tuple(snake_head))
        elif board[snake_head[0]][snake_head[1] - 1] == 252:
            snake_head[1] -= 1
            snake.insert(0, tuple(snake_head))
            randomfood()
    elif direc == RIGHT:
        if board[snake_head[0]][snake_head[1] + 1] == 0:
            snake.pop()
            snake_head[1] += 1
            snake.insert(0, tuple(snake_head))
        elif board[snake_head[0]][snake_head[1] + 1] == 252:
            snake_head[1] += 1
            snake.insert(0, tuple(snake_head))
            randomfood()


randomfood()

while len(snake) < 64:
    printboard(snake, food)
    calcutmpboard(food)
    print "head =", snake_head

    up = tempboard[snake_head[0] - 1][snake_head[1]]
    d = UP
    bfsmin = up
    right = tempboard[snake_head[0]][snake_head[1] + 1]
    if right < bfsmin:
        d = RIGHT
        bfsmin = right
    down = tempboard[snake_head[0] + 1][snake_head[1]]
    if down < bfsmin:
        d = DOWN
        bfsmin = down
    left = tempboard[snake_head[0]][snake_head[1] - 1]
    if left < bfsmin:
        bfsmin = left
        d = LEFT
    move(d)
