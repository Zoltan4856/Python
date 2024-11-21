#Napište program, který přijme ze standardního vstupu různá slova. Program přestane přijímat slova, jakmile uživatel napíše slovo STOP. 
# Poté se na obrazovku vypíše seznam písmenek bez duplicit, která všechny slova obsahovala. K smazaní duplicit využijte množinu. Příklad:
#zadano = ["pavel", "hromada", "traktor"]
#vysledek = ["p", "a", "v", "e", "l", "h", "r", "o", "m", "d", "t", "k"]


stop = True

seznam_pismen = set([])

while stop :
    vstup = input("Zadejte slova jestli chce ukoncit napiste 'STOP' ")
    if vstup == 'STOP':
       stop = False
       break 
    else:
        for pismena in vstup:
            seznam_pismen.add(pismena)
print(sorted(seznam_pismen))