#Úkol: Požádej uživatele o původní cenu zboží a procentuální slevu. Poté spočítej a vypiš cenu po aplikování slevy.

cena = float(input("zadejte cenu"))
sleva = float(input("zadejte slevu"))

final_price = cena * (1 - sleva / 100)

print(f"finalni sleva je {final_price}")