#Hra na hádání čísla
#Cíl hry: Počítač si náhodně vybere číslo v určitém rozsahu a uživatel se pokusí toto číslo uhodnout. Po každém pokusu mu počítač řekne, zda je číslo větší, menší nebo správné.

#Jak to napsat:

#Počítač si náhodně zvolí číslo mezi 1 a 100.
#Uživatel zadá svůj tip.
#Počítač porovná tip uživatele s číslem a poskytne zpětnou vazbu ("Zkuste vyšší číslo", "Zkuste menší číslo", nebo "Správně!").
#Použiješ if, elif a else k rozhodnutí, zda tip je vyšší, nižší nebo správný.

import random

nahodne_cislo = random.randrange(1,100)

print(nahodne_cislo)