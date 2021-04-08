# cpnotes.py - This script saves you time by auto-pasting plaintext from your clipboard onto a txt file formatted
# into bulleted notes

import os
import pyperclip # pip install pyperclip
import time
from pathlib import Path


def start():
    print("Initializing.....")
    time.sleep(2.5)
    print("Done!\n")
    print("Cleaning System Clipboard.....")
    pyperclip.copy(False)
    time.sleep(1.5)
    print("Done!\n")

# This function extracts the name of the user account - for debugging
def UserDir():
   
    home = str(Path.home())
    name = home.split('\\')[-1]

    return name


def header():
    print("\n")
    print("Copied Text will appear below".center(50, "="))
    print("\n")


start()
fname = input("Enter FileName you want to create: ")
print("Saving File to Desktop...")
time.sleep(2)
print("\nProgram Ready!..\n")
header()

while True:
    try:
        
        pn = open(f"{os.path.expanduser('~')}\\Desktop\\{fname}.txt", 'a')
        if pyperclip.paste() == 'False':
            time.sleep(1)
            continue
        else:
            print(pyperclip.paste())
            y = ""
            for i in pyperclip.paste():
                x = i.strip('\n')
                y += x
            pn.write(f"<$>: {y}\n\n")
            pn.close()
            pyperclip.copy(False)
    except KeyboardInterrupt:
        print("\nProgram Paused...")
        a = input("Create New File or Resume Program or Exit? n/r/e: ")
        if a == 'n':
            fname = input("\nEnter FileName you want to create: ")
            pyperclip.copy(False)
            header()
            continue
        elif a == 'r':
            pyperclip.copy(False)
            header()
            continue
        else:
            pyperclip.copy(False)
            break
