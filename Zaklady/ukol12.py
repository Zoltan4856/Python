#Úkol: Zeptej se uživatele na dvě čísla a vypiš zbytek po dělení prvního čísla druhým.
num1 = int(input("Zadej prvni cislo"))
num2 = int(input("Zadej drhe cislo"))
remainder = num1 % num2
print("zbytek", num1, "s", num2, "je:", remainder)
