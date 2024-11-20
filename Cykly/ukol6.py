#Napište program, který v kolekci obsahuje seznam maturitních otázek. Poté se spustí cyklus, který se opakuje do té doby, dokavaď v seznamu nějaká otázka zbývá. 
# Kdykoliv uživatel zmáčkně klávesu ENTER, tak program jednu z otázek náhodně vylosuje a vypíše na obrazovku. Otázky budou voleny náhodně. 
# Podívejte se do modulu random, jaké by funkce by se vám mohly hodit pro tento účel.
import random

seznam = ['Matika','Fyzika','Technika']



while seznam:
    vstup = input("Zmacknete ENTER aby se vylosovala nahodna maturitnu otazka")
    nahoda = random.choice(seznam)
    seznam.remove(nahoda)
    print(f"Vylosvali jste {nahoda}")
    print(f"zbyva otazek {seznam}")
    if not seznam :
        print("Dosly otazky")
