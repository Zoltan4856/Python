#Úkol: Zeptej se uživatele na tři čísla, poté spočítej a vypiš jejich průměr.

cisla = input("zadejte tri cislo oddene carkou")

prvni_cislo, druhe_cislo, treti_cislo = cisla.split(',')
prvni_cislo = int(prvni_cislo)
druhe_cislo = int(druhe_cislo)
treti_cislo = int(treti_cislo)
soucet = prvni_cislo + druhe_cislo + treti_cislo 
prumer = int(soucet)/3

print(f"prumer hontot {prvni_cislo} {druhe_cislo} {treti_cislo} se rovna {prumer} a soucet {soucet}")
