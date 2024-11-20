#Zadání je následující: Napište Python kód, který vytiskne následující vzorec čísel pomocí smyčky:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

radky = 5

for cisla in range(1, radky + 1, 1):
    
    for cislo in range(1, cisla + 1):
        print(cislo, end=' ')
    # empty line after each row
    print("")