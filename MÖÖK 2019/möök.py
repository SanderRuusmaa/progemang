import cmd
import sys
import os
import textwrap
import time
import random
import subprocess


### Mängija setup ###
class player_inf():
    def __init__(self):
        self.mängu_staatus = False
        self.nimi = ""
        self.hp = 0
player = player_inf()

#### Tiitelleht ####
def tiitelleht():
    os.system("clear")
    print("===========================")
    print("=Tere tulemast mängu MÖÖK!=")
    print("===========================")
    print("         + Mängi +         ")
    print("         ? Abi   ?         ")
    print("         - Quit  -         ")
    print("===========================")
    print("     -- rushkin 2019 --    ")
    print("===========================")


#### Tiitellehe valikud ####
def tiitellehe_valikud():
    valik = input(">>> ")
    if valik.lower() == "mängi":
        os.system("clear")
        start_game()
    elif valik.lower() == "abi":
        os.system("clear")
        help_menu()
    elif valik.lower() == "quit":
        os.system("clear")
        time.sleep(0.5)
        for el in "Nägemiseni! :)":
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
        os.system("clear")
        sys.exit()
    while valik.lower() not in ["mängi", "abi", "quit"]:
        print("Palun sisestage tuntud käsk!")
        tiitellehe_valikd()
        
#### Help Menu ####
def help_menu():
    print("===========================")
    print("=          ABI            =")
    print("===========================")
    print("Võitlused:                 ")
    print("Navigeerimine:             ")
    print("                           ")
    print("kirjuta 'tagasi', et naasta")
    print("tagasi peamenüüsse.        ")
    print("===========================")
    sys.stdout.flush()
    
    käsk = input(">>> ")
    
    if käsk.lower() == "tagasi":
        tiitelleht()
        tiitellehe_valikud()
    else:
        for el in "Tundmatu käsk, proovime uuesti...":
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.05)
        print("\n")
        os.system("clear")
        help_menu()

def setup_game():
    os.system("clear")
    küsimus1 = "Tere, mis teie nimi on?\n"
    for el in küsimus1:
        sys.stdout.write(el)
        sys.stdout.flush()
        time.sleep(0.05)

### LOGO DISPLAY ###
def display_the_logo():
    os.system("clear")
    os.system("cat logo.txt")
    ärinimi = "Game by Rushkin"
    time.sleep(1)
    sys.stdout.write("          ")
    for el in ärinimi:
        sys.stdout.write(el)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\n               ")
    aasta = "MMXIX"
    for el in aasta:
        sys.stdout.write(el)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(5)
    
### Mängu intro + menüü ###
display_the_logo()

while player.mängu_staatus == False:
    tiitelleht()
    tiitellehe_valikud()