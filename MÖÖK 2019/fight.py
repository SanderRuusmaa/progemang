from random import randint
from time import sleep
import sys
import time

class player_inf():
    def __init__(self):
        self.mängu_staatus = False
        self.nimi = ""
        self.hp = 100
        self.gold = 20
player = player_inf()

class koll_inf():
    def __init__(self):
        self.nimi = "Koll" 
        self.nimiOm = "Kolli"
        self.NimiOs = "Kolli"
        self.hp = 100
        self.dmg = 10
        self.weakness = "lõikav"
        auhind = 50

class hiidämblik_inf():
    def __init__(self):
        self.nimi = "Hiidämblik" 
        self.nimiOm = "Hiidämbliku"
        self.NimiOs = "Hiidämblikku"
        self.hp = 20
        self.dmg = 4
        self.weakness = "purustav"
        auhind = 5

class hiigelämblik_inf():
    def __init__(self):
        self.nimi = "Hiigelämblik" 
        self.nimiOm = "Hiigelämbliku"
        self.NimiOs = "Hiigelämblikku"
        self.hp = 60
        self.dmg = 8
        self.weakness = "lõikav"
        auhind = 25

class harpüia_inf():
    def __init__(self):
        self.nimi = "Harpüia" 
        self.nimiOm = "Harpüia"
        self.NimiOs = "Harpüiat"
        self.hp = 15
        self.dmg = 5
        self.weakness = "kaugrünnak"
        auhind = 5

class zombi_inf():
    def __init__(self):
        self.nimi = "Zombi" 
        self.nimiOm = "Zombi"
        self.NimiOs = "Zombit"
        self.hp = 10
        self.dmg = 3
        self.weakness = "suskav"
        auhind = 2

class draakon_inf():
    def __init__(self):
        self.nimi = "Draakon" 
        self.nimiOm = "Draakoni"
        self.NimiOs = "Draakonit"
        self.hp = 250
        self.dmg = 25
        self.weakness = "lõikav", "kaugrünnak"
        auhind = 200

class vampiir_inf():
    def __init__(self):
        self.nimi = "Vampiir" 
        self.nimiOm = "Vampiiri"
        self.NimiOs = "Vampiiri"
        self.hp = 20
        self.dmg = 4
        self.weakness = "purustav"
        auhind = 5

class vampiir_inf():
    def __init__(self):
        self.nimi = "Vampiir" 
        self.nimiOm = "Vampiiri"
        self.NimiOs = "Vampiiri"
        self.hp = 20
        self.dmg = 4
        self.weakness = "purustav"
        auhind = 5

class rott_inf():
    def __init__(self):
        self.nimi = "Rott" 
        self.nimiOm = "Roti"
        self.NimiOs = "Rotti"
        self.hp = 5
        self.dmg = 2
        self.weakness = "purustav"
        auhind = 1

class mõõk_inf():
    def __init__(self):
        min_dmg = 2
        dmg = 5
        miss = 10 # 10% võimalus, et rünnak ei lähe üldse läbi
        crit = 20 # Võimalus teha topeltdamage
        supercrit = 1 #Võimalus teha kolmekordselt damage'it
        type = "lõikav"

class nui_inf():
    def __init__(self):
        self.min_dmg = 3
        self.dmg = 8
        self.miss = 10
        self.crit = 5
        self.supercrit = 1
        self.type = "purustav"

class vibu_inf():
    def __init__(self):
        self.min_dmg = 2
        self.dmg = 4
        self.miss = 30
        self.crit = 10
        self.supercrit = 5
        self.type = "kaugrünnak"

class nuga():
    def __init__(self):
        self.min_dmg = 1
        self.dmg = 3
        self.miss = 5
        self.crit = 50
        self.supercrit = 10
        self.type = "suskav"

class vikat():
    def __init__(self):
        self.min_dmg = 1
        self.dmg = 5
        self.miss = 20
        self.crit = 5
        self.supercrit = 1
        self.type = "kaugrünnak", "lõikav"

class sõjahaamer():
    def __init__(self):
        self.min_dmg = 2
        self.dmg = 10
        self.miss = 20
        self.crit = 12.5
        self.supercrit = 1
        self.type = "purustav"

class amb():
    def __init__(self):
        self.min_dmg = 5
        self.dmg = 15
        self.miss = 30
        self.crit = 5
        self.supercrit = 2
        self.type = "kaugrünnak"

class piits():
    def __init__(self):
        self.min_dmg = 1
        self.dmg = 4
        self.miss = 2
        self.crit = 3
        self.supercrit = 1
        self.type = "lõikav"

class oda():
    def __init__(self):
        self.min_dmg = 3
        self.dmg = 10
        self.miss = 15
        self.crit = 5
        self.supercrit = 1
        self.type = "lõikav"

class viskeoda():
    def __init__(self):
        self.min_dmg = 4
        self.dmg = 6
        self.miss = 40
        self.crit = 5
        self.supercrit = 1
        self.type = "kaugrünnak"

koll = draakon_inf()
relv = nui_inf()

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
           "Oskus lasta kaksüks kord rohkem korraga" : [30,False],
           "Oskus lasta üks kord rohkem korraga": [50,False],
           "Oskus võitluse käigus relva vahetada": [15,False],
           "Oskus juua võlujooki käiku raiskamata": [15,False],
           "Oskus alati võitlusest põgeneda": [40,False]}

def shop():
    print("Tere! ", end="")
    while True:
        valik = input("Mida soovite osta? Kui relvi, siis kirjutage \"relvad\", kui rüüsid, kirjutage \"rüüd\", kui võlujooke, kirjutage \"võlujoogid\", kui oskuseid, kirjutage \"oskused\", kui soovite poest lahkuda, kirjutage \"lahku\": ")
        sleep(0.5)
        if valik == "relvad":
            print("\nAh et soovite meie kvaliteetseid relvi vaadata! Siin on meie valik:")
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
            print("\nMa näen, et teid huvitab meie rüükollektsioon! Heitke pilk peale ja laduge raha lauale! Siin on valikud:")
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
            print("\nNäen, et imetlete meie võlujooke. Need kõik võivad olla teie, kui te vaid maksate! Siin on meie valik:")
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
            print("\nNäen, et uurite meie intensiivse treeningu kava. Paremaid võitlusoskuseid kui meiega ei saa te kuskil kuningriigis! Siin on meie programmid:")
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
            print("Lahkusite poest.")
            break
        else:
            pass

shop()

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


#fight(koll)