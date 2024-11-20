#Napište program, kde uživatel hádá náhodné číslo v rozmezí od 1 do nějaké maximální meze. Na začátku je maximální mez nastavena na hodnotu 2.
#  S každým uhádnutým číslem se mez zvětšuje o jedna, takže pokud uživatel v prvním kole číslo uhádne, tak v příštím kole již hádá mezi 1 a 3. 
# Pokud uživatel číslo neuhádně, tak hádáná hodnota musí zůstat stejná a uživatel jen dostane nápovědu, jestli musí hádat číslo nižší nebo vyšší. 
# Uživatel má 3 životy, které pokud dojdou, tak hra končí. 
# Po ukončení hry se na obrazovku vypíše nějakým vhodným způsobem vypočítané skóre.

import random
vrchni_limit = 2
nahoda = random.randint(1,vrchni_limit)
zivoty = 3

while zivoty > 0:
    vstup = input("Zadejte cislo  snad to uhodnete")
    
    try:
        vstup = int(vstup) 
    except ValueError:
        print("Spatne zadanej format! Zadejte cislo.")
        continue 
    if vstup == nahoda:
        print("Jste uhodli cislo")
        vrchni_limit +=1
    elif vstup > nahoda:
        print(f"Nauhadnul jste mate jeste {zivoty} pokusu zkuste uhadnout mensi cislo ")
        zivoty -=1
    
    elif vstup <nahoda:
        print(f"Nauhadnul jste mate jeste {zivoty} pokusu zkuste uhadnout vetsi cislo ")
        zivoty -=1
    elif zivoty == 0:
        print("Pohrali jste")
        
