#Napište program, který zjistí, zda je zadaný rok přestupný. 
# Přestupný rok je dělitelný 4, ale není dělitelný 100, pokud není dělitelný také 400.

vstup = input("Zadejte rok")

vstup = int(vstup)
if (vstup % 4 == 0 and vstup % 100 != 0) or vstup % 400 == 0:
    print("Rok je prestupny")
else:
    print("Rokj je neprestupny")