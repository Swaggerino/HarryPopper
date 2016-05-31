import curses

def main(scr):
    screen = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    screen.keypad(1)

    top_pos = 12
    left_pos = 32
    screen.addstr(top_pos, left_pos, "Press p to play")
    top_pos = 13
    left_post = 32
    screen.addstr(top_pos, left_pos, "Press q to Quit")

    while True:
        event = screen.getch()
        if event == ord("q"): break
        elif event == ord("p"):
            screen.clear()
            top_pos = 0
            left_pos = 5
            screen.addstr(top_pos, left_pos, "X")
            while (top_pos < 14):
                top_pos += 1



curses.wrapper(main)
curses.endwin()
