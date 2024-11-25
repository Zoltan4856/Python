#Použijte stejný seznam studenti. Napište program, který:

#Vypíše první tři studenty.
#Vypíše poslední dva studenty.
#Vypíše všechny studenty kromě prvního.
studenti = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

vstup = input("napiste jestli chcete vybrat prvni tri studenty nebo posdni dva anebo vsechno krome prvniho")

if vstup == 'top3':
    print(studenti[0:3])
elif vstup == 'last2':
    print(studenti[-3:-1])
elif vstup == 'vne1':
    print(studenti[1:])
    