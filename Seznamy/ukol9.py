#Mějme seznam studentů:
studenti = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
#Napište program, který vypíše:

#Prvního studenta.
#Posledního studenta.
#Studenta na indexu 2.

vstup = input("Napiste jakou akci chcete zvolit, vypsat prvniho studenta , posledniho nebo studenta s indexem 2<")


if vstup == 'prvni':
    print(studenti[0])
elif vstup == 'posledni':
    print(studenti[-1])
elif vstup == 'index':
    print(studenti[2])
