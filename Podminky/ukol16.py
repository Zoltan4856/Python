#Napište program, který zjistí, zda je dané číslo dokonalým čtvercem. 
# Číslo je dokonalý čtverec, 
# pokud existuje celé číslo n, pro které platí n * n = dané číslo.

import math

cislo = int(input("Zadejte číslo: "))

# Spočítáme druhou odmocninu
odmocnina = math.sqrt(cislo)

# Zkontrolujeme, zda je odmocnina celé číslo
if odmocnina == int(odmocnina):
    print(f"{cislo} je dokonalý čtverec.")
else:
    print(f"{cislo} není dokonalý čtverec.")


