#Napište program, který přijme naráz ze standardního vstupu oddělené mezerou koeficienty kvadratické rovnice. 
# Program následně spočítá a vypíše na obrazovku kořeny této rovnice. 
# V případě neexistujícího řešení v oblasti reálných čísel vypíše na obrazovku informační hlášku.

hodnota1 = int(input("Zadejte prvni hodnotu kvadraticke rovnice"))
hodnota2 = int(input("Zadejte hodnotu druhe kvadraticke rovnice"))
hodnota3 = int(input("Zadejte trati hodnotu kvadraticke rovnice"))

a,b,c = hodnota1,hodnota2,hodnota3

a = int(a)
b = int(b)
c = int(c)


D = b**2 -4*a*c
if a ==0:
     print("Rovnice nesmi rovnat 0")
else:

    if D > 0:
        kvadr_D = D ** 0.5
        x1 = (-b + kvadr_D) / (2 * a)
        x2 = (-b - kvadr_D) / (2 * a)
        print(f"koreny kvadraticke rovnice jsou {x1}, {x2}")   
    
    
    elif D == 0:
        x3 = -b / (2 * a)
        print(f"reseni teto kvadraticke rovnice s korenem {x3}")
    else:
        print("rovnice je neresitelna")