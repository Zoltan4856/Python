#Napište program, který projde slovo a spočítá v něm počet samohlášek.
import string

vstup = input("Napiste slovlo a ja spocitam pocet samohlasek")
samohlasky = ['A','Á','E','É','I','Í','Y','Ý','O','Ó','U','Ů','Ú','a', 'á', 'e', 'é', 'i', 'í', 'y', 'ý', 'o', 'ó', 'u', 'ů', 'ú']
vystup = []
for pismena in vstup:
    if pismena in samohlasky:
        vystup.append(pismena)
print(f"toto jsou samohlasky {vystup} a jejich pocet je {len(vystup)}")

            
                    
    