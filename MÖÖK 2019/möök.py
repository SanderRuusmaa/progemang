import cmd
import sys
import os
import textwrap
import time
import random
import subprocess
from easygui import *
import easygui #'pip3 install easygui' Thonny System shelli, muidu viskab errorit


### Mängija setup ###
class player_inf():
    def __init__(self):
        self.mängu_staatus = False
        self.nimi = ""
        self.hp = 0
player = player_inf()


#### Tiitellehe valikud ####
def tiitellehe_valikud():
    valik = input(">>> ")
    if valik.lower() == "mängi":
        start_game()
    elif valik.lower() == "abi":
        help_menu()
    elif valik.lower() == "quit":
        sys.exit()
    while valik.lower() not in ["mängi", "abi", "quit"]:
        print("Palun sisestage tuntud käsk!")
        tiitellehe_valikd()
        
        
#### Tiitelleht ####
def tiitelleht():
    os.system("clear")
    print("===========================")
    print("=Tere tulemast mängu MÖÖK!=")
    print("===========================")
    print("         + Mängi +         ")
    print("         ? Abi   ?         ")
    print("         - Quit  -         ")
    print("     -- rushkin 2019 --    ")
    print("===========================")


#### Mängu asukoha saamine ja logo kutsumine ####
def mängu_asukoht():
    global path
    msgbox(msg="Enne mängu käivitumist, palun valige folder, kus asub mäng!", title="Kiire setup", ok_button="OK")
    path = easygui.diropenbox()
    if path == None:
        msgbox(msg="Katkestasite tegevuse, mäng ei käivitu", title="Error", ok_button="OK")
    return path
asukoht = mängu_asukoht()

while True:
    try:
        subprocess.call([r""+asukoht+"\logo.bat"]) #logo kutsumine, kui valiti õige folder
        break
    except:
        if path == None: #kui folderi pathi valimisel paned "cancel"
            break
        else: #kui valiti vale folder
            msgbox(msg= "Midagi läks valesti, te ei valinud õiget folderit...\n\nProovime uuesti.", title="Error", ok_button="OK")
            mängu_asukoht()

def setup_game():
    os.system("clear")
    küsimus1 = "Tere, mis teie nimi on?\n"
    for el in küsimus1:
        sys.stdout.write(el)
        sys.stdout.flush()
        time.sleep(0.05)
    

setup_game()
    