import cmd
import sys
import os
import textwrap
import time
from time import sleep
import random
from random import randint
import subprocess

### teksti animeerimine ###
def animeeri(tekst):
    for el in tekst:
        sys.stdout.write(el)
        sys.stdout.flush()
        time.sleep(0.05)

### Mängija setup ###
class player_inf():
    def __init__(self):
        self.mängu_staatus = False
        self.nimi = ""
        self.hp = 30
        self.gold = 5

player = player_inf()

#===================================================================== RELVAD JA KOLLID ==================================================
### KOLLID ###

class koll_inf():
    def __init__(self):
        self.nimi = "Koll" 
        self.nimiOm = "Kolli"
        self.nimiOs = "Kolli"
        self.hp = 100
        self.dmg = 10
        self.weakness = "lõikav"
        self.dodge = 20
        self.auhind = 50

class hiidämblik_inf():
    def __init__(self):
        self.nimi = "Hiidämblik" 
        self.nimiOm = "Hiidämbliku"
        self.nimiOs = "Hiidämblikku"
        self.hp = 20
        self.dmg = 4
        self.weakness = "purustav"
        self.dodge = 15
        self.auhind = 5

class hiigelämblik_inf():
    def __init__(self):
        self.nimi = "Hiigelämblik" 
        self.nimiOm = "Hiigelämbliku"
        self.nimiOs = "Hiigelämblikku"
        self.hp = 60
        self.dmg = 8
        self.weakness = "lõikav"
        self.dodge = 4
        self.auhind = 25

class harpüia_inf():
    def __init__(self):
        self.nimi = "Harpüia" 
        self.nimiOm = "Harpüia"
        self.nimiOs = "Harpüiat"
        self.hp = 15
        self.dmg = 5
        self.weakness = "kaugrünnak"
        self.dodge = 35
        self.auhind = 5

class zombi_inf():
    def __init__(self):
        self.nimi = "Zombi" 
        self.nimiOm = "Zombi"
        self.nimiOs = "Zombit"
        self.hp = 10
        self.dmg = 3
        self.weakness = "suskav"
        self.dodge = 3
        self.auhind = 2

class draakon_inf():
    def __init__(self):
        self.nimi = "Draakon" 
        self.nimiOm = "Draakoni"
        self.nimiOs = "Draakonit"
        self.hp = 250
        self.dmg = 25
        self.weakness = "lõikav", "kaugrünnak"
        self.dodge = 5
        self.auhind = 200

class vampiir_inf():
    def __init__(self):
        self.nimi = "Vampiir" 
        self.nimiOm = "Vampiiri"
        self.nimiOs = "Vampiiri"
        self.hp = 30
        self.dmg = 5
        self.weakness = "purustav"
        self.dodge = 25
        self.auhind = 10

class rott_inf():
    def __init__(self):
        self.nimi = "Rott" 
        self.nimiOm = "Roti"
        self.nimiOs = "Rotti"
        self.hp = 5
        self.dmg = 2
        self.weakness = "purustav"
        self.dodge = 25
        self.auhind = 1
        
### RELVAD ###
class mõõk_inf():
    def __init__(self):
        self.Nimi = "Mõõk"
        self.nimi = "mõõk"
        self.NimiOm = "Mõõga"
        self.nimiOm = "mõõga"
        self.NimiOs = "Mõõka"
        self.nimiOs = "mõõka"
        self.min_dmg = 2
        self.dmg = 5
        self.miss = 10 # 10% võimalus, et rünnak ei lähe üldse läbi
        self.crit = 20 # Võimalus teha topeltdamage
        self.supercrit = 1 #Võimalus teha kolmekordselt damage'it
        self.type = "lõikav"

class nui_inf():
    def __init__(self):
        self.Nimi = "Nui"
        self.nimi = "nui"
        self.NimiOm = "Nuia"
        self.nimiOm = "nuia"
        self.NimiOs = "Nuia"
        self.nimiOs = "nuia"
        self.min_dmg = 3
        self.dmg = 8
        self.miss = 10
        self.crit = 5
        self.supercrit = 1
        self.type = "purustav"

class vibu_inf():
    def __init__(self):
        self.Nimi = "Vibu"
        self.nimi = "vibu"
        self.NimiOm = "Vibu"
        self.nimiOm = "vibu"
        self.NimiOs = "Vibu"
        self.nimiOs = "vibu"
        self.min_dmg = 2
        self.dmg = 4
        self.miss = 30
        self.crit = 10
        self.supercrit = 5
        self.type = "kaugrünnak"

class nuga_inf():
    def __init__(self):
        self.Nimi = "Nuga"
        self.nimi = "nuga"
        self.NimiOm = "Noa"
        self.nimiOm = "noa"
        self.NimiOs = "Nuga"
        self.nimiOs = "nuga"
        self.min_dmg = 1
        self.dmg = 3
        self.miss = 5
        self.crit = 50
        self.supercrit = 10
        self.type = "suskav"

class vikat_inf():
    def __init__(self):
        self.Nimi = "Vikat"
        self.nimi = "vikat"
        self.NimiOm = "Vikati"
        self.nimiOm = "vikati"
        self.NimiOs = "Vikatit"
        self.nimiOs = "vikatit"
        self.min_dmg = 1
        self.dmg = 5
        self.miss = 20
        self.crit = 5
        self.supercrit = 1
        self.type = "kaugrünnak", "lõikav"

class sõjahaamer_inf():
    def __init__(self):
        self.Nimi = "Sõjahaamer"
        self.nimi = "sõjahaamer"
        self.NimiOm = "Sõjahaamri"
        self.nimiOm = "sõjahaamri"
        self.NimiOs = "Sõjahaamrit"
        self.nimiOs = "sõjahaamrit"
        self.min_dmg = 2
        self.dmg = 10
        self.miss = 20
        self.crit = 12.5
        self.supercrit = 1
        self.type = "purustav"

class amb_inf():
    def __init__(self):
        self.Nimi = "Amb"
        self.nimi = "amb"
        self.NimiOm = "Ammu"
        self.nimiOm = "ammu"
        self.NimiOs = "Ambu"
        self.nimiOs = "ambu"
        self.min_dmg = 3
        self.dmg = 15
        self.miss = 30
        self.crit = 5
        self.supercrit = 2
        self.type = "kaugrünnak"

class piits_inf():
    def __init__(self):
        self.Nimi = "Piits"
        self.nimi = "piits"
        self.NimiOm = "Piitsa"
        self.nimiOm = "piitsa"
        self.NimiOs = "Piitsa"
        self.nimiOs = "piitsa"
        self.min_dmg = 1
        self.dmg = 4
        self.miss = 2
        self.crit = 3
        self.supercrit = 1
        self.type = "lõikav"

class oda_inf():
    def __init__(self):
        self.Nimi = "Oda"
        self.nimi = "oda"
        self.NimiOm = "Oda"
        self.nimiOm = "oda"
        self.NimiOs = "Oda"
        self.nimiOs = "oda"
        self.min_dmg = 3
        self.dmg = 10
        self.miss = 15
        self.crit = 5
        self.supercrit = 1
        self.type = "lõikav"

class viskeoda_inf():
    def __init__(self):
        self.Nimi = "Viskeoda"
        self.nimi = "viskeoda"
        self.NimiOm = "Viskeoda"
        self.nimiOm = "viskeoda"
        self.NimiOs = "Viskeoda"
        self.nimiOs = "viskeoda"
        self.min_dmg = 4
        self.dmg = 6
        self.miss = 40
        self.crit = 5
        self.supercrit = 1
        self.type = "kaugrünnak"

relv = nui_inf()
koll = vampiir_inf()
#==============================================================POOD=================================================================
### Poe sisu ###
relvad = {"mõõk":[10,False], #vastavalt (hind, omamine)
        "nui": [10,False],
        "vibu": [10,False],
        "nuga": [10,False],
        "vikat": [10,False],
        "piits": [10,False],
        "sõjahaamer": [20,False],
        "oda": [20,False],
        "viskeoda": [30,False],
        "amb": [50,False]}

rüüd = {"nahkrüü": [10,False],
         "rõngassärk": [20,False],
         "raudrüü": [35,False],
         "meisterlik raudrüü": [50,False],
         "haldjarauast rüü": [80,False]}

võlujoogid = {"elujook I": [3,0], #Vastavalt hind, kogus
              "elujook II": [8,0],
              "elujook III": [18,0],
              "ründejook I": [3,0],
              "ründejook II": [8,0],
              "ründejook III": [18,0],
              "surematuse jook": [12,0],
              "tulekindluse jook": [12,0],
              "relvamürk": [15,0]}

oskused = {"Oskus lüüa üks kord rohkem korraga": [30,False],
           "Oskus lüüa üks kord rohkem korraga": [50,False],
           "Oskus lasta üks kord rohkem korraga": [30,False],
           "Oskus lasta üks kord rohkem korraga": [50,False],
           "Oskus võitluse käigus relva vahetada": [15,False],
           "Oskus juua võlujooki käiku raiskamata": [15,False],
           "Oskus alati võitlusest põgeneda": [40,False],
           "Oskus õnnetuid lööke ja laske vältida": [40,False]}

########## Poe funktsioon ############

def shop():
    print("Tere! ", end="")
    while True:
        valik = input("Mida soovite osta? Kui relvi, siis kirjutage \"relvad\", kui rüüsid, kirjutage \"rüüd\", kui võlujooke, kirjutage \"võlujoogid\", kui oskuseid, kirjutage \"oskused\", kui soovite poest lahkuda, kirjutage \"lahku\": ")
        sleep(0.5)
        if valik == "relvad":
            animeeri("\nAh et soovite meie kvaliteetseid relvi vaadata! Siin on meie valik:")
            for k in relvad:
                print(k + ": " + str(relvad[k][0]))
            valik2 = input("Sisestage, mida soovite osta või \"tagasi\", kui soovite tagasi pöörduda: ")
            if valik2 == "tagasi":
                pass
            elif valik2 in relvad:
                kas_osta = input("Kas soovite osta " + valik2 + "? Kirjutage \"jah\" või \"ei\": ")
                parameeter = False
                if kas_osta == "jah":
                    parameeter = True
                elif kas_osta == "ei":
                    parameeter = False
                sleep(0.5)
                if parameeter == True and player.gold >= relvad[valik2][0] and relvad[valik2][1] == False:
                    relvad[valik2][1] = True
                    player.gold -= relvad[valik2][0]
                    print("Teil on nüüd relv: " + valik2 + ".\n")
                    sleep(0.5)
                elif parameeter == True and player.gold < relvad[valik2][0] and relvad[valik2][1] == False:
                    print("Teil kahjuks pole piisavalt kulda selle ostu sooritamiseks.\n")
                    sleep(0.5)
                elif relvad[valik2][1] == True:
                    print("Teil juba on see relv!\n")
                    sleep(0.5)
            else:
                pass
            
        elif valik == "rüüd":
            animeeri("\nMa näen, et teid huvitab meie rüükollektsioon! Heitke pilk peale ja laduge raha lauale! Siin on valikud:")
            for k in rüüd:
                print(k + ": " + str(rüüd[k][0]))
            valik2 = input("Sisestage, mida soovite osta või \"tagasi\", kui soovite tagasi pöörduda: ")
            if valik2 == "tagasi":
                pass
            elif valik2 in rüüd:
                kas_osta = input("Kas soovite osta " + valik2 + "? Kirjutage \"jah\" või \"ei\": ")
                parameeter = False
                if kas_osta == "jah":
                    parameeter = True
                elif kas_osta == "ei":
                    parameeter = False
                sleep(0.5)
                if parameeter == True and player.gold >= rüüd[valik2][0] and rüüd[valik2][1] == False:
                    rüüd[valik2][1] = True
                    player.gold -= rüüd[valik2][0]
                    print("Teil on nüüd rüü: " + valik2 + ".\n")
                    sleep(0.5)
                elif parameeter == True and player.gold < rüüd[valik2][0] and rüüd[valik2][1] == False:
                    print("Teil kahjuks pole piisavalt kulda selle ostu sooritamiseks.\n")
                    sleep(0.5)
                elif rüüd[valik2][1] == True:
                    print("Teil juba on see rüü!\n")
                    sleep(0.5)
            else:                
                pass

        elif valik == "võlujoogid":
            animeeri("\nNäen, et imetlete meie võlujooke. Need kõik võivad olla teie, kui te vaid maksate! Siin on meie valik:")
            for k in võlujoogid:
                print(k + ": " + str(võlujoogid[k][0]))
            valik2 = input("Sisestage, mida soovite osta või \"tagasi\", kui soovite tagasi pöörduda: ")
            if valik2 == "tagasi":
                pass
            elif valik2 in võlujoogid:
                kas_osta = input("Kas soovite osta " + valik2 + "? Kirjutage \"jah\" või \"ei\": ")
                parameeter = False
                if kas_osta == "jah":
                    parameeter = True
                elif kas_osta == "ei":
                    parameeter = False
                sleep(0.5)
                if parameeter == True and player.gold >= võlujoogid[valik2][0]:
                    võlujoogid[valik2][1] += 1
                    player.gold -= võlujoogid[valik2][0]
                    print("Teil on seda võlujooki nüüd " + str(võlujoogid[valik2][1]) + ".\n")
                    sleep(0.5)
                elif parameeter == True and player.gold < võlujoogid[valik2][0]:
                    print("Teil pole piisavalt raha selle ostu sooritamiseks!\n")
                    sleep(0.5)
             
        elif valik == "oskused":
            animeeri("\nNäen, et uurite meie intensiivse treeningu kava. Paremaid võitlusoskuseid kui meiega ei saa te kuskil kuningriigis! Siin on meie programmid:")
            for k in oskused:
                print(k + ": " + str(oskused[k][0]))
            valik2 = input("Sisestage, mida soovite osta või \"tagasi\", kui soovite tagasi pöörduda: ")
            if valik2 == "tagasi":
                pass
            elif valik2 in rüüd:
                kas_osta = input("Kas soovite osta " + valik2 + "? Kirjutage \"jah\" või \"ei\": ")
                parameeter = False
                if kas_osta == "jah":
                    parameeter = True
                elif kas_osta == "ei":
                    parameeter = False
                sleep(0.5)
                if parameeter == True and player.gold >= oskused[valik2][0] and oskused[valik2][1] == False:
                    oskused[valik2][1] = True
                    player.gold -= oskused[valik2][0]
                    print("Teil on nüüd oskus: " + valik2 + ".\n")
                    sleep(0.5)
                elif parameeter == True and player.gold < oskused[valik2][0] and oskused[valik2][1] == False:
                    print("Teil kahjuks pole piisavalt kulda sellele treeningkavale registreerimiseks.\n")
                    sleep(0.5)
                elif oskused[valik2][1] == True:
                    print("Teil juba on see oskus!\n")
                    sleep(0.5)
                
        elif valik == "lahku":
            animeeri("Lahkusite poest.")
            break
        else:
            pass


###======================================================VÕITLUSE FUNKTSIOON===================================================
def fight(koll): 
    while koll.hp > 0 and player.hp > 0:
        #Siin seame parameetrid uue tsükli jaoks õigetele väärtusetele
        deftxt = True #kas lõpus prinditakse default teksti
        dmg1 = 0

        ######testimiseks###########
        relv = nui_inf()
        relvad["nui"][1] = True
        oskused["Oskus võitluse käigus relva vahetada"][1] = True
        ############################
        
        ##### valige relv ####
        animeeri("Sinu relvavalik: \n")
        weapons = []
        for weapon in relvad:
            if relvad[weapon][1] == True:
                weapons.append(weapon)
                print("-",weapon)
        if oskused["Oskus võitluse käigus relva vahetada"][1] == True:
            while True:
                valik = input("Valige relv: ")
                if valik in relvad:
                    if relvad[valik][1] == True:
                        if valik == "vibu":
                            relv = vibu_inf()
                            break
                        elif valik == "mõõk":
                            relv = mõõk_inf()
                            break
                        elif valik == "nui":
                            relv = nui_inf()
                            break
                        elif valik == "sõjahaamer":
                            relv = sõjahaamer_inf()
                            break
                        elif valik == "amb":
                            relv = amb_inf()
                            break
                        elif valik == "piits":
                            relv = piits_inf()
                            break
                        elif valik == "nuga":
                            relv = nuga_inf()
                            break
                        elif valik == "oda":
                            relv = oda_inf()
                            break
                        elif valik == "viskeoda":
                            relv = viskeoda_inf()
                            break
                    else:
                        print("Teil pole veel seda relva!")
                elif valik == "":
                    break
                else:
                    print("==Tundmatu sisend!==")
                    print("Siin on relvade nimekiri: " + str(relvad.keys()).strip("dict_keys(").strip(")") + "." + "\nKüll aga sina omad järgnevaid relvi: " + str(weapons))
            print("Teie relv on " + relv.nimi + ".")       
                    
        #### Löögitugevuse valimine ####            
        dmg_katse = 1000
        while not relv.min_dmg<=dmg_katse<=relv.dmg:
            try:
                dmg_katse = int(input("\nSisestage katsetatav löögi tugevus vahemikus " + str(relv.min_dmg) + "..." + str(relv.dmg) + ": "))
            except:
                pass

        print("\n")
        dmg1 = 0

        #### Missimine ####
        if dmg_katse <= randint(relv.min_dmg,relv.dmg):
            if randint(1,100)<=relv.miss:
                if type(relv) == mõõk_inf or type(relv) == vikat_inf:
                    print("Tõeline ebaõnn! Kalevipoja " + relv.nimi + " takerdus mättasse!\n" + koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                elif type(relv) == amb_inf or type(relv) == vibu_inf:
                    print("Oh ei! " + relv.NimiOm+ "nool lendas kaarega üle " + koll.nimiOm + " pea!\n" + koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                elif type(relv) == sõjahaamer_inf:
                    print("Oh õnnetust! "+ koll.nimiOm + " pea asemel purustas möödaläinud löök süütu kivirahnu.\n" + koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                elif type(relv) == nui_inf:
                    print("Tõeline ebaõnn! Ebamugava käepideme tõttu pudenes " + relv.nimi + " Kalevipojal käest!\n" + koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                elif type(relv) == nuga_inf or type(relv) == oda_inf:
                    print("Uskumatu ebaõnn! " + relv.Nimi + " tabas vaid paljast õhku.\n" +koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                elif type(relv) == piits_inf:
                    print("Oh ei! " + relv.Nimi + " takerdus enne " + koll.nimiOm + "ni jõudmist millessegi.\n" + koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                elif type(relv) == viskeoda_inf:
                    print("Oh ebaõnne! Kalevipoeg viskas " + relv.NimiOs + " vale ots ees ja see kukkus õnnetult enne " + koll.nimiOm + " lähedalegi jõudmist maha.\n"+ koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                deftxt = False #et default prinditavat teksti muuta
                
            else:
                param = randint(1,100)
                if param <= relv.crit and param > relv.supercrit:
                    dmg1 = dmg_katse*2
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf: 
                        print("Erakordselt hästi sihitud löök tegi " + koll.nimiOm + "le kahekordselt viga!\n" + koll.nimiOm + "l on nüüd "+ str(koll.hp-dmg1) + " elupunkti.")
                    elif type(relv) == oda_inf or type(relv) == nuga_inf:
                        print("Erakordselt hästi sihitud suse tegi " + koll.nimiOm + "le kahekordselt viga!\n" + koll.nimiOm + "l on nüüd "+ str(koll.hp-dmg1) + " elupunkti.")
                    elif type(relv) == piits_inf:
                        print("Erakordselt hästi sihitud piitsalöök tegi " + koll.nimiOm + "le kahekordselt viga!\n" + koll.nimiOm + "l on nüüd "+ str(koll.hp-dmg1) + " elupunkti.")
                    elif type(relv) == viskeoda_inf:
                        print("Erakordselt hästi sihitud vise tegi " + koll.nimiOm + "le kahekordselt viga!\n" + koll.nimiOm + "l on nüüd "+ str(koll.hp-dmg1) + " elupunkti.")
                    elif type(relv) == vibu_inf or type(relv) == amb_inf:
                        print("Erakordselt hästi sihitud lask tegi " + koll.nimiOm + "le kahekordselt viga!\n" + koll.nimiOm + "l on nüüd "+ str(koll.hp-dmg1) + " elupunkti.")                        
                    deftxt = False
                elif param <= relv.supercrit:
                    dmg1 = dmg_katse*3
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf: 
                        print("Vapustav! Suurepäraselt sihitud löök tegi " + koll.nimiOm + "le kolmekordselt viga!\n" + koll.nimiOm + "l on nüüd "+ str(koll.hp-dmg1) + " elupunkti.")
                    elif type(relv) == oda_inf or type(relv) == nuga_inf:
                        print("Vapustav! Kalevipoeg suskas " + koll.nimiOs + " otse silma, tehes kolmekordselt viga!\n" + koll.nimiOm + "l on nüüd "+ str(koll.hp-dmg1) + " elupunkti.")
                    elif type(relv) == piits_inf:
                        print("Vapustav! Perfektselt sihitud piitsalöök tegi " + koll.nimiOm + "le kolmekordselt viga!\n" + koll.nimiOm + "l on nüüd "+ str(koll.hp-dmg1) + " elupunkti.")
                    elif type(relv) == viskeoda_inf:
                        print("Vau! Suurepäraselt sihitud vise tegi " + koll.nimiOm + "le kolmekordselt viga!\n" + koll.nimiOm + "l on nüüd "+ str(koll.hp-dmg1) + " elupunkti.")
                    elif type(relv) == vibu_inf or type(relv) == amb_inf:
                        print("Uskumatu! Nool läks " + koll.nimiOm + "le otse silma ja tegi talle kolmekordselt viga!\n" + koll.nimiOm + "l on nüüd "+ str(koll.hp-dmg1) + " elupunkti.")                        
                    deftxt = False
                else:
                    dmg1 = dmg_katse
                    
        else:
            #Siia võib veel panna erinevad read vastavalt sisestatud dmg_katse väärtusele
            if randint(1,100) <= koll.dodge: 
                if type(koll) == koll_inf or type(koll) == vampiir_inf:
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == piits_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf:
                        print(koll.nimi + " kargles mängleva kergusega löögi eest kõrvale.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == oda_inf or type(relv) == nuga_inf:
                        print(koll.nimi + " tegi osava tagasihüppe, nii et suse tabas vaid õhku.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")
                    elif type(relv) == viskeoda_inf:
                        print(koll.nimiOm + "l õnnestus veel aegsasti lendava oda eest kõrvale hüpata.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")
                    elif type(relv) == vibu_inf or type(relv) == amb_inf:
                        print(koll.nimi + " nägi aegsasti noolt ja heade refleksidega suutis end selle teelt eest väänata.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")

                elif type(koll) == hiidämblik_inf or type(koll) == hiigelämblik_inf:
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf:
                        print(koll.nimiOm + " kaheksa kiiret jalga aitasid tal lööki vältida.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == oda_inf or type(relv) == nuga_inf:
                        print(koll.nimi + " kergitas oma kõhualust nii, et suse tabas vaid õhku.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")
                    elif type(relv) == viskeoda_inf:
                        print(koll.nimi + " tegi oma suuruse kohta uskumatult võimsa hüppe ja oda lendas kaugelt mööda.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")
                    elif type(relv) == vibu_inf or type(relv) == amb_inf:
                        print("Nool vihises " + koll.nimiOm + " paljude jalgade vahelt läbi ja ei tabanud märki.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")
                    elif type(relv) == piits_inf:
                        print(koll.nimi + " hüppas " + relv.nimiOm + " teelt eest. Võimas elukas...")

                elif type(koll) == harpüia_inf:
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf:
                        print(koll.nimi + " vilgas keha ei saanud pihta.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == oda_inf or type(relv) == nuga_inf:
                        print(koll.nimi + " lendles kergelt suske eest kõrvale.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == viskeoda_inf:
                        print(koll.nimiOm + "l oli napilt aega oda eest kõrvale liuelda.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == vibu_inf or type(relv) == amb_inf:
                        print("Nool ei tabanud "+ koll.nimiOs + ", sest tal õnnestus tiivad kokku tõmmata asukohta kiiresti muuta.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == piits_inf:                
                        print(koll.nimi + " sai piitsa teelt kõrvale, nii et kuulda oli vaid tühja vihinat.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 

                elif type(koll) == zombi_inf:
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == piits_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf:
                        print(koll.nimi + " tuias löögi eest kõrvale.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == oda_inf or type(relv) == nuga_inf:
                        print(koll.nimi + " tegi sammu tagasi, nii et suse tabas vaid õhku.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")
                    elif type(relv) == viskeoda_inf:
                        print(koll.nimiOm + "l õnnestus napilt lendava oda eest kõrvale astuda.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")
                    elif type(relv) == vibu_inf or type(relv) == amb_inf:
                        print(koll.nimi + " suutis noole teelt eest tuigerdada.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")

                elif type(koll) == rott_inf:
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == piits_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf:
                        print(koll.nimi + " sibas löögi eest kõrvale.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == oda_inf or type(relv) == nuga_inf:
                        print(koll.nimi + " sibas suske eest kõrvale.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == viskeoda_inf:
                        print(koll.nimi + " sibas oda eest kõrvale.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == vibu_inf or type(relv) == amb_inf:
                        print(koll.nimi + " sibas noole teelt.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 

                elif type(koll) == draakon_inf:
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf:
                        print(koll.nimiOm + " soomused peatasid löögi.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == oda_inf or type(relv) == nuga_inf:
                        print("Suse tabas vaid lohe soomuseid ja ei suutnud neid läbida.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == viskeoda_inf:
                        print(koll.nimiOm + " soomused peatasid oda jälgi jätmata.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == vibu_inf:
                        print("Lask tabas lohe vägevaid soomuseid ja " + koll.nimiOm + " soomustest ei pääseks ammunoolgi läbi...\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == amb_inf:
                        print("Lask tabas lohe vägevaid soomuseid ja " + koll.nimiOm + " nool põrkas mõlkigi jätmata lihtsalt tagasi.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == piits_inf:
                        print(relv.nimi + " tabas vaid " + koll.nimiOm + " soomuseid ja lohe ei pannud seda isegi tähele.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")
            else:
                dmg1 = relv.min_dmg

                
        dmg2 = randint(0, koll.dmg) #kolli tehtud dmg  
        player.hp -= dmg2
        koll.hp -= dmg1

        ##### Kalevipoja tehtud dmg-le vastav tekst#####
        sleep(0.5)
        if deftxt == True and dmg1 != 0:
            if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf:
                print("Kalevipoeg virutas " +  relv.nimiOm + "ga ning " +  koll.nimi + " kaotas " + str(dmg1) + " elupunkti.\n" + koll.nimiOm +"l on " + str(koll.hp) + " elupunkti.")
            elif type(relv) == oda_inf:
                print("Kalevipoeg suskas " +  relv.nimiOm + "ga ning " +  koll.nimi + " kaotas " + str(dmg1) + " elupunkti.\n" + koll.nimiOm +"l on " + str(koll.hp) + " elupunkti.")
            elif type(relv) == nuga_inf:
                print("Kalevipoeg pussitas " +  relv.nimiOm + "ga ning " +  koll.nimi + " kaotas " + str(dmg1) + " elupunkti.\n" + koll.nimiOm +"l on " + str(koll.hp) + " elupunkti.")
            elif type(relv) == viskeoda_inf:
                print("Kalevipoja visatud " + relv.nimi + " tabas märki ning " +  koll.nimi + " kaotas " + str(dmg1) + " elupunkti.\n" + koll.nimiOm +"l on " + str(koll.hp) + " elupunkti.")
            elif type(relv) == vibu_inf or type(relv) == amb_inf:
                print("Kalevipoja poolt lendu lastud nool tabas " + koll.nimiOs + " ning " +  koll.nimi + " kaotas " + str(dmg1) + " elupunkti.\n" + koll.nimiOm +"l on " + str(koll.hp) + " elupunkti.")
            elif type(relv) == piits_inf:
                print("Kalevipoja ogaline piits tabas " + koll.nimiOs + " ning " +  koll.nimi + " kaotas " + str(dmg1) + " elupunkti.\n" + koll.nimiOm +"l on " + str(koll.hp) + " elupunkti.")

        if koll.weakness == relv.type and dmg1 != 0:
            koll.hp -= 2
            print("\nHea relvavaliku tõttu kaotas " + koll.nimi + " veel 2 elupunkti. " + koll.nimiOm + "l on nüüd " + str(koll.hp) + " elupunkti.")

        ##### Kolli tehtud dmg-le vastav tekst #####
        if type(koll) == koll_inf:
            if dmg2 == 0:
                print("\nKalevipojal õnnestus "+ koll.nimiOm + " rusikahoobi eest kõrvale põigelda!\nKalevipojal on endiselt " + str(player.hp) + " elupunkti.")
            elif 0 < dmg2 <= 0.5*koll.dmg:
                print("\n" + koll.nimi + " andis Kalevipojale rusikahoobi ning Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            elif 0.5*koll.dmg < dmg2 <= 0.8*koll.dmg:
                print("\n" + koll.nimi + " virutas jalaga ning Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            else:
                print("\nOi ei! " + koll.nimi + " sai Kalevipoja oma vägevasse haardesse jagab järjestikku hoope! Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")

        elif type(koll) == hiidämblik_inf or type(koll) == hiigelämblik_inf:
            if dmg2 == 0:
                print("\nKalevipojal vältis edukalt "+ koll.nimiOm + " jalahoopi!\nKalevipojal on endiselt " + str(player.hp) + " elupunkti.")
            elif 0 < dmg2 <= 0.5*koll.dmg:
                print("\n" + koll.nimi + " lõi kalevipoega oma suure jalaga ning Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            elif 0.5*koll.dmg < dmg2 <= 0.8*koll.dmg:
                print("\nKalevipoeg jäi ämblikuvõrku lõksu! " + koll.nimi + " sai teda enne vabanemist korduvalt lüia ja hammustada ning Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            else:
                print("\n" + koll.nimi + " lõi Kalevipoja pikali ning " + koll.nimiOm + " vägevad lõuad sulguvad Kalevipoja kaela ümber... Kuid viimane proovib end valu trotsides vabaks võidelda. Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")

        elif type(koll) == harpüia_inf:
            if dmg2 == 0:
                print("\nKalevipojal läks korda "+ koll.nimiOm + " küünte vahelt läbi liuelda!\nKalevipojal on endiselt " + str(player.hp) + " elupunkti.")
            elif 0 < dmg2 <= 0.5*koll.dmg:
                print("\n" + koll.nimiOm + " nugateravad küüned riivasid Kalevipoega ning Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            elif 0.5*koll.dmg < dmg2 <= 0.8*koll.dmg:
                print("\n" + koll.nimiOm + " nõelteravad küüned suskasid sügavale Kalevipoja ihusse. Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            else:
                print("\nKalevipoeg kaotas hetkeks fookuse ja " + koll.nimiOm + " vahedad küüned lõikasid teda kõikjalt!" + koll.nimi + " sai isegi võimaluse oma oma kiskjahambad Kalevipoega lüüa. Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")

        elif type(koll) == zombi_inf:
            if dmg2 == 0:
                print("\nKalevipojal läks korda "+ koll.nimiOm + " kohmakate käte vahelt pääseda!\nKalevipojal on endiselt " + str(player.hp) + " elupunkti.")
            elif 0 < dmg2 <= 0.5*koll.dmg:
                print("\n" + koll.nimiOm + " virutas Kalevipoega ning Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            elif 0.5*koll.dmg < dmg2 <= 0.8*koll.dmg:
                print("\n" + koll.nimiOm + "l õnnestus meie kangelasele hambad sisse lüüa. Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            else:
                print("\n" + koll.nimiOm + " sai Kalevipoja oma haardesse ja " + koll.nimiOm + "l õnnestus Kalevipojalt hammastega tükk küljest rebida! Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")

        elif type(koll) == vampiir_inf:
            if dmg2 == 0:
                print("\nKalevipojal läks korda "+ koll.nimiOm + " käte vahelt pääseda!\nKalevipojal on endiselt " + str(player.hp) + " elupunkti.")
            elif 0 < dmg2 <= 0.5*koll.dmg:
                print("\n" + koll.nimiOm + " virutas oma küünistega kätega Kalevipoega ning Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            elif 0.5*koll.dmg < dmg2 <= 0.8*koll.dmg:
                print("\n" + koll.nimi + " lõi oma teravad esihambad Kalevipoega! Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            else:
                print("\n" + koll.nimiOm + " sai Kalevipoja oma haardesse, lõi hambad kangelase kaela ja imes mõnuga kuninglikku verd! Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")

        elif type(koll) == draakon_inf:
            if dmg2 == 0:
                print("\nImekombel läks Kalevipojal korda nii "+ koll.nimiOm + " küüniste kui ka leegi eest pääseda!\nKalevipojal on endiselt " + str(player.hp) + " elupunkti.")
            elif 0 < dmg2 <= 0.25*koll.dmg:
                print("\n" + koll.nimiOm + " poolemeetrine küünis riivas Kalevipoega ning Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            elif 0 < dmg2 <= 0.5*koll.dmg:
                print("\n" + koll.nimiOm + " kaks võimsat küünist said Kalevipojale pihta! Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            elif 0.5*koll.dmg < dmg2 <= 0.8*koll.dmg:
                print("\n" + koll.nimiOm + " leek kõrvetab ka kaugelt! Hea, et Kalevipoeg otse pihta ei saanud... Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            else:
                print("\nOi ei!" + koll.nimi + " purskas tuld ja Kalevipojal ei jäänud aega kõrvale hüpata! Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")

        elif type(koll) == rott_inf:
            if dmg2 == 0:
                print("\n"+ koll.nimiOm + " hambad näksasid tühja õhku!\nKalevipojal on endiselt " + str(player.hp) + " elupunkti.")
            elif dmg2 == 1:
                print("\n" + koll.nimiOm + " hambad said kalevipoja varba kätte! Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            else:
                print("\n" + koll.nimiOm + "l õnnestus Kalevipoega mööda üles ronida ja oma küüniste ja hammastega kangelasele haiget teha! Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")

        if type(koll) == vampiir_inf and koll.hp > 0:
            if dmg2 > 0.5*koll.dmg:
                koll.hp += round(0.75*dmg2)
                if koll.hp > 30:
                    koll.hp = 30
                sleep(0.75)
                print("\n" + koll.nimi + " imes omale " + str(round(0.75*dmg2)) + " elupunkti tagasi.\n" + koll.nimiOm + "l on nüüd " + str(koll.hp) + " elupunkti.\n")

        
    #Fighti lõpp
    if player.hp <= 0:
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

        #### Erinevad surmad ####
        if type(koll) == koll_inf:
            lõpp2 = koll.nimi + " haarab Kalevipoja peast kinni ning rebib selle otsast"
        elif type(koll) == hiidämblik_inf or type(koll) == hiigelämblik_inf:
            lõpp2 = koll.nimi + " lööb oma kihvad Kalevipoja kaela, tuimestades kangelase ja mähib ta seejärel tugevasse ämblikuvõrku"
        elif type(koll) == harpüia_inf:
            lõpp2 = koll.nimiOm + " teravad küüned suskavad Kalevipoja südamest läbi"
        elif type(koll) == zombi_inf:
            lõpp2 = koll.nimi + " võtab väsinud Kalevipoja oma haardesse ning pureb kangelase kägiveeni"
        elif type(koll) == vampiir_inf:
            lõpp2 = koll.nimi + " võtab väsinud Kalevipoja oma haardesse ning lööb kihvad kangelase kägiveeni"
        elif type(koll) == draakon_inf:
            lõpp2 = koll.nimiOm + " küünis läbistab Kalevipoja ja võiduka möirgega teeb lohe Kalevipojast grillliha"
        elif type(koll) == rott_inf:
            lõpp2 = koll.nimiOm + " pisikesed küüned rebivad küljest Kalevipoja silmad ning varsti jõuavad hambad ka kägiveenini kaelas"
                
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

    elif koll.hp <= 0:
        if type(koll) == koll_inf:
            lõpp1_1 = koll.nimi + " kukub korisedes sellili"
        elif type(koll) == hiidämblik_inf or type(koll) == hiigelämblik_inf:
            lõpp1_1 = koll.nimiOm + " jalad tõmbuvad krõnksu ja " + koll.nimi + " kukub selili maha"
        elif type(koll) == harpüia_inf:
            lõpp1_1 = koll.nimiOm + " auklikud tiivad ei ole enam võimelised " + koll.nimiOs + " õhus hoidma. " + koll.nimi + " kukub kohmakalt maha"
        elif type(koll) == zombi_inf:
            lõpp1_1 = koll.nimi + " kukub kähisedes kõhuli"
        elif type(koll) == vampiir_inf:
            lõpp1_1 = koll.nimi + " vajub põlvili ja tema piirjooned hägunevad"
        elif type(koll) == draakon_inf:
            lõpp1_1 = koll.nimi + " kukub maavärina saatel maha"
        elif type(koll) == rott_inf:
            lõpp1_1 = koll.nimi + " vajub niutsatusega kõhuli"

        for el in lõpp1_1:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.1)
        for el in [".",".","."]:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.8)
        print("\n")

        if type(koll) == koll_inf or type(koll) == harpüia_inf or type(koll) == zombi_inf:
            if type(relv) == mõõk_inf or type(relv) == vikat_inf:
                lõpp2_1 = "Kalevipoeg võtab " + relv.nimiOm + "st kahe käega kinni ning lööb selle lapiti " + koll.nimiOm + "le pähe kinni, purustades ta kolju ja muutes aju kördiks."
            elif type(relv) == nui_inf or type(relv) == sõjahaamer_inf:
                lõpp2_1 = "Kalevipoeg virutab " + relv.nimiOm + "ga vastu " + koll.nimiOm + " pead, purustades kolju ja muutes aju kördiks."
            elif type(relv) == piits_inf:
                lõpp2_1 = "Kalevipoja " + relv.nimi + " haakub ümber " + koll.nimiOm + " kaela ja tugeva tõmbega rebib Kalevipoeg " + koll.nimiOm + " pea otsast."
            elif type(relv) == vibu_inf or type(relv) == amb_inf:
                lõpp2_1 = "Kalevipoja läkitatud nool läheb " + koll.nimiOm + "l otse läbi silma ajju. Järgmine "+ relv.nimiOm + "nool läbistab südame."
            elif type(relv) == oda_inf or type(relv) == viskeoda_inf or type(relv) == nuga_inf:
                lõpp2_1 = "Kalevipoeg suskab " + relv.nimiOm + koll.nimiOm + "le otse lõua alla ja läbistab " + koll.nimiOm + " aju."

        elif type(koll) == hiidämblik_inf or type(koll) == hiigelämblik_inf:
            if type(relv) == mõõk_inf:
                lõpp2_1 = "Kalevipoeg võtab " + relv.nimiOm + "st kahe käega kinni ning lööb selle lapiti " + koll.nimiOm + "le pähe kinni, purustades ta kolju ja muutes aju kördiks."
            elif type(relv) == nui_inf or type(relv) == sõjahaamer_inf:
                lõpp2_1 = "Kalevipoeg virutab " + relv.nimiOm + "ga vastu " + koll.nimiOm + " pead, purustades kolju ja muutes aju kördiks."
            elif type(relv) == piits_inf:
                lõpp2_1 = "Kalevipoeg rebib " + relv.nimiOm + "ga ükshaaval " + koll.nimiOm + "l jalad küljest ja lõpuks on sama saatus ka peletise peal."
            elif type(relv) == amb_inf or type(relv) == vibu_inf:
                lõpp2_1 = "Kalevipoeg haarab " + relv.nimiOm + "noole kätte ja suskab ükshaaval igat " + koll.nimiOm + " silma."
            elif type(relv) == oda_inf or type(relv) == viskeoda_inf:
                lõpp2_1 = "Kalevipoeg haarab " + relv.nimiOm + "st kahe käega kinni ja rammib selle " + koll.nimiOm + " ajju."
            elif type(relv) == nuga_inf:
                lõpp2_1 = "Kalevipoeg suskab " + relv.nimiOs + koll.nimiOm + "igasse silma, kuni " + koll.nimiOm + "näost pole enam midagi järel."

        elif type(koll) == vampiir_inf:
            if type(relv) == mõõk_inf:
                lõpp2_1 = "Kalevipoeg raiub " + koll.nimiOm + " pea otsast, et saada tagasi varastatud veri. " + koll.nimi + " hajub eimillekski."
            elif type(relv) == nui_inf or type(relv) == sõjahaamer_inf:
                lõpp2_1 = "Kalevipoja " + relv.nimiOm + "löök purustab " + koll.nimiOm + " pea ja " + koll.nimi + " hajub eimillekski."
            elif type(relv) == piits_inf:
                lõpp2_1 = "Kalevipoja " + relv.nimi + " rebib " + koll.nimiOm + " pea otsast ja " + koll.nimi + " hajub igavikku."
            elif type(relv) == amb_inf or type(relv) == vibu_inf:
                lõpp2_1 = "Kalevipoeg pussitab " + relv.nimiOm + "noolega " + koll.nimiOs + " kuni see siit ilmast igavikku hajub."
            elif type(relv) == oda_inf or type(relv) == viskeoda_inf:
                lõpp2_1 = relv.Nimi + " läbistab " + koll.nimiOs + ", nii et see siit ilmast jäädavalt igavikku hajub." 
            elif type(relv) == nuga_inf:
                lõpp2_1 = "Kalevipoeg pussitab " + relv.nimiOm + "ga " + koll.nimiOs + " kuni see siit ilmast igavikku hajub."

        elif type(koll) == draakon_inf:
            if type(relv) == mõõk_inf:
                lõpp2_1 = "Kalevipoeg raiub " + relv.nimiOm + "ga tundideviisi " + koll.nimiOm + " soomuselist kaela, et pea trofeeks koduseinale saada." 
            elif type(relv) == nui_inf or type(relv) == sõjahaamer_inf:
                lõpp2_1 = "Kalevipoeg nüpeldab " +relv.nimiOm + "ga " + koll.nimiOm + "pead, kuni jõuab lõpuks vääriskividest ajuni."
            elif type(relv) == piits_inf:
                lõpp2_1 = relv.NimiOm + "lööke on kuulda veel mitu päeva, enne kui Kalevipoeg lõpuks " + koll.NimiOm + "ga ühele poole saab ja võidukalt vägeva eluka peaga koju naaseb."
            elif type(relv) == amb_inf or type(relv) == vibu_inf:
                lõpp2_1 = relv.NimiOm + "nooled purustavad " + koll.nimiOm + "silmad ja Kalevipoeg urgitseb silmaavadest kalliskive."
            elif type(relv) == oda_inf or type(relv) == viskeoda_inf or type(relv) == nuga_inf:
                lõpp2_1 = "Kalevipoeg suskab " +relv.nimiOs + " läbi " + koll.nimiOm + "silmaavade ja avastab, et relva otsa külge jäävad teemantid."

        elif type(koll) == rott_inf:
            lõpp2_2 = "Kalevipoeg astub jalaga " + koll.nimiOs + " lödiks."

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

#========================================================MÄNGU SELGROOG============================================================

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
        setup_game()
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
        tiitellehe_valikud()
        
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

### Mängu interaktiivsus ###
def käsk():
    print("\n" + "()===()===()===()===()===()===()===()")
    for el in "Mis on sinu järgmine tegevus?":
        sys.stdout.write(el)
        sys.stdout.flush()
        time.sleep(0.05)
    tegevus = input("\n> ")
    aktsepteeritud = ["mine", "liigu", "jookse", "kõnni", "jaluta", "pööra","keera", "patseeri", "flaneeri", "quit", "exit game"]
    while tegevus.lower() not in aktsepteeritud:
        for el in "Tundmatu käsk, proovime uuesti!.\n":
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.05)
        käsk()
    if tegevus.lower() in ["mine", "liigu", "jookse", "kõnni", "jaluta", "pööra", "keera", "patseeri", "flaneeri"]:
        player_movement()
    elif tegevus.lower() in ["quit", "exit game"]:
        os.system("clear")
        time.sleep(0.5)
        animeeri("Nägemiseni! :)")
        sys.exit()
        
def player_movement():
    animeeri("Kuhu sa minna soovid?\n")
    siht = input("> ")
    if siht.lower() == "poodi":
        shop()

    
### Mängu intro ###
#Nime küsimine jms
def setup_game():
    os.system("clear")
    for el in "Tervist, kes sa selline oled? Mis rüütlil nimeks on, kui küsida tohib?":
        sys.stdout.write(el)
        sys.stdout.flush()
        time.sleep(0.05)
    nimeks = input("\n> ")
    player.nimi = nimeks
    tervitus = player.nimi + "....."
    for el in tervitus:
        sys.stdout.write(el)
        sys.stdout.flush()
        time.sleep(0.25)
    for el in "Milline meeldiv nimi. Tere tulemast mängu, " + nimeks + "!":
        sys.stdout.write(el)
        sys.stdout.flush()
        time.sleep(0.05)
        
    time.sleep(3)
    os.system("clear")
    time.sleep(1.5)
    animeeri("Kikerikii!")
    print("\n")
    time.sleep(2)
    animeeri("Kikerikii!")
    print("\n")
    time.sleep(2)
    animeeri("Metsik kukk lõõritab sinu hurtsiku kõrval. Kellaosutid näitavad, et kell on saamas pool seitse hommikul.\n...\nKõht koriseb ning sa võtad mõne suutäie üleeilsest karaskist ja rüüpad mõdu peale. Nõnda algab sinu hommik meie maailmas. ")
    time.sleep(3)
    animeeri("Taskutes sobrades märkad, et sul on " + str(player.gold) + " kuldmünti.\n")
    time.sleep(2)
    animeeri("Sul on alati teada, et kohalik poeomanik, rüü- ning relvameister Otto äritseb Karuküüne külas.\nTeda saad sa alati külastada, kui sa just parasjagu võitlemisega hõivatud ei ole. Kirjutades käsk 'mine', 'liigu' vms ning siis 'poodi' saad sa Ottot külastada.\n")
    time.sleep(1)
    animeeri("...\n")
    time.sleep(1)
    animeeri("Sa teed oma kriuksuva ning kägiseva esiukse lahti ning astud maailma, kus varitsevad igasugused kollid ja loomad.\n")
    time.sleep(2)
    animeeri("Kui peaks juhtuma, et satud mõne kolliga võitlusesse ning sa ta ka maha lööd, leiad sa ta korjusest kuldmünte.\n")
    time.sleep(2)
    animeeri("Mõned kollid on ka teatud relva löögitüüpidele nõrgemad. Seda on hea meeles pidada. :)\n")
    time.sleep(2)
    animeeri("Aga kui juhtub, et kolli jõud käib sinu omast üle, siis saad rüübata erinevaid jooke keset võitlust, et teha end tugevamaks.\n")
    time.sleep(2)
    animeeri("Kui see ka ei aita ning koll sind maha lööb, lahkud sa siit maailmast ning naased oma kodumaailma tagasi...\n")
    time.sleep(2)
    animeeri("Aitab monoloogist. Alaku sinu retk meie maailmas!\n")
    time.sleep(2)
    käsk()
        

#display_the_logo()
"""    
tiitelleht()
tiitellehe_valikud()
käsk()
"""

fight(koll)