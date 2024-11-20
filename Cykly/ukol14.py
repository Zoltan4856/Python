#Napište program, který vygeneruje tabulku násobků pro zadané číslo. Použijte smyčku for k tisku tabulky od 1 do 10.

vstup = int(input("Zadejte cislo a program vygeneruje tabuulku nasobilky"))

for cisla in range(1,11):
    nasobilka = vstup * cisla
    print(f"{vstup} X {cisla} je {nasobilka}")
   
    