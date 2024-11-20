#Napište program, který neskončí dokavaď nezadáá uživatel ze standardního vstupu číslo, které po přetypování nevyhodí chybu.



while True:
    vstup = input("Zadejte cislo")
    try:
        cislo = int(vstup)
        print(f"Je to cislo {cislo}")
        break
    except ValueError:
        print("TOTO NENI CISLO  ")