#Úkol: Napiš program, který se uživatele zeptá na počáteční částku, úrokovou sazbu a časové období v letech. 
#Poté spočítej a vypiš jednoduchý úrok pomocí vzorce:
#Jednoduchý úrok = (Počáteční částka * Sazba * Čas) / 100.

pocatecni_castka = int(input("Zadejte pocatecni castku"))
urokova_sazba = int(input("Zadejte urokovou sazba"))
cas = int(input("Zadejte cas"))

urok = pocatecni_castka*urokova_sazba*cas/100

print(urok)