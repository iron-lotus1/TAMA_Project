#!/usr/bin/env python3

import curses
import subprocess
import scapy.all as scapy

TITLE = "Network Sniffer"

MENU_ITEMS = [
    ("Scapy", ["sudo", "scapy", "-H"]),
    # this is an test function, or what to add if I can link scapy to project
    # ("sniff", "p=sniff(count=50)"),
    ("Extra, This can be changed, I can add an extra function", [None]),
]

def draw(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    stdscr.addstr(1, 2, TITLE, curses.A_BOLD)

    for i, (label, _) in enumerate(MENU_ITEMS):
        item_text = "[{}] {}".format(i + 1, label)
        stdscr.addstr(i + 3, 2, item_text)

    stdscr.addstr(height - 10, 1, "input text here")
    stdscr.refresh()


def run_command(stdscr, command):
    curses.def_prog_mode()
    curses.endwin()
    try:
        subprocess.run(command)
    finally:
        curses.reset_prog_mode()
        stdscr.clear()
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