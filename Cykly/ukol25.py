

hodnoty = input("Zadej výšku osob: ")
hodnoty = hodnoty.split (",")
počet_hodnot = len(hodnoty)
print (f"Nalezl jsem {počet_hodnot} hodnot")
i=1
součet = 0
for i in range(počet_hodnot):
    if i <= počet_hodnot:
        součet = součet + int(hodnoty[i])
         
průměr = (součet / počet_hodnot)
print(f"Součet je {součet}")
print(f"Průměr je {průměr}")