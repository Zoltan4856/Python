#Zadání: Napište Python program, který pomocí smyčky for vypíše následující obrácený číselný vzorec:

#Zkopírovat kód
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1


for cisla in range(5, 0, -1):
    for cislo in range(cisla, 0, -1):
        print(cislo, end=" ")
    print()
