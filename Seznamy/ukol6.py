#Napište program, do kterého uživatel zadá seznam studentů ze standardního vstupu a počet skupin, na které chce studenty rozdělit. 
# Program ze seznamu studentů následně vytvoří seznam ntic, kde ntice bude tak velká, jako je vypočítaná velikost skupiny podle požadovaného počtu skupin. 
# Počet lidí ve skupině nemusí vycházet (některé skupiny mohou být podle zadaného počtu studentů menší). S takovou variantou také počítejte.
 


vstup = input("Napiste seznam skupin")
vstup1 = int(input("Napiste pocet skupin ktery je chtete rozdelit")) 

seznam_studentu = vstup.split(',')
kolik_skupin = vstup1 
kolik_skupin = int(kolik_skupin)


rozdelene_skupiny = []
pocet_studentu = len(seznam_studentu) # zjistim pocet studentu

pocet_studentu = int(pocet_studentu)

pocet_skupin = pocet_studentu//kolik_skupin # podelim pocet studentu

zbytek_skupin = pocet_studentu % kolik_skupin # zbytek studentu

#indexovani

zacatek_index = 0

while zacatek_index + pocet_skupin <= pocet_studentu - zbytek_skupin:
    konecny_index = zacatek_index+pocet_skupin
    rozdeleni = seznam_studentu[zacatek_index:konecny_index]
    rozdelene_skupiny.append(rozdeleni)
    zacatek_index = konecny_index

if zbytek_skupin >0:
    rozdelene_skupiny[-1].extend(seznam_studentu[zacatek_index:zacatek_index + zbytek_skupin])
    
print("Skupiny:")
for skupina in rozdelene_skupiny:
    print(skupina)



