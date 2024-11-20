#Zadání: Napište Python program, který přijme číslo od uživatele a vypočítá součet všech čísel od 1 do zadaného čísla.



vstup = int(input("Zadejte cislo a spocitame soucet"))

seznam = []


for soucet in range(1,vstup):
    seznam.append(soucet)
    
print(seznam)
soucet = sum(seznam)
print(f"soucet je {soucet}")
