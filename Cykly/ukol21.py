#Napište Python program, který spočítá celkový počet číslic v zadaném čísle.

vstup = int(input("Zadejte cislo a my spocitam kolik cislic tam je"))
    
pocet = 0
while vstup != 0:
    vstup = vstup // 10

    pocet = pocet + 1
print("Total digits are:", pocet)


