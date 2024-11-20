#Upravte váš kód na kámen-nůžky-papír z předchozího cvičení na verzi hry, ve které vyhrává hráč nebo počítač až po dvou vítězných kolech


import random


vyherne = 0
proherne = 0
while vyherne < 2 and proherne < 2:
    ai = random.choice(('kamen','nuzky','papir'))
    vstup = input("Kamen nuzky papir")
    if vstup not in ('kamen','nuzky','papir'):
        print("Nezadali jste spravne neco")
    else:
        if vstup == ai:
            print(f"Oba dva jste dali{ai} dejte jeste jedno kolo")
        elif    (vstup == 'kamen' and ai == 'nuzky') or \
                (vstup == 'nuzky' and ai == 'papir') or \
                (vstup == 'papir' and ai == 'kamen'):
            print(f'Vyhrali jste zkuste to jeste')
            vyherne +=1
            if vyherne == 2:
                print("vyhrali jste ")
        else:
            print(f"Prohrali jste zkuste to jeste ")
            proherne +=1
            if proherne == 2:
                print("Prohrali jste")
        