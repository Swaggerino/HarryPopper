import curses
import time
import random
import string

win = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)


def main_title():
    with open("main.txt") as f:
        content = f.readlines()
        for i, row in enumerate(content):
            win.addstr(curses.LINES // 7+i, curses.COLS // 4, row, curses.color_pair(1))


def last_screen():
    with open("dobby.txt") as f:
        content = f.readlines()
        for i, row in enumerate(content):
            win.addstr(curses.LINES - 18 + i, curses.COLS // 5, row)


def main_screen():
    curses.noecho()
    curses.curs_set(0)
    win.keypad(1)
    main_title()
    win.border(0)
    menu_bar = "Press p to Play"
    quit = "Press q to Quit"
    win.addstr(curses.LINES // 2, (curses.COLS - len(menu_bar)) // 2, menu_bar, curses.A_BOLD)
    win.addstr(curses.LINES // 2 + 1, (curses.COLS - len(quit)) // 2, quit, curses.A_BOLD)


def ghost_erase():
    for i in range(5):
            win.addstr(char - i, wl - 3, '          ')


# def ghost():
#     with open("ghost.txt") as f:
#         content = f.readlines()
#         for i, row in enumerate(content):
#             win.addstr(char-3+i, wl-3, row, curses.color_pair(2))


def randomch():
    randomchar = random.choice(string.ascii_letters + string.digits)
    return randomchar


def randomch_with_specials():
    special_chars = ("$" + "#" + "!" + "%" + "<" + ">" + "¤" + "@")
    randomcharsp = random.choice(string.ascii_letters + string.digits + special_chars)
    return randomcharsp


def randompoz():
    randomp = random.randrange(26, curses.COLS - 10)
    return randomp


def game_over():
    win.clear()
    last_screen()
    win.border(0)
    this_is_the_end = "Game Over!"
    win.addstr(curses.LINES // 2, (curses.COLS - len(this_is_the_end)) // 2, this_is_the_end)
    restart = "Press [Shift + R] if you want to try again"
    win.addstr(curses.LINES // 2 + 2, (curses.COLS - len(restart)) // 2, restart)


def main():
    global char  # global for the ghost movement
    char = 6
    level = 1
    score = 0
    wintime = 120
    win.addstr(1, 1, "[Score: 0]", curses.A_BOLD)
    string = ("LEVEL: 1")
    win.addstr(curses.LINES - 2, (curses.COLS - len(string)) // 2, string, curses.A_BOLD)
    bottom = curses.LINES - 3  # modified not to delete level string
    key_pressed = False         # I also made a "bottom" variable to assign the value
    buddy = randomch()
    global wl  # global for the ghost movement
    wl = randompoz()
    while char < bottom:
        ghost()
        win.addch(char, wl, buddy, curses.A_BOLD)
        win.addstr(char-4, wl-3, '    ')
        char += 1
        win.refresh()
        win.timeout(wintime - level * 15)
        win.border(0)  # enumerate erase border so we need this
        event = win.getch()
        if char == bottom:
            key_pressed = 0
            game_over()     # game ends
        if key_pressed is False:
            with open("littleharry.txt") as f:
                content = f.readlines()
                for i, row in enumerate(content):
                    win.addstr(curses.LINES-17+i, 1, row)
                    win.border(0)
        if event == ord(buddy):
            score += 1
            score = str(score)
            win.addstr(1, 1, "[Score: " + score + "]", curses.A_BOLD)
            score = int(score)
            key_pressed = True
            ghost_erase()
            win.refresh()
            buddy = randomch()
            if score >= 45:
                buddy = randomch_with_specials()
            wl = randompoz()
            char = 6
            with open("littleharry2.txt") as f:
                content = f.readlines()
                for i, row in enumerate(content):
                    win.addstr(curses.LINES-17+i, 1, row)
                    win.border(0)
                    key_pressed = False
        if score == 15:
            level = 2
            level = str(level)
            string = " LEVEL: "
            win.addstr(curses.LINES - 2, (curses.COLS - len(string)) // 2, "LEVEL: " + level, curses.A_BOLD)
            level = int(level)
        elif score == 30:
            level = 3
            level = str(level)
            string = " LEVEL: "
            win.addstr(curses.LINES - 2, (curses.COLS - len(string)) // 2, "LEVEL: " + level, curses.A_BOLD)
            level = int(level)
        elif score == 45:
            level = 4
            level = str(level)
            string = " LEVEL: "
            win.addstr(curses.LINES - 2, (curses.COLS - len(string)) // 2, "LEVEL: " + level, curses.A_BOLD)
            level = int(level)


def get_started():
    win.clear()
    win.border(0)
    title = "<<<Harry Popper>>>"
    win.addstr(1, (curses.COLS - len(title)) // 2, title, curses.A_BOLD)
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
