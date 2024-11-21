#Mějme seznam hráčů a jejich nahrané skóre ve hře:

#hraci = [("Pavel", 5), ("Honza", 3), ("Jana", 7), ("Milan", 4), ("Michaela", 9)]
#Vypište na obrazovku jméno nejlepšího a nejhoršího hráče podle skóre.
#Mějme seznam hráčů a jejich nahrané skóre ve hře:

#hraci = [("Pavel", 5), ("Honza", 3), ("Jana", 7), ("Milan", 4), ("Michaela", 9)]
#Vypište na obrazovku hráče v pořadí od nejlepšího po nejhoršího a jen ty nejlepší 3 (top-3).


hraci = [("Pavel", 5), ("Honza", 3), ("Jana", 7), ("Milan", 4), ("Michaela", 9)]


print(hraci)
vstup = input("vitejte tento program umi 3 funkce, Vpsat od nejlepsiho k nejhorsimu anebo k tomu jenom top3 ")

sorted_hraci = sorted(hraci, key=lambda x: x[1], reverse=True)


if vstup == 'topdown':
    print(f"Nejlepsi hrac je {sorted_hraci[0][0]} se skore {sorted_hraci[0][1]}")
    print(f"Nejlepsi hrac je {sorted_hraci[-1][0]} se skore {sorted_hraci[-1][1]}")

elif vstup == 'maxmin':
    for hrac in sorted_hraci:
        print(f"{hrac[0]} se skore {hrac[1]}")
elif vstup =='top3':
    top3 = sorted_hraci[:3]
    print(f"{sorted_hraci[0]} se skore {sorted_hraci[1]}")