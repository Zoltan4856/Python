#Úkol: Napiš program, který se uživatele zeptá na teplotu v Celsiích, potom ji převede na Fahrenheit podle vzorce:
#Fahrenheit = (Celsius * 9/5) + 32.
#Vypiš výsledek.

hodnota = float(input("zadejte kolik je stupnu"))

celsius = hodnota
celsius = float(celsius)

farenheit = (celsius*9/5)+32
print(f"aktualne je{hodnota} a ve Fahreheitech {farenheit} stupnu5")