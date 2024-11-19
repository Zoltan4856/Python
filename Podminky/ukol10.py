#Napište program, který zjistí, zda je zadané číslo kladné, záporné nebo nula.

vstup = int(input("napiste cislo"))

if vstup < 0:
    print("cislo je zaporne ")
elif vstup > 0:
    print("cislo he kladne ")
elif vstup ==0: 
    print("cislo je 0")