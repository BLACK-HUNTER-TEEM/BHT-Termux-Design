import os
import sys
import time

def des():
    os.system("python2 BHT-Termux-Design.py")


def logo():
    os.system("python logo.py")

def clr():
    os.system("clear")

def fb():
    os.system("python fb.py")

def exit():
    sys.exit()


#main....

#col value

red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

#yellow = '\33[93m'

green = '\033[1;32m'


#ok
#main

clr()
logo()
print(yellow+"\n\n\t\t[🔥] Selecte Your Options [🔥]")
os.system("lolcat print.txt")
#print(blue+"\n\n\t\t[1] Setup Termux Install All Command Properly\n\t\t[2] FacebooK\n\t\t[3] [!] ExiT [!]")
opt=int(input(yellow+"\n\n\t\t[$] Enter Your Option : "))
if opt==1:
   os.system("python set.py")
elif opt==2:
     des()
elif opt==3:
     fb()
elif opt==4:
     exit()
else:
	print("\n\n\t\tWRONG Option Choices")
	exit()
