# coding: utf-8

import curses, time


def writef():
    fp = open("datas.txt", 'w')
    for i in range(10000000):
        fp.write("ID:" + str(i) + '\n')
    fp.close()


def readf():
    fp = open("datas.txt", "r")
    scr = curses.initscr()
    scr.border(0)
    line = fp.readline()
    time.clock()
    while line != "":
        line = fp.readline()
        scr.refresh()
    # 一亿行数据读取需要180秒
    tm = time.clock()
    scr.addstr(10, 7, str(tm))
    scr.getch()
    fp.close()
    curses.endwin()


def main():
    try:
        readf()
    except IOError:
        writef()


if __name__ == '__main__':
    main()
