# coding: utf-8
import random, copy

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
food = [2, 2]
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


def isSafe():
    head = snake_head[:]
    tail = snake[-1]
    print "tail:", tail
    pred = copy.deepcopy(tempboard)
    calcutmpboard(pred, tail)
    print pred


def calcutmpboard(mboard, mfood):
    for ti in range(0, HEIGHT):
        for tj in range(0, WIDTH):
            if ti == 0 or tj == 0 or ti == HEIGHT - 1 or tj == WIDTH - 1:
                mboard[ti][tj] = 255
            elif mboard[ti][tj] == 254:
                mboard[ti][tj] = 254
            else:
                dist = abs(ti - mfood[0]) + abs(tj - mfood[1])
                mboard[ti][tj] = dist


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


def filewrite():
    fp = open("board.txt", 'w')
    for i in range(HEIGHT):
        for j in range(WIDTH):
            fp.write("%3d," % board[i][j])
        fp.write('\n')


randomfood()
fp = open("board.txt", 'w')
fp1 = open("tempboard.txt", 'w')
head = [0, 0]
while len(snake) < 64:
    printboard(snake, food)
    calcutmpboard(tempboard, food)

    for i in range(HEIGHT):
        for j in range(WIDTH):
            fp.write("%3d," % board[i][j])
        fp.write('\n')

    for i in range(HEIGHT):
        for j in range(WIDTH):
            fp1.write("%3d," % tempboard[i][j])
        fp1.write('\n')
    fp1.write("Snake Head: " + str(snake_head) + '\n')
    fp1.write("Snake Tail: " + str(snake[-1]) + "\n\n")
    fp.write("Snake Head: " + str(snake_head) + '\n')
    fp.write("Snake Tail: " + str(snake[-1]) + "\n\n")

    print "head =", snake_head
    isSafe()

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
    if head == snake_head:
        fp.close()
        fp1.close()
        break
    else:
        head = snake_head[:]
