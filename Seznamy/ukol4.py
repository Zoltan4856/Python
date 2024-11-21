#Mějme následující seznam produktů s cenou:

""" produkty = [
  ("banán", 10),
  ("rohlík", 3),
  ("paštika", 30),
  ("hermelín", 50),
  ("chleba", 30),
  ("salám", 60),
  ("kečup", 70),
  ("eidam", 40),
  ("mandarinka", 8),
  ("okurka", 10),
] """
#Napište program, do kterého uživatel napíše název produktu a množství, které chce zakoupit daného produktu. 
# Až uživatel napíše ZAPLATIT, tak program ukončí zadávání zboží do košíku a vypíše na obrazovku celkovou cenu za nákup.

produkty = [
  ("banán", 10),
  ("rohlík", 3),
  ("paštika", 30),
  ("hermelín", 50),
  ("chleba", 30),
  ("salám", 60),
  ("kečup", 70),
  ("eidam", 40),
  ("mandarinka", 8),
  ("okurka", 10),
]

kosik = []
print(produkty)

zaplatit = True

while zaplatit is True:
    vstup = input("Vitejte v obchode co si prejete nakoupit nebo zaplatit")
    zbozi,mnozstvi = vstup.split(",")
    mnozstvi = int(mnozstvi)

    if zbozi == 'ZAPLATIT':
        print(f"celkova cen je {sum(kosik)} korun")
        zaplatit = False
        break

    najit_produkt = False

    for produkt in produkty:
        if zbozi == produkt[0]:
            pocitani = produkt[1]*mnozstvi
            kosik.append(pocitani)
            print(f"Vybrali jste {produkt} x {mnozstvi} je {pocitani} korun")
            najit_produkt = True
    if not najit_produkt:
        print("Toto zbozi neni v obchode")


