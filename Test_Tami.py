#!/usr/bin/env python3

import curses
import subprocess

TITLE = "Network Sniffer"

MENU_ITEMS = [
    ("Scapy", ["sudo", "scapy", "-H"]),
    ("Extra, This can be changed", [None]),
]

def draw(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    stdscr.addstr(1, 2, TITLE, curses.A_BOLD)

    for i, (label, _) in enumerate(MENU_ITEMS):
        item_text = "[{}] {}".format(i + 1, label)
        stdscr.addstr(i + 3, 2, item_text)

    stdscr.addstr(height - 2, 2, "input text here")
    stdscr.refresh()


def main(stdscr):

    while True:
        draw(stdscr)
        key = stdscr.getch()

        if ord("1") <= key <= ord("2"):
            selection_inx = key - ord("1")
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