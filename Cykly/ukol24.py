#Vypočítejte třetí mocninu všech čísel od 1 do daného čísla

vstup = int(input("Zadejte cislo "))
for cislo in range(1, vstup + 1):
    print("puvodni cislo je:", cislo, " 3 mocnina je", (cislo * cislo * cislo))