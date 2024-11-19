#Napište program, který zjistí, zda je zadané číslo sudé nebo liché.

vstup = int(input("Zadejte cislo "))

if vstup % 3 != 0:
    print("cislo je sude")
else:
    print("cislo je liche")