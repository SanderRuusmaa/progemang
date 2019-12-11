import cmd
import sys
import os
import textwrap
import time
from time import sleep
import random
from random import randint
import subprocess
from math import floor, ceil

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
        self.quick_fight = True
        self.nimi = ""
        self.hp = 20 #effective hp sel momendil
        self.hp_max = 20 #20 + rüüdest saadav hp rüü ostmisega muuta
        self.gold = 5

player = player_inf()

#===================================================================== RELVAD JA KOLLID ==================================================
### KOLLID ###

class koll_inf():
    def __init__(self):
        self.nimi = "Sookoll" 
        self.nimiOm = "Sookolli"
        self.nimiOs = "Sookolli"
        self.hp = 100
        self.maxhp = 100
        self.dmg = 10
        self.weakness = "lõikav"
        self.dodge = 20
        self.escape = 25
        self.auhind = 35
        self.alles = 2

class hiidämblik_inf():
    def __init__(self):
        self.nimi = "Hiidämblik" 
        self.nimiOm = "Hiidämbliku"
        self.nimiOs = "Hiidämblikku"
        self.hp = 30
        self.maxhp = 30
        self.dmg = 4
        self.weakness = "purustav"
        self.dodge = 15
        self.escape = 50
        self.auhind = 5
        self.alles = 10

class hiigelämblik_inf():
    def __init__(self):
        self.nimi = "Hiigelämblik" 
        self.nimiOm = "Hiigelämbliku"
        self.nimiOs = "Hiigelämblikku"
        self.hp = 60
        self.maxhp = 60
        self.dmg = 9
        self.weakness = "lõikav"
        self.dodge = 4
        self.escape = 20
        self.auhind = 25
        self.alles = 10

class harpüia_inf():
    def __init__(self):
        self.nimi = "Harpüia" 
        self.nimiOm = "Harpüia"
        self.nimiOs = "Harpüiat"
        self.hp = 25
        self.maxhp = 25
        self.dmg = 5
        self.weakness = "kaugrünnak"
        self.dodge = 35
        self.escape = 20
        self.auhind = 8
        self.alles = 8

class zombi_inf():
    def __init__(self):
        self.nimi = "Zombi" 
        self.nimiOm = "Zombi"
        self.nimiOs = "Zombit"
        self.hp = 15
        self.maxhp = 15
        self.dmg = 3
        self.weakness = "suskav"
        self.dodge = 3
        self.escape = 80
        self.auhind = 5
        self.alles = 10

class draakon_inf():
    def __init__(self):
        self.nimi = "Draakon" 
        self.nimiOm = "Draakoni"
        self.nimiOs = "Draakonit"
        self.hp = 500
        self.maxhp = 500
        self.dmg = 25
        self.weakness = "lõikav"
        self.weakness = "kaugrünnak"
        self.dodge = 5
        self.escape = 25
        self.auhind = 250
        self.alles = 1

class vampiir_inf():
    def __init__(self):
        self.nimi = "Vampiir" 
        self.nimiOm = "Vampiiri"
        self.nimiOs = "Vampiiri"
        self.hp = 30
        self.maxhp = 30
        self.dmg = 5
        self.weakness = "purustav"
        self.dodge = 25
        self.escape = 50
        self.auhind = 10
        self.alles = 5
        ### Vampiir imeb omale tugeva hiti puhul 3 või 4 elu tagasi

class rott_inf():
    def __init__(self):
        self.nimi = "Rott" 
        self.nimiOm = "Roti"
        self.nimiOs = "Rotti"
        self.hp = 5
        self.maxhp = 5
        self.dmg = 2
        self.weakness = "purustav"
        self.dodge = 25
        self.escape = 65
        self.auhind = 3
        self.alles = 10

class hiidrott_inf():
    def __init__(self):
        self.nimi = "Hiidrott" 
        self.nimiOm = "Hiidroti"
        self.nimiOs = "Hiidrotti"
        self.hp = 15
        self.maxhp = 15
        self.dmg = 4
        self.weakness = "purustav"
        self.dodge = 20
        self.escape = 60
        self.auhind = 5
        self.alles = 10

class hiigelrott_inf():
    def __init__(self):
        self.nimi = "Hiigelrott" 
        self.nimiOm = "Hiigelroti"
        self.nimiOs = "Hiigelrotti"
        self.hp = 35
        self.maxhp = 35
        self.dmg = 6
        self.weakness = "purustav"
        self.dodge = 13
        self.escape = 50
        self.auhind = 10
        self.alles = 8

class muumia_inf():
    def __init__(self):
        self.nimi = "Muumia" 
        self.nimiOm = "Muumia"
        self.nimiOs = "Muumiat"
        self.hp = 50
        self.maxhp = 50
        self.dmg = 6
        self.weakness = "suskav"
        self.dodge = 10
        self.escape = 75
        self.auhind = 20
        self.alles = 4
        #Tappev aura: Iga käigu lõpus kaotab mängija ceil(10% alles olevatest eludest)

class kummitus_inf():
    def __init__(self):
        self.nimi = "Kummitus" 
        self.nimiOm = "Kummituse"
        self.nimiOs = "Kummitust"
        self.hp = 20
        self.maxhp = 20
        self.dmg = 4
        self.weakness = "suskav"
        self.dodge = 50
        self.escape = 45
        self.auhind = 8
        self.alles = 8

class poltergeist_inf():
    def __init__(self):
        self.nimi = "Poltergeist" 
        self.nimiOm = "Poltergeisti"
        self.nimiOs = "Poltergeisti"
        self.hp = 50
        self.maxhp = 50
        self.dmg = 8
        self.weakness = "suskav"
        self.dodge = 50
        self.escape = 45
        self.auhind = 25
        self.alles = 4
        

rotid = [rott_inf(), hiidrott_inf()]
nõrgemad_kollid = [rott_inf(), hiidrott_inf(), kummitus_inf(), zombi_inf(), hiidämblik_inf(), harpüia_inf()]
tugevad_kollid = [poltergeist_inf(), muumia_inf(), hiigelrott_inf(), vampiir_inf(), hiigelämblik_inf(), koll_inf()]
boss = draakon_inf()

### =============================RELVAD========================== ###
class rusikad_inf():
    def __init__(self):
        self.Nimi = "Rusikad"
        self.nimi = "rusikad"
        self.NimiOm = "Rusikate"
        self.nimiOm = "rusikate"
        self.NimiOs = "Rusikaid"
        self.nimiOs = "rusikaid"
        self.min_dmg = 1
        self.dmg = 2
        self.miss = 5 # 10% võimalus, et rünnak ei lähe üldse läbi
        self.crit = 3 # Võimalus teha topeltdamage
        self.supercrit = 1 #Võimalus teha kolmekordselt damage'it
        self.type = "purustav"
        
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
        self.supercrit = 12
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
        self.type = "kaugrünnak"
        self.type = "lõikav"

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
        self.min_dmg = 3
        self.dmg = 4
        self.miss = 2
        self.crit = 12
        self.supercrit = 4
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
        self.type = "suskav"

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
        "amb": [50,False],
        "rusikad": [0,True]}

#Rüü HP boonused stackivad
rüüd = {"nahkrüü": [10,False], #+20HP
         "rõngassärk": [20,False], #+30HP
         "raudrüü": [35,False], #+35HP
         "meisterlik raudrüü": [50,False], #+45HP
         "haldjarauast rüü": [80,False]} #+50HP

#Vastavalt hind, kogus
võlujoogid = {"elujook I": [3,0], #+8HP
              "elujook II": [8,0], #+24HP
              "elujook III": [18,0], #+60HP
              "ründejook I": [3,0], #+1dmg õnnestunud rünnakul (ründejoogid ei stacki, parim töötab)
              "ründejook II": [8,0], #+2dmg õnnestunud rünnakul
              "ründejook III": [18,0], #+3dmg õnnestunud rünnakul
              "surematuse jook": [12,0], #3 käiku elu ei lange alla 1HP, cooldown 3+3 käiku
              "vampiirijook": [12,0]} #healid ceil(0.5*dmg1) iga käigu lõpus fighti lõpuni

oskused = {"Oskus teha vahel teine rünnak": [30,False],
           "Oskus võitluse käigus relva vahetada": [15,False], #implementeeritud
           "Oskus juua võlujooki käiku raiskamata": [40,False], #implementeeritud
           "Oskus alati võitlusest põgeneda": [40,False], #implementeeritud
           "Oskus õnnetuid lööke ja laske vältida": [40,False]} #implementeeritud

########## Poe funktsioon ############

def shop():
    print("Tere! ", end="")
    while True:
        valik = input("Mida soovite osta? Kui relvi, siis kirjutage \"relvad\", kui rüüsid, kirjutage \"rüüd\", kui võlujooke, kirjutage \"võlujoogid\", kui oskuseid, kirjutage \"oskused\", kui soovite poest lahkuda, kirjutage \"lahku\": ")
        sleep(0.5)
        if valik == "relvad":
            animeeri("\nAh et soovite meie kvaliteetseid relvi vaadata! Siin on meie valik:\n")
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
            animeeri("\nMa näen, et teid huvitab meie rüükollektsioon! Heitke pilk peale ja laduge raha lauale! Siin on meie valik:\n")
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
                    if valik2 == "nahkrüü":
                        player.hp += 20
                        player.hp_max += 20
                    elif valik2 == "rõngassärk":
                        player.hp += 30
                        player.hp_max += 30
                    elif valik2 == "raudrüü":
                        player.hp += 35
                        player.hp_max += 35
                    elif valik2 == "meisterlik raudrüü":
                        player.hp += 45
                        player.hp_max += 45
                    elif valik2 == "haldjarauast rüü":
                        player.hp += 50
                        player.hp_max += 50
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
            animeeri("\nNäen, et imetlete meie võlujooke. Need kõik võivad olla teie, kui te vaid maksate! Siin on meie valik:\n")
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
            animeeri("\nNäen, et uurite meie intensiivse treeningu kava. Paremaid võitlusoskuseid kui meiega ei saa te kuskil kuningriigis! Siin on meie pakutavad programmid:\n")
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

######testimiseks###########
koll = zombi_inf()
############################
def fight(koll):
    ####testimiseks####
    relv = rusikad_inf()
    oskused["Oskus teha vahel teine rünnak"][1] = True
    ###################
    
    põgene = False #Kas õnnestus põgeneda
    ründejook1 = False
    ründejook2 = False
    ründejook3 = False
    surematusejook = 0
    vampiirijook = False
    cooldown = 0 #loeb, millal saab surematuse jooki juua
    
    while koll.hp > 0 and player.hp > 0:
        #Siin seame parameetrid uue tsükli jaoks õigetele väärtusetele
        deftxt = True #kas lõpus prinditakse default teksti
        dmg1 = 0
        põgenemiskatse = False #kas prooviti põgeneda
        if cooldown > 0:
            cooldown -= 1
        if surematusejook > 0:
            surematusejook -= 1
        
        ##### valige relv ####
        if oskused["Oskus võitluse käigus relva vahetada"][1] == True:
            animeeri("Sinu relvavalik: \n")
            weapons = []
            for weapon in relvad:
                if relvad[weapon][1] == True:
                    weapons.append(weapon)
                    print("-",weapon)
            while True:
                valik = input("\nValige relv: ")
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
        #############################################

        #### Löögitugevuse, põgenemise või võlujoogi joomise valimine ####        
        dmg_katse = 1000
        while not relv.min_dmg <= dmg_katse <= relv.dmg: 
            dmg_katse = input("\nSisestage katsetatav löögi tugevus vahemikus " + str(relv.min_dmg) + "..." + str(relv.dmg) + " või \"põgene\": ")
            if dmg_katse == "põgene":
                põgenemiskatse = True
                if oskused["Oskus alati võitlusest põgeneda"][1] == True:
                    print("Oma meisterlikku põgenemisoskust kasutades oli Kalevipjal käkitegu " + koll.nimiOm + " eest plehku pista!")
                    põgene = True
                    dmg_katse = relv.min_dmg
                    break
                elif randint(1,100) <= koll.escape:
                    print("Kalevipojal õnnestus " + koll.nimiOm + " eest plehku pista!")
                    põgene = True
                    dmg_katse = relv.min_dmg
                    break
                else:
                    print("Oi ei! Põgenemiskatse nurjus!")
                    dmg_katse = 0
                    break

            ######## Võlujoogid #########
            elif dmg_katse in ["elujook I", "elujook II", "elujook III", "ründejook I", "ründejook II", "ründejook III", "surematuse jook", "vampiirijook"]:
                if võlujoogid[dmg_katse][1] >= 1:
                    if dmg_katse == "elujook I":
                        print("Jõite võlujooki Elujook I ja saite 8 elupunkti.")

                        puudu = player.hp_max - player.hp
                        if puudu > 8:
                            player.hp += 8
                        else:
                            player.hp = player.hp_max

                        võlujoogid[dmg_katse][1] -= 1
                        dmg_katse = 0
                        if oskused["Oskus juua võlujooki käiku raiskamata"][1] == False:
                            põgenemiskatse = True #et ta ei laseks playeril rünnata
                            break
                        
                    elif dmg_katse == "elujook II":
                        print("Jõite võlujooki Elujook II ja saite 24 elupunkti.")

                        puudu = player.hp_max - player.hp
                        if puudu > 24:
                            player.hp += 24
                        else:
                            player.hp = player.hp_max
                        
                        võlujoogid[dmg_katse][1] -= 1
                        dmg_katse = 0
                        if oskused["Oskus juua võlujooki käiku raiskamata"][1] == False:
                            põgenemiskatse = True
                            break
                        
                    elif dmg_katse == "elujook III":
                        print("Jõite võlujooki Elujook III ja saite 60 elupunkti.")

                        puudu = player.hp_max - player.hp
                        if puudu > 60:
                            player.hp += 60
                        else:
                            player.hp = player.hp_max
                        
                        võlujoogid[dmg_katse][1] -= 1
                        dmg_katse = 0
                        if oskused["Oskus juua võlujooki käiku raiskamata"][1] == False:
                            põgenemiskatse = True
                            break
                        
                    elif dmg_katse == "ründejook I":
                        if ründejook1 == False and ründejook2 == False and ründejook3 == False:
                            ründejook1 = True
                            print("Jõite võlujooki Ründejook I ja ründate võitluse lõpuni 1 elupunkti võrra tugevamalt.")
                            võlujoogid[dmg_katse][1] -= 1
                            dmg_katse = 0
                            if oskused["Oskus juua võlujooki käiku raiskamata"][1] == False:
                                põgenemiskatse = True
                                break
                        else:
                            print("See või parem ründejook on juba aktiivne!")
                        
                    elif dmg_katse == "ründejook II":
                        if ründejook2 == False and ründejook3 == False:
                            ründejook2 = True
                            print("Jõite võlujooki Ründejook II ja ründate võitluse lõpuni 2 elupunkti võrra tugevamalt.")
                            võlujoogid[dmg_katse][1] -= 1
                            dmg_katse = 0
                            if oskused["Oskus juua võlujooki käiku raiskamata"][1] == False:
                                põgenemiskatse = True
                                break
                        else:
                            print("See või parem ründejook on juba aktiivne!")
                            
                    elif dmg_katse == "ründejook III":
                        if ründejook3 == False:
                            ründejook3 = True
                            print("Jõite võlujooki Ründejook III ja ründate võitluse lõpuni 3 elupunkti võrra tugevamalt.")
                            võlujoogid[dmg_katse][1] -= 1
                            dmg_katse = 0
                            if oskused["Oskus juua võlujooki käiku raiskamata"][1] == False:
                                põgenemiskatse = True
                                break
                        else:
                            print("See jook on juba aktiivne!")
                        
                    elif dmg_katse == "surematuse jook":
                        if cooldown == 0:
                            surematusejook = 3
                            print("Jõite võlujooki " + str(dmg_katse))
                            võlujoogid[dmg_katse][1] -= 1
                            cooldown += 6
                            dmg_katse = 0
                            if oskused["Oskus juua võlujooki käiku raiskamata"][1] == False:
                                põgenemiskatse = True
                                break
                        else:
                            print("Seda jooki ei saa veel " + str(cooldown) + " käiku juua!")
                            dmg_katse = 0
                        
                    elif dmg_katse == "vampiirijook":
                        vampiirijook = True
                        print("Jõite võlujooki " + str(dmg_katse))
                        võlujoogid[dmg_katse][1] -= 1
                        dmg_katse = 0
                        if oskused["Oskus juua võlujooki käiku raiskamata"][1] == False:
                            põgenemiskatse = True
                            break
                        
                else:
                    print("Teil pole seda võlujooki!")
                    dmg_katse = 0                                 
            else:
                try:
                    dmg_katse = int(dmg_katse)
                except:
                    dmg_katse = 0

        if põgene == True:
            break

        print("\n")

        #### Missimine ####
        #Siia võib veel panna erinevad read vastavalt sisestatud dmg_katse väärtusele
        if põgenemiskatse == False:
            if randint(1,100) <= koll.dodge:
                if type(koll) == koll_inf or type(koll) == vampiir_inf:
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == piits_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf or type(relv) == rusikad_inf:
                        print(koll.nimi + " kargles mängleva kergusega löögi eest kõrvale.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == oda_inf or type(relv) == nuga_inf:
                        print(koll.nimi + " tegi osava tagasihüppe, nii et suse tabas vaid õhku.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")
                    elif type(relv) == viskeoda_inf:
                        print(koll.nimiOm + "l õnnestus veel aegsasti lendava oda eest kõrvale hüpata.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")
                    elif type(relv) == vibu_inf or type(relv) == amb_inf:
                        print(koll.nimi + " nägi aegsasti noolt ja heade refleksidega suutis end selle teelt eest väänata.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")

                elif type(koll) == hiidämblik_inf or type(koll) == hiigelämblik_inf:
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf or type(relv) == rusikad_inf:
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
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf or type(relv) == rusikad_inf:
                        print(koll.nimi + " vilgas keha ei saanud pihta.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == oda_inf or type(relv) == nuga_inf:
                        print(koll.nimi + " lendles kergelt suske eest kõrvale.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == viskeoda_inf:
                        print(koll.nimiOm + "l oli napilt aega oda eest kõrvale liuelda.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == vibu_inf or type(relv) == amb_inf:
                        print("Nool ei tabanud "+ koll.nimiOs + ", sest tal õnnestus tiivad kokku tõmmata asukohta kiiresti muuta.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == piits_inf:                
                        print(koll.nimi + " sai piitsa teelt kõrvale, nii et kuulda oli vaid tühja vihinat.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 

                elif type(koll) == zombi_inf or type(koll) == muumia_inf:
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == piits_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf or type(relv) == rusikad_inf:
                        print(koll.nimi + " tuias löögi eest kõrvale.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == oda_inf or type(relv) == nuga_inf:
                        print(koll.nimi + " tegi sammu tagasi, nii et suse tabas vaid õhku.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")
                    elif type(relv) == viskeoda_inf:
                        print(koll.nimiOm + "l õnnestus napilt lendava oda eest kõrvale astuda.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")
                    elif type(relv) == vibu_inf or type(relv) == amb_inf:
                        print(koll.nimi + " suutis noole teelt eest tuigerdada.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")

                elif type(koll) == rott_inf or type(koll) == hiidrott_inf or type(koll) == hiigelrott_inf:
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == piits_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf or type(relv) == rusikad_inf:
                        print(koll.nimi + " sibas löögi eest kõrvale.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == oda_inf or type(relv) == nuga_inf:
                        print(koll.nimi + " sibas suske eest kõrvale.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == viskeoda_inf:
                        print(koll.nimi + " sibas oda eest kõrvale.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == vibu_inf or type(relv) == amb_inf:
                        print(koll.nimi + " sibas noole teelt.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 

                elif type(koll) == draakon_inf:
                    if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf or type(relv) == rusikad_inf:
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

                elif type(koll) == kummitus_inf or type(koll) == poltergeist_inf:
                    if type(relv) != rusikad_inf and type(relv) != vibu_inf and type(relv) != amb_inf:
                        print(relv.Nimi + " vuhises otse läbi " + koll.nimiOm + ", vigastusi põhjustamata.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == vibu_inf or type(relv) == amb_inf:
                        print(relv.NimiOm + "nool vuhises otse läbi " + koll.nimiOm + ", vigastusi põhjustamata.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.") 
                    elif type(relv) == rusikad_inf:
                        print(relv.Nimi + " vuhisesid otse läbi " + koll.nimiOm + ", vigastusi põhjustamata.\n" + koll.nimiOm + "l on ikka " + str(koll.hp) + " elupunkti.")

            elif dmg_katse <= randint(relv.min_dmg,relv.dmg):
                if randint(1,100)<=relv.miss and oskused["Oskus õnnetuid lööke ja laske vältida"][1] == False:
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
                    elif type(relv) == rusikad_inf:
                        print("On vast ebaõnn! Rusikahoop läks hoopis mööda!")
                    deftxt = False #et default prinditavat teksti muuta
                    
                else:
                    param = randint(1,100)
                    if param <= relv.crit and param > relv.supercrit:
                        dmg1 = dmg_katse*2
                        if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf or type(relv) == rusikad_inf: 
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
                        if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf or type(relv) == rusikad_inf: 
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
                dmg1 = relv.min_dmg

     
        dmg2 = randint(0, koll.dmg) #kolli tehtud dmg  
        player.hp -= dmg2
        if põgenemiskatse == False:
            koll.hp -= dmg1


        ##### Kalevipoja tehtud dmg-le vastav tekst#####
        sleep(0.5)
        if põgenemiskatse == False:
            if deftxt == True and dmg1 != 0:
                if type(relv) == mõõk_inf or type(relv) == vikat_inf or type(relv) == sõjahaamer_inf or type(relv) == nui_inf or type(relv) == rusikad_inf:
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

            if ründejook3 == True and dmg1 != 0:
                koll.hp -= 3
                print("\nRündejoogist III saadud jõu tõttu kaotas " + koll.nimi + " veel 3 elupunkti. " + koll.nimiOm + "l on nüüd " + str(koll.hp) + " elupunkti.")
            elif ründejook2 == True and dmg1 != 0:
                koll.hp -= 2
                print("\nRündejoogist II saadud jõu tõttu kaotas " + koll.nimi + " veel 2 elupunkti. " + koll.nimiOm + "l on nüüd " + str(koll.hp) + " elupunkti.")
            elif ründejook1 == True and dmg1 != 0:
                koll.hp -= 1
                print("\nRündejoogist III saadud jõu tõttu kaotas " + koll.nimi + " veel 3 elupunkti. " + koll.nimiOm + "l on nüüd " + str(koll.hp) + " elupunkti.")
            
        if oskused["Oskus teha vahel teine rünnak"][1] == True and randint(1,100) < 20:
            print("\nKalveipojal õnnestus teha veel üks rünnak!")
            sleep(0.75)
            if randint(1,100)<=koll.dodge:
                print("\n... kuid " + koll.nimiOm + "l õnnestus seda vältida. " + koll.nimiOm + "l on endiselt " + str(koll.hp) + " elupunkti.")
            elif randint(1,100)<=relv.miss and oskused["Oskus õnnetuid lööke ja laske vältida"][1] == False:
                if type(relv) == mõõk_inf or type(relv) == vikat_inf:
                    print("\n... kuid Kalevipoja " + relv.nimi + " takerdus mättasse!\n" + koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                elif type(relv) == amb_inf or type(relv) == vibu_inf:
                    print("\n... kuid " + relv.nimiOm+ "nool lendas kaarega üle " + koll.nimiOm + " pea!\n" + koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                elif type(relv) == sõjahaamer_inf:
                    print("\n... kuid "+ koll.nimiOm + " pea asemel purustas möödaläinud löök süütu kivirahnu.\n" + koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                elif type(relv) == nui_inf:
                    print("\n... kuid ebamugava käepideme tõttu pudenes " + relv.nimi + " Kalevipojal käest!\n" + koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                elif type(relv) == nuga_inf or type(relv) == oda_inf:
                    print("\n... kuid " + relv.nimi + " tabas vaid paljast õhku.\n" +koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                elif type(relv) == piits_inf:
                    print("\n... kuid " + relv.nimi + " takerdus enne " + koll.nimiOm + "ni jõudmist millessegi.\n" + koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                elif type(relv) == viskeoda_inf:
                    print("\n... kuid Kalevipoeg viskas " + relv.NimiOs + " vale ots ees ja see kukkus õnnetult enne " + koll.nimiOm + " lähedalegi jõudmist maha.\n"+ koll.nimiOm+ "l on ikka " + str(koll.hp) + " elupunkti.")
                elif type(relv) == rusikad_inf:
                    print("\n... kuid rusikahoop läks hoopis mööda!")
            elif randint(relv.min_dmg,relv.dmg) >= dmg1:
                koll.hp -= dmg1
                print("\n... ja " + koll.nimi + " kaotas " + str(dmg1) + " elupunkti! " + koll.nimiOm + "l on nüüd " + str(koll.hp) + " elupunkti.")
            else:
                koll.hp -= relv.min_dmg
                print("\n... ja ehkki löök polnud õnnestunuim, kaotas " + koll.nimi + " siiski " + str(dmg1) + " elupunkti! " + koll.nimiOm + "l on nüüd " + str(koll.hp) + " elupunkti.")

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
                print("\nKalevipoeg vältis edukalt "+ koll.nimiOm + " jalahoopi!\nKalevipojal on endiselt " + str(player.hp) + " elupunkti.")
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

        elif type(koll) == zombi_inf or type(koll) == muumia_inf:
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

        elif type(koll) == hiidrott_inf or type(koll) == hiigelrott_inf:
            if dmg2 == 0:
                print("\n"+ koll.nimiOm + " hambad näksasid tühja õhku!\nKalevipojal on endiselt " + str(player.hp) + " elupunkti.")
            elif 0 < dmg2 <= 0.5*koll.dmg:
                print("\n" + koll.nimi + " hammustas Kalevipoega! Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            elif 0.5*koll.dmg < dmg2:
                print("\n" + koll.nimi + " sai Kalevipoja väga kõvasti hambusse! Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")

        elif type(koll) == kummitus_inf or type(koll) == poltergeist_inf:
            if dmg2 == 0:
                print("\nKalevipoeg lõi jalaga mulda üles ja " + koll.nimiOm + "l ei õnnestunud hinge imeda!\nKalevipojal on endiselt " + str(player.hp) + " elupunkti.")
            elif 0 < dmg2 <= 0.7*koll.dmg:
                print("\n" + koll.nimi + " imes kalevipoja hinge! Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")
            elif 0.7*koll.dmg < dmg2:
                print("\n" + koll.nimi + " imes Kalevipoja hinge ja oli tunda, kuidas tükk kangelasest lahkus. Kalevipoeg kaotas " + str(dmg2) + " elupunkti.\n" + "Kalevipojal on " + str(player.hp) + " elupunkti.")


        if type(koll) == vampiir_inf and koll.hp > 0:
            if dmg2 > 0.5*koll.dmg:
                koll.hp += round(0.75*dmg2)
                if koll.hp > 30:
                    koll.hp = 30
                sleep(0.75)
                print("\n" + koll.nimi + " imes omale " + str(round(0.75*dmg2)) + " elupunkti tagasi.\n" + koll.nimiOm + "l on nüüd " + str(koll.hp) + " elupunkti.\n")

        if type(koll) == muumia_inf and koll.hp > 0:
            surmav_aura = ceil(player.hp*0.1)
            player.hp -=surmav_aura
            print("\nMuumia surmav aura põletab Kalevipoja sisemust. Kalevipoeg kaotab " + str(surmav_aura) + " elupunkti.\nKalevipojal on nüüd " + str(player.hp) + " elupunkti.")

        if player.hp <= 0 and surematusejook > 0:
            print("\nSurematuse jook päästis Kalevipoja elu! Kalevipojal on 1 elupunkt.")
            player.hp = 1

        if vampiirijook == True and player.hp > 0:
            print("\nVampiirijook taastas Kalevipojal " + str(ceil(0.5*dmg1)) + " elupunkti. Kalevipojal on nüüd " + str(player.hp + ceil(0.5*dmg1)) + " elupunkti.")
            player.hp += ceil(0.5*dmg1)
            if player.hp > player.hp_max:
                player.hp = player.hp_max
            
        if player.quick_fight == True:
            print("\n(" + str(player.hp), str(koll.hp) + ")")
            


    ######### Fighti lõpp ############
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
        elif type(koll) == hiidrott_inf or type(koll) == hiigelrott_inf:
            lõpp2 = koll.nimi + " närib ja küünistab Kalevipoega, kuni järele jääb ainult skelett ja punaseks värvunud maalapp"
        elif type(koll) == muumia_inf:
            lõpp2 = "Kangelane vajub surmava aura käes pikali. " + koll.nimi + " mähib Kalevipoja kaltsudesse ja varsti tõusebki uus " + koll.nimi + "."
        elif type(koll) == kummitus_inf or type(koll) == poltergeist_inf:
            lõpp2 = koll.nimi + " sai kätte Kalevipoja viimase hingeraasu, kangelasest jääb alles vaid tühi kest."
                
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
        player.mängu_staatus = True

    elif koll.hp <= 0:
        if type(koll) == koll_inf:
            lõpp1_1 = "\n" + koll.nimi + " kukub korisedes sellili"
        elif type(koll) == hiidämblik_inf or type(koll) == hiigelämblik_inf:
            lõpp1_1 = "\n" + koll.nimiOm + " jalad tõmbuvad krõnksu ja " + koll.nimi + " kukub selili maha"
        elif type(koll) == harpüia_inf:
            lõpp1_1 = "\n" + koll.nimiOm + " auklikud tiivad ei ole enam võimelised " + koll.nimiOs + " õhus hoidma. " + koll.nimi + " kukub kohmakalt maha"
        elif type(koll) == zombi_inf or type(koll) == muumia_inf:
            lõpp1_1 = "\n" + koll.nimi + " kukub kähisedes kõhuli"
        elif type(koll) == vampiir_inf:
            lõpp1_1 = "\n" + koll.nimi + " vajub põlvili ja tema piirjooned hägunevad"
        elif type(koll) == draakon_inf:
            lõpp1_1 = "\n" + koll.nimi + " kukub maavärina saatel maha"
        elif type(koll) == rott_inf:
            lõpp1_1 = "\n" + koll.nimi + " vajub niutsatusega kõhuli"
        elif type(koll) == hiidrott_inf or type(koll) == hiigelrott_inf:
            lõpp1_1 = "\n" + koll.nimi + " vajub kähinaga kõhuli."
        elif type(koll) == kummitus_inf or type(koll) == poltergeist_inf:
            lõpp1_1 = "\n" + koll.nimi + " tardub õhus."

        for el in lõpp1_1:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.1)
        for el in [".",".","."]:
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.8)
        print("\n")

        if type(koll) == koll_inf or type(koll) == harpüia_inf or type(koll) == zombi_inf or type(koll) == muumia_inf:
            if type(relv) == mõõk_inf or type(relv) == vikat_inf:
                lõpp2_1 = "Kalevipoeg võtab " + relv.nimiOm + "st kahe käega kinni ning lööb selle lapiti " + koll.nimiOm + "le pähe kinni, purustades ta kolju ja muutes aju kördiks."
            elif type(relv) == nui_inf or type(relv) == sõjahaamer_inf or type(relv) == rusikad_inf:
                lõpp2_1 = "Kalevipoeg virutab " + relv.nimiOm + "ga vastu " + koll.nimiOm + " pead, purustades kolju ja muutes aju kördiks."
            elif type(relv) == piits_inf:
                lõpp2_1 = "Kalevipoja " + relv.nimi + " haakub ümber " + koll.nimiOm + " kaela ja tugeva tõmbega rebib Kalevipoeg " + koll.nimiOm + " pea otsast."
            elif type(relv) == vibu_inf or type(relv) == amb_inf:
                lõpp2_1 = "Kalevipoja läkitatud nool läheb " + koll.nimiOm + "l otse läbi silma ajju. Järgmine "+ relv.nimiOm + "nool läbistab südame."
            elif type(relv) == oda_inf or type(relv) == viskeoda_inf or type(relv) == nuga_inf:
                lõpp2_1 = "Kalevipoeg suskab " + relv.nimiOm + " " + koll.nimiOm + "le otse lõua alla ja läbistab " + koll.nimiOm + " aju."

        elif type(koll) == hiidämblik_inf or type(koll) == hiigelämblik_inf:
            if type(relv) == mõõk_inf or type(relv) == vikat_inf:
                lõpp2_1 = "Kalevipoeg võtab " + relv.nimiOm + "st kahe käega kinni ning lööb selle lapiti " + koll.nimiOm + "le pähe kinni, purustades ta kolju ja muutes aju kördiks."
            elif type(relv) == nui_inf or type(relv) == sõjahaamer_inf or type(relv) == rusikad_inf:
                lõpp2_1 = "Kalevipoeg virutab " + relv.nimiOm + "ga vastu " + koll.nimiOm + " pead, purustades kolju ja muutes aju kördiks."
            elif type(relv) == piits_inf:
                lõpp2_1 = "Kalevipoeg rebib " + relv.nimiOm + "ga ükshaaval " + koll.nimiOm + "l jalad küljest ja lõpuks on sama saatus ka peletise peal."
            elif type(relv) == amb_inf or type(relv) == vibu_inf:
                lõpp2_1 = "Kalevipoeg haarab " + relv.nimiOm + "noole kätte ja suskab ükshaaval igat " + koll.nimiOm + " silma."
            elif type(relv) == oda_inf or type(relv) == viskeoda_inf:
                lõpp2_1 = "Kalevipoeg haarab " + relv.nimiOm + "st kahe käega kinni ja rammib selle " + koll.nimiOm + " ajju."
            elif type(relv) == nuga_inf:
                lõpp2_1 = "Kalevipoeg suskab " + relv.nimiOs + " " + koll.nimiOm + "igasse silma, kuni " + koll.nimiOm + "näost pole enam midagi järel."

        elif type(koll) == vampiir_inf:
            if type(relv) == mõõk_inf or type(relv) == vikat_inf:
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
            elif type(relv) == rusikad_inf:
                lõpp2_1 = "Kalevipoeg virutab " + relv.nimiOm + "ga " + koll.nimiOm + "l hambad sisse ja peksab teda, kuni temast siia ilma enam kübetki ei jää."

        elif type(koll) == draakon_inf:
            if type(relv) == mõõk_inf or type(relv) == vikat_inf:
                lõpp2_1 = "Kalevipoeg raiub " + relv.nimiOm + "ga tundideviisi " + koll.nimiOm + " soomuselist kaela, et pea trofeeks koduseinale saada." 
            elif type(relv) == nui_inf or type(relv) == sõjahaamer_inf:
                lõpp2_1 = "Kalevipoeg nüpeldab " +relv.nimiOm + "ga " + koll.nimiOm + "pead, kuni jõuab lõpuks vääriskividest ajuni."
            elif type(relv) == piits_inf:
                lõpp2_1 = relv.NimiOm + "lööke on kuulda veel mitu päeva, enne kui Kalevipoeg lõpuks " + koll.NimiOm + "ga ühele poole saab ja võidukalt vägeva eluka peaga koju naaseb."
            elif type(relv) == amb_inf or type(relv) == vibu_inf:
                lõpp2_1 = relv.NimiOm + "nooled purustavad " + koll.nimiOm + "silmad ja Kalevipoeg urgitseb silmaavadest kalliskive."
            elif type(relv) == oda_inf or type(relv) == viskeoda_inf or type(relv) == nuga_inf:
                lõpp2_1 = "Kalevipoeg suskab " +relv.nimiOs + " läbi " + koll.nimiOm + "silmaavade ja avastab, et relva otsa külge jäävad teemantid."
            elif type(relv) == rusikad_inf:
                lõpp2_1 = "Kalevipoeg virtab ome rusika " + koll.nimiOm + " silmaauku, sobrab tema ajus ja tõmbab välja säravaid kalliskive."

        elif type(koll) == rott_inf:
            lõpp2_1 = "Kalevipoeg astub jalaga " + koll.nimiOm + " lödiks."

        elif type(koll) == hiidrott_inf or type(koll) == hiigelrott_inf:
            if type(relv) == mõõk_inf:
                lõpp2_1 = "Kalevipoeg raiub " + relv.nimiOm + "ga " + koll.nimiOm + " pea otsast."
            elif type(relv) == nui_inf or type(relv) == sõjahaamer_inf or type(relv) == rusikad_inf:
                lõpp2_1 = "Kalevipoeg lömastab " + relv.nimiOm + "ga " + koll.nimiOm + " pea."
            elif type(relv) == piits_inf:
                lõpp2_1 = "Kalevipoeg lööb " + relv.nimiOm + "ga " + koll.nimi + " ribadeks."
            elif type(relv) == amb_inf or type(relv) == vibu_inf:
                lõpp2_1 = relv.NimiOm + "nool läbistab " + koll.nimiOm + " kolju."
            elif type(relv) == oda_inf or type(relv) == viskeoda_inf or type(relv) == nuga_inf:
                lõpp2_1 = relv.NimiOm + "hoop purustab " + koll.nimiOm + " pea."

        elif type(koll) == kummitus_inf or type(koll) == poltergeist_inf:
            lõpp2_1 = koll.nimi + " muutub uduvineks ja hajub, jättes maha vaid pisut kulda."


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

        print("\nKalevipeg leidis surnukehalt " + str(koll.auhind) + " kuldmünti.")
        player.gold += koll.auhind
        koll.hp = koll.maxhp
        koll.alles -= 1
        if koll.alles == 0:
            if koll in rotid:
                rotid.remove(koll)
            elif koll in nõrgemad_kollid:
                nõrgemad_kollid.remove(koll)
            elif koll in tugevamad_kollid:
                tugevamad_kollid.remove(koll)

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
    print("Navigeerimine: Kui sa liigud")
    print("ühes suunas 5 korda, siis sa")
    print("saad järgmisesse tsooni.   ")
    print("                           ")
    print("Igas järgnevas tsoonis leidub")
    print("tugevamaid kolle.          ")
    print("                           ")
    print("Kui sa soovid läbi uuritud ")
    print("tsoonide vahel kiiresti    ")
    print("liikuda, kirjutda järgmiseks")
    print("tegevuseks 'quicktravel'   ")
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
move_counter = 0
läände = 0
itta = 0
põhja = 0
lõunasse = 0
quicktravel = False

def käsk():
    global quicktravel
    print("\n" + "()===()===()===()===()===()===()===()")
    for el in "Mis on sinu järgmine tegevus?":
        sys.stdout.write(el)
        sys.stdout.flush()
        time.sleep(0.05)
    tegevus = input("\n> ")
    aktsepteeritud = ["mine", "liigu", "jookse", "kõnni", "jaluta", "pööra","keera", "patseeri", "flaneeri", "quit", "exit game", "quicktravel"]
    if tegevus.lower() not in aktsepteeritud:
        print("Tundmatu käsk, proovime uuesti...")
    while tegevus.lower() not in aktsepteeritud:
        käsk()
    if tegevus.lower() in ["mine", "liigu", "jookse", "kõnni", "jaluta", "pööra", "keera", "patseeri", "flaneeri"]:
        player_movement()
    elif tegevus.lower() == "quicktravel":
        quicktravel = True
        player_movement()
    elif tegevus.lower() in ["quit", "exit game"]:
        os.system("clear")
        time.sleep(0.5)
        animeeri("Nägemiseni! :)")
        sys.exit()
        
def player_movement():
    global itta
    global läände
    global põhja
    global lõunasse
    global quicktravel
    global move_counter
    #QUICK TRAVEL#
    if quicktravel == True:
        animeeri("Kuhu sa kiiresti liikuda sooviksid? (Sisesta tsooni nimi)\n")
        siht = input("> ")
        if siht.lower().capitalize() in asukohad:
            indeks = asukohad.index(siht.lower().capitalize())
            if kaart[asukohad[indeks]] is True:
                move_counter = indeks
                animeeri("Sa kiirliikusid kohta, nimega " + asukohad[move_counter] +".\n\n")
            else:
                animeeri("See tsoon on avastamata, seega sinna ei saa kiirliikuda! Jääd samasse tsooni.\n\n")
            
        else:
            animeeri("Tundmatu asukoht.")
         
        quicktravel = False
        
        
    animeeri("Kuhu sa minna soovid? (läände, itta, põhja, lõunasse, poodi)\n")
    siht = input("> ")
    chance = randint(0,2)
    if siht.lower() == "poodi":
        shop()
    elif siht.lower() == "läände":
        läände += 1
        animeeri("Liikusid suunaga läände.\n")
        liikumine()
        if chance == 1 or chance == 2:
            kolli_rünne()
    elif siht.lower() == "itta":
        itta += 1
        animeeri("Liikusid itta.\n")
        liikumine()
        if chance == 1 or chance == 2:
            kolli_rünne()
    elif siht.lower() == "põhja":
        põhja += 1
        animeeri("Jalutasid põhja suunas.\n")
        liikumine()
        if chance == 1 or chance == 2:
            kolli_rünne()
    elif siht. lower() == "lõunasse":
        lõunasse += 1
        animeeri("Patseerisid lõuna suunas.\n")
        liikumine()
        if chance == 1 or chance == 2:
            kolli_rünne()
    else:
        print("Tundmatu käsk, proovime uuesti...\n")
    
### Mängu intro ###
#Nime küsimine jms
def setup_game():
    os.system("clear")
    for el in "Tervist, kes sa selline oled? Mis sul nimeks on, kui küsida tohib?":
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
    animeeri("Mõõga peegeldusest märkad, et sa oled muistne eesti kangelane, Kalevipoeg.")
    time.sleep(1.5)
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
    animeeri("Aitab monoloogist. Alaku sinu retk meie maailmas! Kivi kotti, Kalevipoeg.\n")
    time.sleep(4)
    os.system("clear")
    käsk()
###MÄNGU KAART###
#Teen lineaarse kaardi, lihtsalt counteriga vaatan, et kui sa oled liikunud mingi arv kordi ühes suunas, siis tuleb järgmine tsoon
asukohad = ["Oma kodu", "Näriliste põld", "Verejärv", "Surnumets", "Kolliväli", "Kondimägi", "Printsessi torn"]
kaart = {
    asukohad[0]: True,  #oma talu
    asukohad[1]: False, #näriliste põld
    asukohad[2]: False, #Verejärv
    asukohad[3]: False, #surnumets
    asukohad[4]: False, #kolliväli
    asukohad[5]: False, #kondmimägi
    asukohad[6]: False, #printsessi torn
    }

def liikumine():
    global move_counter
    global läände
    global itta
    global põhja
    global lõunasse
    global quicktravel
    if abs(läände - itta) > 4:
        animeeri("\nSa jõudsid kohta, nimega " + asukohad[move_counter + 1] + ".\n")
        move_counter += 1
        kaart[asukohad[move_counter]] = True
        läände, itta, põhja, lõunasse = 0, 0, 0, 0
    elif abs(põhja - lõunasse) > 4:
        animeeri("\nSa jõudsid kohta, nimega " + asukohad[move_counter + 1] + ".\n")
        move_counter += 1
        kaart[asukohad[move_counter]] = True
        läände, itta, põhja, lõunasse = 0, 0, 0, 0
        
def kolli_rünne():
    """ rotid = [rott_inf(), hiidrott_inf()]
        nõrgemad_kollid = [rott_inf(), hiidrott_inf(), kummitus_inf(), zombi_inf(), hiidämblik_inf(), harpüia_inf()]
        tugevad_kollid = [poltergeist_inf(), muumia_inf(), hiigelrott_inf(), vampiir_inf(), hiigelämblik_inf(), koll_inf()]
        boss = draakon_inf()"""
    chance = randint(0, 10)
    
    if asukohad[move_counter] == "Näriliste põld":
        if chance <= 7:
            animeeri("Ah sa mait, sinu teele kargas " + rotid[0].nimi + "...\nAlgab vägev võitlus.")
            fight(rotid[0])
        else:
            animeeri("Ah sa mait, sinu teele kargas " + rotid[1].nimi + "...\nAlgab vägev võitlus.")
            fight(rotid[1])
            
    elif asukohad[move_counter] == "Verejärv":
        if chance <=7:
            koll1 = random.choice(nõrgemad_kollid)
            animeeri("Oi pagan! Verd täis järvest roomas välja " + koll1.nimi + "...\nAlgab vägev võitlus.")
            fight(koll1)
        else:
            koll1 = hiigelrott_inf()
            animeeri("Oi pagan! Verd täis järvest roomas välja " + koll1.nimi + "...\nAlgab vägev võitlus.")
            fight(koll1)
            
    elif asukohad[move_counter] == "Surnumets":
        if chance <= 6:
            koll1 = random.choice(nõrgemad_kollid)
            animeeri("Oh õudust! Vana tamme tagant hüppas välja " + koll1.nimi + "...\nAlgab vägev võitlus.")
            fight(koll1)
        else:
            koll1 = random.choice([muumia_inf(), hiigelrott_inf(), hiigelämblik_inf()])
            animeeri("Oh õudust! Vana tamme tagant hüppas välja " + koll1.nimi + "...\nAlgab vägev võitlus.")
            fight(koll1)
    
    elif asukohad[move_counter] == "Kolliväli":
        if chance <= 5:
            koll1 = random.choice(nõrgemad_kollid)
            animeeri("Oi ei! Su poole jookseb " + koll1.nimi + "...\nAlgab vägev võitlus.")
            fight(koll1)
        else:
            koll1 = random.choice([muumia_inf(), hiigelrott_inf(), vampiir_inf(), hiigelämblik_inf(), koll_inf()])
            animeeri("Oi ei! Su poole jookseb " + koll1.nimi + "...\nAlgab vägev võitlus.")
            fight(koll1)
    elif asukohad[move_counter] == "Kondimägi":
        if chance <= 3:
            koll1 = random.choice(nõrgemad_kollid)
            animeeri("Tule taevas appi! Kondirusu seest ärkas üles " + koll1.nimi + "...\nAlgab vägev võitlus.")
            fight(koll1)
        else:
            koll1 = random.choice(tugevad_kollid)
            animeeri("Tule taevas appi! Kondirusu seest ärkas üles " + koll1.nimi + "...\nAlgab vägev võitlus.")
            fight(koll1)
    elif asukohad[move_counter] == "Printsessi torn":
        animeeri("Imekaunis printsess lehvitab sulle oma torni aknaaugust...\n Torni ümber lendab kolossaalne tuld sülitav draakon...\n Printsessi päästmiseks tuleb draakon maha lüüa...\n Algab vägevaim võitlus.")
        fight(boss)
        

display_the_logo()
   
tiitelleht()
tiitellehe_valikud()
käsk()

while player.mängu_staatus == False:
    käsk()
    
if player.mängu_staatus == True:
        os.system("clear")
        time.sleep(1)
        display_the_logo()
        for el in "\n\nMäng sai läbi.":
            sys.stdout.write(el)
            sys.stdout.flush()
            time.sleep(0.1)
