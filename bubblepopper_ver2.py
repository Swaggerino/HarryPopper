import curses
import time
import random
import string

win = curses.initscr()
curses.start_color()  # This commad allow us to use colors.
curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Initiated the colors
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)   # which we want to use in our game.


def main_title():  # Harry Popper logo appears on the first screen.
    with open("main.txt") as f:
        content = f.readlines()
        for i, row in enumerate(content):
            win.addstr(curses.LINES // 7+i, curses.COLS // 4, row, curses.color_pair(1))


def last_screen():  # A figure (Dobby) appears on the left-bottom side on the screen.
    with open("dobby.txt") as f:
        content = f.readlines()
        for i, row in enumerate(content):
            win.addstr(curses.LINES - 18 + i, curses.COLS // 5, row)


def main_screen():  # Sets the parameters for the game, and appers the menu.
    curses.noecho()
    curses.curs_set(0)
    win.keypad(1)
    main_title()
    win.border(0)
    menu_bar = "Press p to Play"
    quit = "Press q to Quit"
    win.addstr(curses.LINES // 2, (curses.COLS - len(menu_bar)) // 2, menu_bar, curses.A_BOLD)
    win.addstr(curses.LINES // 2 + 1, (curses.COLS - len(quit)) // 2, quit, curses.A_BOLD)


def ghost_erase():  # Deleting ghosts after pushing the right key.
    for i in range(5):
            win.addstr(char - i, wl - 3, '          ')


def ghost():  # Creating a ghost from the additional txt.file.
    with open("ghost.txt") as f:
        content = f.readlines()
        for i, row in enumerate(content):
            win.addstr(char-3+i, wl-3, row)


def randomch():  # Generate a random character.
    randomchar = random.choice(string.ascii_letters + string.digits)
    return randomchar


def randomch_with_specials():  # Generate a random charater  for level 4. Special characters included.
    special_chars = ("$" + "#" + "!" + "%" + "<" + ">" + "¤" + "@")
    randomcharsp = random.choice(string.ascii_letters + string.digits + special_chars)
    return randomcharsp


def randompoz():  # Generate a random x pos for the character.
    randomp = random.randrange(26, curses.COLS - 10)
    return randomp


def game_over():  # This func is responsible for the last screen.
    win.clear()
    last_screen()
    win.border(0)
    this_is_the_end = "Game Over!"
    win.addstr(curses.LINES // 2, (curses.COLS - len(this_is_the_end)) // 2, this_is_the_end, curses.A_BOLD)
    restart = "Press [Shift + R] if you want to try again"
    win.addstr(curses.LINES // 2 + 2, (curses.COLS - len(restart)) // 2, restart, curses.A_BOLD)


def main():  # Where the magic happens :)
    global char  # Had to make global because of the ghost movement.
    char = 6  # Assigned the starting y pos of the character.
    level = 1
    score = 0
    wintime = 120
    win.addstr(1, 1, "[Score: 0]", curses.A_BOLD)
    string = "LEVEL: 1"
    win.addstr(curses.LINES - 2, (curses.COLS - len(string)) // 2, string, curses.A_BOLD)
    bottom = curses.LINES - 3  # This is a line, and when the ghost reach this the game ends.
    key_pressed = False  # It is about to control ghost erase and the "moving" of Harry.
    buddy = randomch()
    global wl  # Had to make global because of the ghost movement.
    wl = randompoz()
    while char < bottom:
        ghost()                                    # Here is where ghost appears.
        win.addch(char, wl, buddy, curses.A_BOLD)  # Here is where character appears.
        win.addstr(char-4, wl-3, '     ')          # This block is responsible
        char += 1                                  # for the moving
        win.refresh()                              # of the
        win.timeout(wintime - level * 15)          # characters
        win.border(0)                              # and the
        event = win.getch()                        # ghost.
        if char == bottom:
            key_pressed = 0  # Assigned 0 to stop calling "littleharry.txt"
            game_over()
        if key_pressed is False:
            with open("littleharry.txt") as f:
                content = f.readlines()
                for i, row in enumerate(content):
                    win.addstr(curses.LINES-17+i, 1, row)
                    win.border(0)
        if event == ord(buddy):  # This is where we control what should happen if the player hits the right key.
            score += 1
            score = str(score)
            win.addstr(1, 1, "[Score: " + score + "]", curses.A_BOLD)
            score = int(score)
            key_pressed = True  # Assigned True to call littleharry2.txt.
            ghost_erase()
            win.refresh()
            buddy = randomch()  # After deleting the ghost,
            wl = randompoz()    # it randomize again(character and starting x pos) and
            char = 6            # assign the starting y pos.
            if score >= 45:  # This is where the game switch to the second list with special characters. (Level4)
                buddy = randomch_with_specials()
            with open("littleharry2.txt") as f:
                content = f.readlines()
                for i, row in enumerate(content):
                    win.addstr(curses.LINES-17+i, 1, row)
                    win.border(0)
                    key_pressed = False  # Assigned False to call littleharry.txt.
        if score == 15:  # Level 2
            level = 2
            level = str(level)
            string = " LEVEL: "
            win.addstr(curses.LINES - 2, (curses.COLS - len(string)) // 2, "LEVEL: " + level, curses.A_BOLD)
            level = int(level)
        elif score == 30:  # Level 3
            level = 3
            level = str(level)
            string = " LEVEL: "
            win.addstr(curses.LINES - 2, (curses.COLS - len(string)) // 2, "LEVEL: " + level, curses.A_BOLD)
            level = int(level)
        elif score == 45:  # Level 4
            level = 4
            level = str(level)
            string = " LEVEL: "
            win.addstr(curses.LINES - 2, (curses.COLS - len(string)) // 2, "LEVEL: " + level, curses.A_BOLD)
            level = int(level)


def get_started():  # Clear the window, project title and call the main function.
    win.clear()
    win.border(0)
    title = "<<<Harry Popper>>>"
    win.addstr(1, (curses.COLS - len(title)) // 2, title, curses.A_BOLD)
    main()


def next_screen():  # It controls menu keys.
    while True:
        event = win.getch()
        if event == ord("q"):
            break
        elif event == ord("R"):
            win.clear()
            main_screen()
        elif event == ord("p"):
            get_started()


main_screen()
next_screen()


curses.endwin()
