#Realizujte algoritmus přihlašování do SIM karty. Program vás požadá o zadání správného PINu SIM karty. Na zadání máte 3 pokusy. Pokud se trefíte do správného PINu, pak vám aplikace vypíše informaci o úspěšném přihlášení do SIM karty. 
# Pokud se netrefíte, pak vás požadá o korektní zadaní. 
# Pokud se netrefíte 3x, tak aplikace vypíše informaci o zablokování SIM karty.

pokus = 3
heslo = "123456789"
while pokus > 0:
    vstup = input("Zadejte heslo")
    if vstup != heslo:
        print(f"mate spatne uvedene heslo mate {pokus} pokusu")
        pokus -= 1
        if pokus ==0:
            print("Vyprsel vas pocet pokusu mate zablokovanou sim kartu")
    else:
        print("Heslo ktery jste zadal je spravne")