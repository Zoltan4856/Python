#Systém pro určení daňové sazby podle příjmu
#Popis projektu: Vytvoř systém pro výpočet daňové sazby na základě příjmu uživatele. Tento systém bude používat podmínky k určení, do které daňové kategorie příjem patří, a podle toho vypočítá výši daně.

#Předpoklady:

#Pokud příjem je méně než 100 000 Kč, daňová sazba je 10%.
#okud příjem je od 100 000 Kč do 300 000 Kč, daňová sazba je 15%.
#Pokud příjem je více než 300 000 Kč, daňová sazba je 20%.
#Technická implementace: Použijeme podmínky k určení daňové sazby a následně spočítáme, kolik daně uživatel zaplatí na základě příjmu.


vstup = int(input("Zadejte vas prijem"))

nizky_prijem = 100000
stredni_prijem = 300000


if vstup <= nizky_prijem :
    
  reseni = vstup * (10 / 100)
  print(f"Danova sazna je 10% tedy dan bude {reseni} korun")
elif vstup >= nizky_prijem and vstup <= stredni_prijem:
   reseni1 = vstup * (15/100)
   print(f"Danova sazna je 15% tedy dan bude {reseni1} korun")
else:
   reseni2 = vstup * (20/100)
   print(f"Danova sazna je 20% tedy dan bude {reseni2} korun")
