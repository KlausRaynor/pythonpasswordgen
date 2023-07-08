import random
from tkinter_gui import *
import tkinter_gui as gui
import generate_passwords as gen


# function to increase label value by 1
def increase_num():
    value = int(gui.lbl_pnum["text"])
    if value >= 100:
        return
    else:
        gui.lbl_pnum["text"] = f"{value + 1}"


def increase_len():
    value = int(gui.lbl_plen["text"])
    if value >= 25:
        gui.lbl_plen["text"] = 25
    else:
        gui.lbl_plen["text"] = f"{value + 1}"


# function to decrease label value by 1
def decrease_num():
    value = int(gui.lbl_pnum["text"])
    gui.lbl_pnum["text"] = f"{value - 1}"


def decrease_len():
    value = int(gui.lbl_plen["text"])
    if value <= 6:
        gui.lbl_plen["text"] = 6
    else:
        gui.lbl_plen["text"] = f"{value - 1}"


def generate():
    print("Generate button clicked!")
    number = int(gui.lbl_pnum["text"]) - 1
    length = int(gui.lbl_plen["text"])
    chars = gen.chars
    display = gui.display_passwords
    for pwd in range(number + 1):
        passwords = ''
        for c in range(length):
            passwords += random.choice(chars)
        display.insert(float(number), f"{passwords}\n")
