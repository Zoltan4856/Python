#Středně pokročilá cvičení


#Vypište písmena slova "Python a najdi pocet samohlasek ".

#Sečtěte všechny sudé hodnoty v seznamu [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

#Zjistěte největší číslo v seznamu [15, 22, 8, 19, 31].

#Převraťte řetězec a pak to srovnejste zda je palindrom.

#Vypište násobící tabulku (1–10) pro číslo zadané uživatelem.


print(
    "Vítejte v programu, který nabízí několik užitečných funkcí:\n"
    "- Pokud chcete analyzovat větu (např. spočítat krátké ), napište 'Analyza'.\n"
    "- Dokážeme také sečíst všechny sudé hodnoty, které zadáte, nebo zjistit největší číslo.\n"
    "- Můžeme převrátit řetězec, nebo vypsat tabulku násobení."
)

vstup = input("Prosim uvedte zda chce resit matematicka ci vetevne ulohy")
seznam = []

if vstup == 'jazyk':
    vstup1 = input("Prosim napiste funki, analyza, prevratit,jestli ani jedna napiste next ")
    samohlasky_kratke = ['A','E','I','Y','O','U','a', 'e', 'i', 'y', 'o', 'u']
    operace, vety = vstup1.split(',')
    if operace == 'analyza':
        print("Tady mate pocet analyzace vety ")
    for slova in vety:
        if slova in samohlasky_kratke:
            seznam.append(slova)
    
    pocitadlo = len(seznam)
    print(f"Pocet kratkych samohlasek cini {pocitadlo}")
    if operace == 'reverse':
        print("Obrtili jste celou vetu")
        obratit = vety[::-1]
        if vety == obratit:
            print(f"Je to palindrom")
        else:
            print(f"slovo {vety} neni palindrom")
elif vstup == 'matika':
    vstup2 = input("Prosim napiste jestli chtete secist vsechny sude hodnoty secist anebo najit nejmensi nebo nejvetsi cislo minmax anebo chtete vygenerovat abulku nasobeni")
    operace2,prvni_cislo,druhe_cislo = vstup2.split(',')

    prvni_cislo = int(prvni_cislo)
    druhe_cislo = int(druhe_cislo)

    nekonecnemalo = float('inf')
    nekonecnemnoho = float('-inf')

    if operace2 == 'sude':
        print("Vypiseme sude a nasledovne secte je mezi sebou")
        for sude_cislo in range(prvni_cislo,druhe_cislo):
            if sude_cislo % 2 == 0:
                seznam.append(sude_cislo)
        reseni2 = sum(seznam)
        print(f"tady mate seznam sudych cisel {seznam}")
        print(f"tady mate soucet sudych cisel {reseni2}")

    elif operace2 == 'minmax':
        print("najdeme nejmensi a nejvetsi cislo")         
        for minmax in range(prvni_cislo,druhe_cislo):
            if minmax < nekonecnemalo:
                nekonecnemalo = minmax
            elif minmax > nekonecnemnoho:
                nekonecnemnoho = minmax
        print(f"nejmensi cislo je {nekonecnemalo} a nejvetsi je {nekonecnemnoho}")

    elif operace2 == 'nasobilka':
        for tabulka in range(1,druhe_cislo+1):
            reseni3 = prvni_cislo*tabulka
            print(f"{prvni_cislo} X {tabulka} = {reseni3}")
