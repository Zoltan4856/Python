#Napište program, ve kterém na standardní vstup napíše uživatel sadu čísel oddělených čárkou. Následně ve druhém vstupu zvolí slovy jakou operaci chce s čísly v kolekci provést 
#(například: sečti, vynásob). 
#Program podle výběru spustí příslušný algoritmus, který čísla vzájemně sečte, vynásobí nebo provede další jiné operace, které zavedete.


vstup = input("zadejte 3 cisla ")

cislo1, cislo2, cislo3 = vstup.split(',')

cislo1 = int(cislo1)
cislo2 = int(cislo2)
cislo3 = int(cislo3)

vstup2 = input("zadejte operaci, secti , odecti , nasob , del ")

#secist 
if vstup2 == 'secti':
    reseni = cislo1+cislo2+cislo3
    print(f"reseni je {reseni}")
elif vstup2 == 'odecti':
    reseni = cislo1-cislo2-cislo3
    print(f"reseni je {reseni}")
elif vstup2 == 'nasob':
    reseni = cislo1*cislo2*cislo3
    print(f"reseni je {reseni}")
elif vstup2 == 'del':
    reseni = cislo1/cislo2/cislo3
    print(f"reseni je {reseni}")
    


