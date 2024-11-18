#Úkol: Napiš program, který požádá uživatele o číslo a exponent, poté vypočítá a vypíše výsledek (tj. číslo umocněné na zadaný exponent).

hodnota1 = int(input("zadejte cislo"))
hodnota2 = int(input("zadejte exponent"))

umocneni = hodnota1**hodnota2

print(f"exponent {hodnota2} s cislem {hodnota1} je {umocneni}")