#Úkol: Zeptej se uživatele na cenu zboží a sazbu DPH. Poté spočítej a vypiš celkovou cenu (cena + daň).
cena_zbozi = int(input("Zadejte cenu zbozi"))
sazba_DPH = int(input("Zadejte sazbu DPH"))

desetine_cislo = sazba_DPH/100

celkova_cena = cena_zbozi * (1 + desetine_cislo)
print(f"celkova cena({cena_zbozi}) s pridanou sazbou DPH({sazba_DPH}) cini{celkova_cena}korun")

