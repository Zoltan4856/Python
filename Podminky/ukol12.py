#Napište program, který přiřadí písmenou známku podle skóre.

vstup = int(input("Zadejte vase skore "))

if vstup < 0:
    print("zadali jste spatne cislo")
else:
    if vstup >= 90 :
        print("Mate znamku A")
    elif vstup >=80 and vstup <=89 :
        print("Mate znamku B")
    elif vstup >=70 and vstup <=79 :
        print("Mate znamku C")
    elif vstup >=60 and vstup <=69 :
        print("Mate znamku D")
    else:
        print("Mate F")