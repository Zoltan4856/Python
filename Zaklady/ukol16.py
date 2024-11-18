#Úkol: Napiš program, který se uživatele zeptá na základnu a výšku trojúhelníku. Poté spočítej a vypiš obsah trojúhelníku podle vzorce:

základna = float(input("Zadejte základnu trojúhelníku: "))
výška = float(input("Zadejte výšku trojúhelníku: "))


obsah = (základna * výška) / 2


print(f"Obsah trojúhelníku je: {obsah:.2f}")
