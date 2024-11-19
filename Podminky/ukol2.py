#Napište program, který realizuje jedno kolo hry kámen-nůžky-papír. Hráč volí mezi třemi symboly (kámen, nůžky, papír) pomocí standardního vstupu. 
#Protihráčem je umělá inteligence, která vybírá symboly náhodně. 
#Vypište na obrazovku informační hlášku o tom, kdo si vybral jaký symobl a jak kolo hry dopadlo.
#
import random

nahoda = random.choice(('kamen','nuzky','papir'))
volba = input("zvolte kamen,nuzky anebo papir").lower()

if volba not in ('kamen', 'nuzky', 'papir'):
    print("Neplatná volba. Zvolte prosím 'kamen', 'nuzky' nebo 'papir'.")
else:
    # Determine the result
    if nahoda == volba:
        print(f"Remíza! AI zvolil {nahoda}.")
    elif (nahoda == 'kamen' and volba == 'nuzky') or (nahoda == 'nuzky' and volba == 'papir') or (nahoda == 'papir' and volba == 'kamen'):
        print(f"Jste prohrál! AI zvolil {nahoda}.")
    else:
        print(f"Jste vyhrál! AI zvolil {nahoda}.")


