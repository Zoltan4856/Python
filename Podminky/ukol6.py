#Napište program, do kterého uživatel zadá svůj věk, výšku a záliby. Řekněme, že na seznamce je již registrována jedna osoba jménem Pepina. 
#Uživatel s ní bude mít match, pokud nejsou příliš daleko od sebe svým věkem, výškou a mají alespoň 2 společné záliby.
#Realizujte takový algoritmus.

vstup1 = input("Zadejte svuj vek vysku a zaliby odellenou cerkou")

uzivatel = vstup1.split(',')

pepina = (20, 135, 'Kone', 'Sport')

uzivatel_vek = int(uzivatel[0])
uzivatel_vyska = int(uzivatel[1])
uzivatel_zaliby = set(uzivatel[2:])

if uzivatel_vek == pepina[0] and uzivatel_vyska == pepina[1] and uzivatel_zaliby == set(pepina[2:]):
    print("MATCH")
else:
    print("Hledejte dal")

