#Napište kód, který požádá uživatele o login a heslo. P
# rogram následně zkontroluje, zda se zadaná dvojice (login, heslo) nachází v seznamu registrovaných uživatelů. Pokud ne, tak program zjistí, 
# zda se nachází alespoň login v seznamu registrovaných. Pokud tam login nalezne, tak vypíše hlášku o nesprávném hesle. 
# Pokud se tam nenachází ani login, tak program dovolít uživateli se registrovat - přidá se zadaný login a heslo mezi registrované uživatele.


seznam_udaju = [('Pavel', '1'), ('Miroslav', '554abc'), ('Boromir', '789789')]

vstup = input("Zadejte login a heslo (ve formátu login,heslo): ")
login, heslo = vstup.split(',')

if (login, heslo) in seznam_udaju:
    print("Jste v systému.")
else:

    login_exists = any(item[0] == login for item in seznam_udaju)
    if login_exists:
        print("Špatně zadané heslo.")
    else:
        print("Login neexistuje. Registrování nového uživatele.")
        seznam_udaju.append((login, heslo))
        print(f"Registrován uživatel: {login}, {heslo}")


