#Napište program, který najde index daného prvku v seznamu. Ošetřete případy, kdy prvek neexistuje.

#Příklad vstupu:
# Seznam čísel
cisla = [5, 3, 8, 6, 1]
print(cisla)

vstup = input("Zadejte číslo a my řekneme index: ")

num = int(vstup)

if num in cisla:
    index = cisla.index(num) 
    print(f"Číslo {num} se nachází na indexu {index}.")
else:
    print(f"Číslo {num} v seznamu není.")


