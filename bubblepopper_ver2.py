import curses
import random

win = curses.initscr()


def main_screen():  # defines the enter screen
    curses.noecho()
    curses.curs_set(0)
    win.keypad(1)
    win.border(0)
    menu_bar = "Press p to Play"
    quit = "Press q to Quit"
    win.addstr(curses.LINES // 2, (curses.COLS - len(menu_bar)) // 2, menu_bar)  # overwrited to place to the middle
    win.addstr(curses.LINES // 2 + 1, (curses.COLS - len(quit)) // 2, quit)  # overwrited to place to the middle


def randomch():
    charlist = ["x", "c", "v", "b", "n", "m", "d", "f", "g", "h", "j"]
    randomchar = random.randrange(len(charlist))
    return charlist[randomchar]


def randompoz():
    randomp = random.randrange(24, curses.COLS - 1)
    return randomp


def game_over():
    win.clear()
    win.border(0)
    this_is_the_end = "Game Over!"
    win.addstr(curses.LINES // 2, (curses.COLS - len(this_is_the_end)) // 2, this_is_the_end)
    restart = "Press [Shift + R] if you want to try again"
    win.addstr(curses.LINES // 2 + 2, (curses.COLS - len(restart)) // 2, restart)


def main():
    char = 2
    level = 1
    score = 0
    wintime = 100
    win.addstr(0, 0, "Score: 0")
    string = "LEVEL: 1"
    win.addstr(curses.LINES - 2, (curses.COLS - len(string)) // 2, string)
    bottom = curses.LINES - 2
    key_pressed = False         # I also made a "bottom" variable to assign the value
    buddy = randomch()
    wl = randompoz()
    while char < bottom:
        win.addch(char, wl, buddy)
        win.addch(char-1, wl, ' ')
        char += 1
        win.refresh()
        win.timeout(wintime - level * 20)
        event = win.getch()
        if char == bottom:
            game_over()     # game ends
        if event == ord(buddy):
            score += 1
            score = str(score)
            win.addstr(0, 0, "Score: " + score)
            score = int(score)
            key_pressed = True
            win.addch(char-1, wl, ' ')
            win.refresh()
            buddy = randomch()
            wl = randompoz()
            char = 2        # assigned to 2 cos it won't clear border this way
        if score == 20:
            level = 2
            with open("littleharry.txt") as f:
                content = f.readlines()
                for i, row in enumerate(content):
                    win.addstr(curses.LINES-16+i, 1, row)
                    win.border(0)
                    title = "Harry Popper"
                    win.addstr(0, (curses.COLS - len(title)) // 2, title)
                    level = str(level)
                    string = " LEVEL: "
                    win.addstr(curses.LINES - 2, (curses.COLS - len(string)) // 2, "LEVEL: " + level)
                    level = int(level)
        elif score == 40:
            level = 3
            level = str(level)
            string = " LEVEL: "
            win.addstr(curses.LINES - 2, (curses.COLS - len(string)) // 2, "LEVEL: " + level)
            level = int(level)


def get_started():
    win.clear()
    win.border(0)
    title = "Harry Popper"
    win.addstr(0, (curses.COLS - len(title)) // 2, title)
    main()


def next_screen():
    while True:
        event = win.getch()
        if event == ord("q"):
            break
        elif event == ord("R"):
            win.clear()          # restart, calling the main again
            main_screen()
        elif event == ord("p"):
            get_started()


main_screen()
next_screen()


curses.endwin()
