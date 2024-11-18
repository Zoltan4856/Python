#Napište program, který se zeptá uživatele na 3 hodnoty oddělené čárkou ze standardního vstupu. 
#Program tyto hodnoty separuje do proměnných, provede jejich přetypování a spočítá objem kvádru. 
#Velikost objemu vypíše na obrazovku. 

hodnoty = input("Zadejte délku, šířku a výšku kvádru, oddělené čárkami:")
delka, sirka, vyska =   hodnoty.split(',')

delka = float(delka)
sirka = float(sirka)
vyska = float(vyska)

objem = delka * sirka * vyska
print(f"objem kvadru je {objem}")