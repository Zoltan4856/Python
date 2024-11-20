#Napište program, který sečte všechna čísla v zadaném rozsahu. Uživatel zadá hodnotu pro začátek a konec rozsahu. Použijte smyčku for.

vstup = input("zadejte rozmezi cisel a program to spocita")

prvni_cislo, druhe_cislo = vstup.split(',')
prvni_cislo = int(prvni_cislo)
druhe_cislo = int(druhe_cislo)
seznam = []
for rozmezi in range(prvni_cislo,druhe_cislo):
   seznam.append(rozmezi)
pocitani = sum(seznam)
print(f"Soucet cisel {seznam} je {pocitani}")