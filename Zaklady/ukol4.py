#Relace je vztah mezi hodnotami. Tyto relace jsou <, <=, >, >=, !=, ==. Výsledky relací lze ukládat do proměnných. 
#Zkuste si porovnat věk dvou osob a ulož výsledek do proměnných. Tento výsledek si vytiskněte na obrazovku

kontrolni_cislo = 5
zadane_cislo = int(input("zadejte cislo"))
cislo = zadane_cislo

je_vetsi = cislo >= kontrolni_cislo
je_mensi = cislo <= kontrolni_cislo
nerovna = cislo != kontrolni_cislo
rovna = cislo == kontrolni_cislo

print(f"Je zadane cislo {zadane_cislo} vetsi nebo rovno jako kontrolni cislo {kontrolni_cislo}?{je_mensi}{ je_vetsi}{nerovna}{rovna} ")
