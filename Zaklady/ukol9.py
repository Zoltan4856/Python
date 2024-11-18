#Úkol: Napiš program, který se uživatele zeptá na dvě čísla a prohodí jejich hodnoty. 
#Vypiš hodnoty obou proměnných po prohození.

cislo1 = int(input("zadejte prvni cislo"))
cislo2 = int(input("zadejte druhe cislo"))

zmena = cislo1,cislo2 = cislo2,cislo1
print(f"cisla jsou opravdu prohozene{zmena}")
