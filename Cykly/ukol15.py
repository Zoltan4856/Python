#Napište program, který vypočítá faktoriál čísla zadaného uživatelem. Použijte smyčku while.

vstup = int(input("napiste cislo a porgram vypicse faktorial"))
zacatek_faktorialu = 1
for cislo in range(1,vstup+1):
    zacatek_faktorialu = zacatek_faktorialu*cislo
print(f"faktorial cisla {vstup} je {zacatek_faktorialu}")