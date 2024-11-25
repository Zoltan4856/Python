#Napište program, který spočítá součet prvků na sudých indexech v seznamu.

#Příklad vstupu:
cisla = [5, 10, 15, 20, 25]

soucet = 0

for sude_indexy in range(len(cisla)):
    if sude_indexy % 2 ==0 :
        soucet += cisla[sude_indexy]
print(soucet)

