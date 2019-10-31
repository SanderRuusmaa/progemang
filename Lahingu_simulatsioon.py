from time import sleep
from random import *
heroHP = 100
kollHP = 100

#intro
print("Kalevipoeg flaneerib Kesk-Eesti niidul")
sleep(1.5)
print("Selja tagant on kuulda jubedaid samme")
sleep(1.5)
print("See on koll!")
sleep(1.5)
print("Kalevipoeg haarab vammuse alt soome sepa mõõga")
sleep(1.5)
print("Koll ragistab hambaid ja ragistab nukke")
sleep(1.5)
print("Algab vägev lahing")
for i in range(0, 3):
    sleep(0.8)
    print(".")

#lahing
while heroHP > 0 and kollHP > 0:
    dmg1 = randint(0, 5)
    dmg2 = randint(0, 5)
    heroHP -= dmg1
    kollHP -= dmg2
    print("Kalevipoeg suskas mõõgaga ning koll kaotas " + str(dmg1) + " elupunkti.\n" + "Kollil on " + str(kollHP) + " elupunkti.\n") 
    print("Koll andis Kalevipojale rusikahoobi ning Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(heroHP) + " elupunkti.\n\n")

#lõpp
if heroHP <= 0:
    print("Vapper Kalevipoeg kukub väsinult põlvili maha...")
    sleep(3)
    print("Koll haarab Kalevipoja peast kinni ning rebib selle otsast")
    sleep(3)
    print("Kalevipoeg sai lüüa.")
elif kollHP <= 0:
    print("Koll kukub korisedes sellili...")
    sleep(3)
    print("Kalevipoeg võtab mõõgast kahe käega kinni ning lööb selle lapiti kollile pähe kinni, purustades ta kolju ja muutes aju kördiks")
    sleep(3)
    print("Koll sai lüüa.")
    
    