from random import randint
from time import sleep
import sys
import time

class player_inf():
    def __init__(self):
        self.mängu_staatus = False
        self.nimi = ""
        self.hp = 100
player = player_inf()

class koll_inf():
    def __init__(self):
        self.nimi = "Koll" 
        self.nimiOm = "Kolli"
        self.NimiOs = "Kolli"
        self.hp = 100
        self.dmg = 10

class mõõk_inf():
    dmg = 5
    miss = 10 # 10% võimalus, et rünnak ei lähe üldse läbi
    crit = 20 # Võimalus teha topeltdamage
    supercrit = 1 #Võimalus teha kolmekordselt damage'it



koll = koll_inf()
relv = mõõk_inf()

def fight(koll): 
    while koll.hp > 0 and player.hp > 0:
        #Siin seame parameetrid uue tsükli jaoks õigetele väärtusetele
        deftxt = True #kas lõpus prinditakse default teksti
        dmg1 = 0  

        #valige relv
        dmg_katse = 1000
        while not 1<=dmg_katse<=relv.dmg:
            try:
                dmg_katse = int(input("\nSisestage katsetatav löögi tugevus vahemikus 1..." + str(relv.dmg) + ": "))
            except:
                pass

        print("\n")
        dmg1 = 0
        if dmg_katse <= randint(0,relv.dmg):
            if randint(1,100)<=relv.miss:
                print("Tõeline ebaõnn! Kalevipoja relv takerdus mättasse!\n" +koll.nimiOm+ "l on ikka " + str(koll.hp) + "elupunkti.")
                deftxt = False #et default prinditavat teksti muuta
            else:
                param = randint(1,100)
                if param <= 20 and param > 1:
                    dmg1 = dmg_katse*2
                    print("Erakordselt hästi sihitud löök tegi " + koll.nimiOm + "le kahekordselt viga!\n" + koll.nimiOm + "l on nüüd "+ str(koll.hp-dmg1) + " elupunkti.")
                    deftxt = False
                elif param == 1:
                    dmg1 = dmg_katse*3
                    print("Vapustav! Kalevipoeg suskas " + koll.nimiOs + " otse silma, tehes kolmekordselt viga!\n" + koll.nimiOm + "l on nüüd "+ str(koll.hp-dmg1) + " elupunkti.")
                    deftxt = False
                else:
                    dmg1 = dmg_katse
                    
        else:
            #Siia panna erinevat read vastavalt sisestatud dmg_katse väärtusele
            print(koll.nimi + " kargles mängleva kergusega nii tugeva löögi eest kõrvale.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 

        dmg2 = randint(0, koll.dmg) #kolli tehtud dmg
        player.hp -= dmg2
        koll.hp -= dmg1

        
        sleep(0.5)
        if deftxt == True and dmg1 != 0:
            print("Kalevipoeg suskas mõõgaga ning " +  koll.nimi + " kaotas " + str(dmg1) + " elupunkti.\n" + koll.nimiOm +"l on " + str(koll.hp) + " elupunkti.")
        #elif deftxt == True and dmg1 == 0:
        #    print(koll.nimi + " pareeris Kalevipoja kohmaka löögi.\n" + koll.nimiOm +"l on " + str(koll.hp) + " elupunkti.\n")
        if dmg2 != 0:
            print("\n" + koll.nimi + " andis Kalevipojale rusikahoobi ning Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
        else:
            print("\nKalevipojal õnnestus "+ koll.nimiOm + " rusikahoobi eest kõrvale põigelda!\n Kalevipojal on endiselt " + str(player.hp) + " elupunkti.")

    #Fighti lõpp
    if 2 <= 0:
        lõpp1 = "Vapper Kalevipoeg kukub väsinult põlvili maha"
        for el in lõpp1:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.1)
        for el in [".",".","."]:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.8)
        print("\n")
        lõpp2 = koll.nimi + " haarab Kalevipoja peast kinni ning rebib selle otsast"
        for el in lõpp2:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.1)
        for el in [".",".","."]:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.8)
        print("\n")
        lõpp3 = "Kalevipoeg sai lüüa."
        for el in lõpp3:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.1)
    elif 0 <= 0:
        lõpp1_1 = koll.nimi + " kukub korisedes sellili"
        for el in lõpp1_1:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.1)
        for el in [".",".","."]:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.8)
        print("\n")
        lõpp2_1 = "Kalevipoeg võtab mõõgast kahe käega kinni ning lööb selle lapiti " + koll.nimiOm + "le pähe kinni, purustades ta kolju ja muutes aju kördiks."
        for el in lõpp2_1:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.05)
        for el in [".",".","."]:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.8)
        print("\n")
        lõpp3_1 = koll.nimi + " sai lüüa."
        for el in lõpp3_1:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.1)


fight(koll)