#Napište program, který se zeptá na dvě desetinná čísla ze standardního vstupu a na obrazovce se objeví jejich součet, rozdíl, součin a podíl. 
#Tyto operace proveďte při výpisu v interpolačním řetězci (je možná zadat do složených závorek i např.: a+b).

prvni_cislo = float(input("zadej prvni cislo"))
druhe_cislo = float(input("zadej druhe cislo"))
soucet = prvni_cislo+druhe_cislo
rozdil = prvni_cislo-druhe_cislo
soucin = prvni_cislo*druhe_cislo
podil = prvni_cislo/druhe_cislo

print(f'soucet{soucet},rozdil{rozdil},soucin{soucin},podil{podil}')
