import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "#", "#", "#", "#", "#", "O", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]                                                                   # change as per need.

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i,j
    return None

def find_path(maze, stdscr):
    start = 'O'
    end = 'X'
    start_pos = find_start(maze,start)

    q = queue.Queue()
    q.put((start_pos,[start_pos]))

    visited = set()
    visited.add(start_pos) 

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neis = find_neis(maze,row,col)
        for nei in neis:
            if nei in visited:
                continue

            r,c = nei
            if maze[r][c] == '#':
                continue

            new_path = path + [nei]
            q.put((nei,new_path))  
            visited.add(nei)
            
def find_neis(maze,row,col):
    neis = []

    if row > 0:
        neis.append((row - 1,col))
    if row + 1 < len(maze):
        neis.append((row + 1,col))
    if col > 0:
        neis.append((row, col - 1))
    if col + 1 < len(maze[0]) :
        neis.append((row, col + 1))

    return neis

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,'O',RED)
            else:
                stdscr.addstr(i,j*2,value,BLUE)

def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getkey()

wrapper(main)
    
