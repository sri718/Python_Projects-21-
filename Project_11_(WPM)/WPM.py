import curses
from curses import wrapper
import time
import random

def start_scr(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to TEST.\n")
    stdscr.addstr("Press any key to start!")
    stdscr.refresh()
    stdscr.getkey()

def check_display(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"WPM: {wpm}")

    for i, char in enumerate(current):
        color = curses.color_pair(1)
        if char != target[i]:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

def load_text():
    with open("WPM_content_P11.txt",'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip() 

def wpm(lines,stdscr):
    target = load_text()
    current_text = []
    wpm = 0
    s_time = time.time()
    stdscr.nodelay(True)
    # don't block for the key.

    while True:
        
        time_taken = max(time.time() - s_time, 1)
        wpm = round((len(current_text)/(time_taken/60))/5)
        # cpm/5 --> avg len of word is assumed as 5.
        
        stdscr.clear()
        check_display(stdscr, target, current_text,wpm)
        stdscr.refresh()

        if "".join(current_text) == target:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:                           # ASCII of esc button.
            break

        if key in ("KEY_BACKSPACE",'\b',"\x7f"):     # for diff os. - \x7f
            if len(current_text)>0:
                current_text.pop()
        elif len(target) > len(current_text):
            current_text.append(key)
        
    
    
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_scr(stdscr)

    while True:
        lines = load_text()
        wpm(lines,stdscr)

        stdscr.addstr(2,0, "You completed the test! Press any key to continue...")
        
        try:
            key = stdscr.getkey()
        except:
            break

        #if esc in the middle of the test it will make an exception so try-except

        if ord(key) == 27:
            break 
    
    
wrapper(main)
