#Napište program, který přijme zadanou větu a zjistí, zda má zadavatel spíše negativní nebo spíše pozitivní náladu. 
# Definujte si k tomu kolekci pozitivních slov a kolekci negativních slov.


pozitivni = ['dobry','lepsi','nejlepsi']
negativni = ['sptany','horsi','nejhorsi'] 

vstup = input("Zadejte vetu a program zjisti zda mate pozitivni ci negativni naladu")

slova = vstup.split()

for slovo in slova:
    if slovo in pozitivni:
        print("Mate pozitivni naldau")
        break
    elif slovo in negativni:
        print("Vidim ze mate negativni nalady")
        break
    else:
        print("nelze urcit naldu")