Mäng töötab bash shellis. Windows OS arvutiga on vaja läbida järgnevad sammud, enne kasutamist:
-Otsida Control Panelist või alt otsingu rea pealt "Windows Features", sealt lisa linnuke "Windows Subsystem for Linux"
-Microsoft store-ist alla alladida "Ubuntu"
-Kirjutad windowsi otsinugsse "bash", peaks avanema, ootad kuni ära installib jne


-Käsud navigeerimiseks:
	- cd (change directory)
	- cd .. (liigud ühe sammu võrra tagasi)
	- cd / (saad root directory)
	- ls (näed, mis praegu folderis on)


-Et saada MÖÖK 2019 juurde ja käivitada mäng (kui see asub teie Desktopil), (Puðkin: kui asub Documents folderis):
	kui DESKTOPIL
	-cd /mnt/c/users/"SINU WINDOWSI KASUTAJANIMI"/desktop/"MÖÖK 2019"
	-python3 möök.py

	kui GitHubi folderis
	-cd /mnt/c/users/"SINU WINDOWSI KASUTAJANIMI"/documents/github/progemang/"MÖÖK 2019"
	-python3 möök.py