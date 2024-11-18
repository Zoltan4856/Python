#Úkol: Požádej uživatele o počet sekund, poté je převeď na minuty a sekundy. Vypiš výsledek ve formátu "x minut y sekund".

hodnota1 = int(input("zadejte hodiny"))
hodnota2 = int(input("zadejte minuty"))
hodnota3 = int(input("zadejte sekundy"))

minutes = 60
seconds = 60
hodina = hodnota1
minuta = hodnota2
sekunda = hodnota3

prevod_hodiny = hodina*minutes*seconds
prevod_minuty = minuta*seconds
celkem = prevod_hodiny+prevod_minuty+sekunda

print(f"v {hodnota1} hodin a {hodnota2} minut a {hodnota3} sekund je {celkem} sekund")
