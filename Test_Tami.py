#!/usr/bin/env python3

import curses
# subprocess allows commands to pass through a temp terminal. Possible remove if I import scapy as if I end up running the commands it should be from the imported folder
import subprocess
import scapy.all as scapy

TITLE = "Network Sniffer"
'''This is a scapy intergrated function that will allow the user to select and run a command from scapy'''

# I need to find how to call a scapy function from MENU_ITEMS
MENU_ITEMS = [
    ("Run Scapy", ["sudo", "scapy", "-H"]), # This will need to be removed or updated as right now it shows that scapy works
    # this is an test function, or what to add if I can link scapy to project
    ("sniff", ["scapy.sniff()"]),
    ("Extra, This can be changed, I can add an extra function", [None]),
]

def draw(stdscr): # standard screen which is the main window for curses
    stdscr.clear() # clears the terminal
    height, width = stdscr.getmaxyx() # gets the size, width and height

    stdscr.addstr(1, 2, TITLE, curses.A_BOLD)

    for i, (label, _) in enumerate(MENU_ITEMS):
        """Displays the Menu options"""
        item_text = "[{}] {}".format(i + 1, label)
        stdscr.addstr(i + 3, 2, item_text)

    stdscr.addstr(height - 10, 1, "input text here")
    stdscr.refresh() # update terminal


def run_command(stdscr, command):
    """This will run an external command while temp exit out of first screen"""
    curses.def_prog_mode()
    curses.endwin() # temp exit screen
    try:
        subprocess.run(command)
    finally: # This will restore the option menu
        curses.reset_prog_mode()
        stdscr.clear()
        stdscr.refresh()


def main(stdscr):

    while True:
        draw(stdscr)
        key = stdscr.getch() # wait for user input

        if ord("1") <= key <= ord("2"):
            selection_inx = key - ord("1") # Convert ASCII keycode
            if selection_inx < len(MENU_ITEMS):
                command = MENU_ITEMS[selection_inx][1]

                if command is None:
                    break

                run_command(stdscr, command)

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass