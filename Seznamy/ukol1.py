#Vytvořte seznam ntic, který naplňte dvojicemi (jméno, počet samohlásek ve jméně). Jména jsou zadaná v předpřipraveném seznamu. Použijte k tomu metodu count.

jména = ["Pavel", "Milan", "Alena", "Rostislavomir"]
samohlasky_kratke = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
reseni = []

for jmeno in jména:

    pocet_samohlasek = 0
    for pismeno in jmeno:
        if pismeno in samohlasky_kratke:
            pocet_samohlasek += 1
    reseni.append((jmeno, pocet_samohlasek))

print(reseni)
