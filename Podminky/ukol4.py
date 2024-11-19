#Sportka Napište program, který kontroluje výherní los. Uživatel zadá na klávesnici číslo svého losu a pokud jeho los vyhrál ve sportce, tak se vypíše hláška na obrazovku o vítězství.
#Ve sportce se losuje jen jedna číslice a to od 1 do 9. Los má také jen jednu číslici. 
#Pro generování náhodného čísla použijte knihovnu random a její příkaz randint(min, max), kde min a max jsou rozmezí generování náhodného čísla.
#
import random

vyherni_los = random.randint(1,9)

vstup = int(input("Zadejte svuj vyherni cislo od 1,9"))

if vstup != vyherni_los:
    print("bohuzl jste prohral")
elif vstup == vyherni_los:
    print("gratuluji ")