#Zde je Python program, který zobrazuje pouze ta čísla z daného seznamu, která splňují následující podmínky:

#Číslo musí být dělitelné pěti.
#Pokud je číslo větší než 150, přeskočíme ho a pokračujeme na následující číslo.
#Pokud je číslo větší než 500, ukončíme smyčku.

seznam = [12, 75, 150, 180, 145, 525, 50]

for najit_cislo in seznam:
    if najit_cislo >500:
        break
    elif najit_cislo >150:
        continue
    elif najit_cislo % 5 == 0:
        print(najit_cislo)
