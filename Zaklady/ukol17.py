#Úkol: Požádej uživatele, aby zadal číslo, a vypiš ho zaokrouhlené na dvě desetinná místa.

hodnota = float(input("Zadejte číslo: "))

zaokrouhlene = round(hodnota, 2)

print("Zaokrouhlené číslo:", zaokrouhlene)
