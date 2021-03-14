# !/usr/bin/env python

# Pomodoro timer
# git: apaaris

import os
import time
from tqdm import tqdm 
from colorama import Fore

# Importa impostazioni
_length = [25,5,15]
_colors = [Fore.RED, Fore.GREEN, Fore.BLUE]
icon = "🍅 "
_modes = ["Focus","Short Break", "Long Break"]

# Setup
def setup():
    for i in range(3):
        print(_colors[i])
        _length[i] = int(input("Enter " + _modes[i] + " length [min] (default: "
                + str(_length[i])  + "): "))
# Ascii art
def display(i,cnt):
    print(_colors[i])
    print(
    "      ____                            _        "+ cnt +" \n"
    "     / __ \____  ____ ___  ____  ____/ /___  _________   \n"
    "    / /_/ / __ \/ __ `__ \/ __ \/ __  / __ \/ ___/ __ \  \n"
    "   / ____/ /_/ / / / / / / /_/ / /_/ / /_/ / /  / /_/ /  \n"
    "  /_/    \____/_/ /_/ /_/\____/\__,_/\____/_/   \____/   \n" 
    "                                                         \n" +
    "  -> " + str(_modes[i]) +" <-" + (33-len(str(_modes[i])))*" "+ "git: apaaris    \n")

# Continue
def resume():
    print("\n")
    key = input("Press any key to continue, enter A to quit: ")
    os.system('clear')
    if (key == 'A'):
        return True

# Barra
def bar(j,cnt):
    display(j,cnt)
    for i in tqdm(range(_length[j])):
        time.sleep(1)
# Loop
#  1 2 1 2 1 2 1 3
def loop():
    done = False
    while(done == False):
        cnt = "|"
        os.system('clear')
        #for 3x(1,2)+1+3
        for j in range(3):
            for i in range(2):
                bar(i,cnt)
                if resume() == True:
                    done = True
                    break
            cnt += "|"
        bar(0,cnt)
        if resume() == True:
            done = True
            break
        bar(2,cnt)
        if resume() == True:
            done = True
            break
# Main
def main():
    setup()
    loop()
    print("Thanks for using pomodoro. Good luck for your exams")

# RUUN
main()
