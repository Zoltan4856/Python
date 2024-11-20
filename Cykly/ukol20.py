#Zadání: Napište Python program, který vypíše násobení zadaného čísla. Program by měl vytisknout tabulku násobení pro číslo, které uživatel zadá.


vstup = int(input("Zadejte cislo kteryho tabulku nasobilky chce videt"))


for nasobilka in range(1,10,1):
    reseni = vstup*nasobilka
    print(reseni)

