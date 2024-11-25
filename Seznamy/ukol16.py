#Napište program, který najde nejmenší a největší číslo v seznamu pomocí indexování a porovnání.

#Příklad vstupu:
cisla = [8, 3, 10, 6, 1]

nejvetsi = cisla[0]
nejmensi = cisla[0]


for minmax in range(len(cisla)):
    if cisla[minmax] > nejvetsi:
        nejvetsi = cisla[minmax]
    elif cisla[minmax] < nejmensi:
        nejmensi = cisla[minmax]
print(nejvetsi)
print(nejmensi)