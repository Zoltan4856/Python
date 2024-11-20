#Vemte předchozí program a naimportujte si do něj knihovnu statistics. Tato knihovna obsahuje různé užitečné statistické vzorce. Po nasbírání dat v předchozím cvičení 
# vypište pomocí této knihovny statistické hodnoty jako střední hodnota, modus, medián, směrodatná odchylka, 
# rozptyl, atd.

import statistics

stop = 10
seznam = []
while stop > 0:
    vstup = int(input("Zadejte cislo"))
    seznam.append(vstup)
    stop -=1
    if stop ==0:
        prumer = sum(seznam)/len(seznam)
        prume =statistics.mean(seznam)
        mode = statistics.mode(seznam)
        dev =statistics.pstdev(seznam)
        print(f"prumer{prumer},střední hodnota{prume},modus {mode},směrodatná odchylka{dev}")