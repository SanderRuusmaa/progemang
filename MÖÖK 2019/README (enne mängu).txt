M�ng t��tab bash shellis. Windows OS arvutiga on vaja l�bida j�rgnevad sammud, enne kasutamist:
-Otsida Control Panelist v�i alt otsingu rea pealt "Windows Features", sealt lisa linnuke "Windows Subsystem for Linux"
-Microsoft store-ist alla alladida "Ubuntu" V�I mine siia https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab
-Kirjutad windowsi otsinugsse "bash", peaks avanema, ootad kuni �ra installib jne


-K�sud navigeerimiseks:
	- cd (change directory)
	- cd .. (liigud �he sammu v�rra tagasi)
	- cd / (saad root directory)
	- ls (n�ed, mis praegu folderis on)


-Et saada M��K 2019 juurde ja k�ivitada m�ng (kui see asub teie Desktopil), (Pu�kin: kui asub Documents folderis):
	kui DESKTOPIL
	- cd /mnt/c/users/"SINU WINDOWSI KASUTAJANIMI"/desktop/"M��K 2019"
	- python3 m��k.py

	kui GitHubi folderis
	- cd /mnt/c/users/"SINU WINDOWSI KASUTAJANIMI"/documents/github/progemang/"M��K 2019"
	- python3 m��k.py

	ET COPY PASTEIDA SIIT BASH TERMINALI, selectid k�su, CTRL+C ja bashis vajutad paremat hiire kl�psu


Et macOS-il t����le saada:
	-ava terminal ja installi python3 j�rgnevate commadidega
	- /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	- brew install python3