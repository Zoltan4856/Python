#Napište program, který na základě délek tří stran určí typ trojúhelníka:

#Rovnostranný: Všechny tři strany jsou stejné.
#Rovnoramenný: Dvě strany jsou stejné.
#Různostranný: Všechny tři strany jsou různé.


vstup = input("zadejte 3 cisla ")

prvni_strana, druha_strana, treti_strana = vstup.split(",")

prvni_strana = int(prvni_strana)
druha_strana = int(druha_strana)
treti_strana = int(treti_strana)

if prvni_strana == druha_strana == treti_strana:
    print("Je to rovnostranný trojúhelník")

elif prvni_strana != druha_strana and druha_strana != treti_strana and prvni_strana != treti_strana:
    print("Je to různostranný trojúhelník")

else:
    print("Je to rovnoramenný trojúhelník")