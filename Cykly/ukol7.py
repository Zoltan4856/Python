#Napište program, který pomocí for cyklu proiteruje řídící proměnnou od hodnoty 0 do hodnoty 100. Pokud číslo v řídící proměnné bude liché, 
# pak bude číslo uloženo do kolekce lichá_čisla. 
# Pokud bude sudé, tak do kolekce sudá_čísla. Sudost nebo lichost můžete zjistit pomocí operace modulo (značí se procentem v jazyce python).
sude = []
liche = []
for pocitatdlo in range(1,100):
    if pocitatdlo % 2 == 1:
        liche.append(pocitatdlo)
    elif pocitatdlo % 2 ==0:
        sude.append(pocitatdlo)
print(sude)
print(liche)
