#Napište program, který zjistí, zda je zadané číslo dělitelné jak 3, tak 5.

#Vstup: 15
#Výstup: Číslo je dělitelné 3 i 5


vstup = int(input("Zadejte cislo"))

if vstup % 3 ==0 and vstup % 5 ==0:
    print("cislo je delitelne 3 a 5") 
else:
    print("cislo neni delitelne 3 a 5")
    