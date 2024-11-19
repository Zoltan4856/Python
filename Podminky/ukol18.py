#Napište program, který najde největší ze tří čísel. Nepoužívejte vestavěnou funkci max(). Musíte použít if, elif a else.

vstup = input("Zadejte 3 cisla ")

prvni_cislo,druha_cislo,treti_cislo = vstup.split(',')

prvni_cislo = int(prvni_cislo)
druha_cislo = int(druha_cislo)
treti_cislo = int(treti_cislo)

# Porovnáme, které číslo je největší
if prvni_cislo > druha_cislo and prvni_cislo > treti_cislo:
    print(f"{prvni_cislo} je největší")
elif druha_cislo > prvni_cislo and druha_cislo > treti_cislo:
    print(f"{druha_cislo} je největší")
elif treti_cislo > prvni_cislo and treti_cislo > druha_cislo:
    print(f"{treti_cislo} je největší")
else:
    print("Některá čísla jsou si rovna.")
