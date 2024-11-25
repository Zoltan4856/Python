#Mějme seznam jmen, rozdělte je do skupin po 2. Ošetřete případy, kdy počet jmen není dělitelný 2.

#Příklad vstupu:
#jmena = ["Anna", "Ben", "Chris", "Dana", "Eva"]
#Výstup:
#[("Anna", "Ben"), ("Chris", "Dana"), ("Eva",)]


jmena = ["Anna", "Ben", "Chris", "Dana", "Eva"]

skupiny = []  
for dva in range(0, len(jmena), 2):  
    dvojice = jmena[dva:dva+2]  
    if len(dvojice) == 2:   
        skupiny.append((dvojice[0], dvojice[1]))
    else:                
        skupiny.append((dvojice[0],))

print(skupiny)

