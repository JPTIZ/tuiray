import curses
from curses import wrapper


def loop(stdscr):
    pad = curses.newpad(100, 100)

    pad.addstr(0, 0, "Test mode", curses.A_REVERSE | curses.color_pair(1))

    c = stdscr.getch()
    if c == ord('q'):
        exit(0)
    elif c == ord('p'):
        stdscr.addstr('pressed P!')
    stdscr.refresh()

    pad.refresh(0, 0, 5, 5, 20, 75)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

    while True:
        loop(stdscr)
        stdscr.clear()

    stdscr.refresh()


if __name__ == '__main__':
    wrapper(main)
