#Jednoducha cviceni na for loop dava to do projektu kvuli tomu abych tu nespamoval commity :p take takhle je to vic komplexni
#Vypište čísla od 1 do 10. ---
#Použijte range a for cyklus k výpisu čísel od 1 do 10.


#Vypište sudá čísla od 2 do 20. 
#pomocí for cyklu a podmínky vypište sudá čísla.

#Vypište všechna čísla od 1 do 50 dělitelná 5.

#Sečtěte čísla od 1 do 100.
#Použijte proměnnou pro ukládání součtu.

#Vytvořte násobky čísla 3.
#Vypište prvních 10 násobků čísla 3.


vstup = input("Zadejte rozmezi cisel a taky zvolete operaci, vypsat, suda, cisla delitalna 5, secist anebo vypsat nasobky cisla 3")


#Definovani hodnot
operace, prvni_cislo, druhe_cislo = vstup.split(',')
prvni_cislo = int(prvni_cislo)
druhe_cislo = int(druhe_cislo)


#seznamy
seznam = []
#vypsani rozmezi cisel

if operace == 'vypsat':
    print("Vybrali jste vypsani vsech cisel")
    for vypsani in range(prvni_cislo,druhe_cislo):
        seznam.append(vypsani)
    print(seznam)

#Suda cisla :p

elif operace == 'suda':
    print("Vybrali jste vypis vsechn sudych cisel")
    for vypis_sudych_cisel in range(prvni_cislo,druhe_cislo):
        if vypis_sudych_cisel % 2 == 0:
            seznam.append(vypis_sudych_cisel)
    print(seznam)

#Delitelna 5

elif operace == 'delitelna5':
    print("Vybrali jste cisla s nasobkem 5")
    for vypiscisel_delitelnych_peti in range(prvni_cislo,druhe_cislo):
        if vypiscisel_delitelnych_peti % 5 ==0:
            seznam.append(vypiscisel_delitelnych_peti)
    print(seznam)
#secist
elif operace == 'secist':
    print("Secteme to")
    for secist in range(prvni_cislo,druhe_cislo):
        seznam.append(secist)
    reseni = sum(seznam)
    print(reseni)
elif operace == 'delitelna3':
    print("Vynasobime to 3")
    for vynasob in range(prvni_cislo,druhe_cislo):
        if vynasob % 3 ==0:
            seznam.append(vynasob)
    print(seznam)