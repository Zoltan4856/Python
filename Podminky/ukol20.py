#zade je to prvocislo

cislo = int(input("Zadejte číslo: "))

# Pokud je číslo menší než 2, není to prvočíslo
if cislo <= 1:
    print(f"{cislo} není prvočíslo.")
# Pokud je číslo 2, je to prvočíslo
elif cislo == 2:
    print(f"{cislo} je prvočíslo.")
# Pokud je číslo dělitelný 2, není to prvočíslo
elif cislo % 2 == 0:
    print(f"{cislo} není prvočíslo.")
# Pokud je číslo dělitelný 3, není to prvočíslo
elif cislo % 3 == 0:
    print(f"{cislo} není prvočíslo.")
# Pokud je číslo dělitelný 5, není to prvočíslo
elif cislo % 5 == 0:
    print(f"{cislo} není prvočíslo.")
# Pokud je číslo dělitelný 7, není to prvočíslo
elif cislo % 7 == 0:
    print(f"{cislo} není prvočíslo.")
# Pokud číslo není dělitelné žádným z výše uvedených čísel, je to prvočíslo
else:
    print(f"{cislo} je prvočíslo.")
