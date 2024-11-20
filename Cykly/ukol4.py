#Napište program, který bude žádat uživatele o zadávání číselných dat z klávesnice do té doby, dokavaď nenapíše řetězec STOP. Poté vypíše na obrazovku aritmetický průměr z hodnot. 
# Přidávání do kolekce se provádí příkazem append. Na začátku si budete muset vytvořit prázdnou kolekci.

stop = 10
seznam = []
while stop > 0:
    vstup = int(input("Zadejte cislo"))
    seznam.append(vstup)
    stop -=1
    if stop ==0:
        prumer = sum(seznam)/len(seznam)
        print(f"prumer{prumer}")