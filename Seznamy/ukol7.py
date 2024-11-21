#Mějme následující seznamy studentů, které chodí na příslušný předmět:

#studenti = ["Pavel Beránek", "Jana Novotná", "Jan Hřib", "Víteslav Nezval", "Petr Slavný", "Milan Balog", "Alena Jakubská"]
#apr1 = ["Pavel Beránek", "Jana Novotná", "Petr Slavný", "Milan Balog", "Alena Jakubská"]
#ikt = ["Pavel Beránek", "Petr Slavný", "Alena Jakubská"]
#Použijte množinové operace a zjistěte následující:

#Kolik studentů celkem studuje APR1 nebo IKT (dohromady)
#Kolik studentů studuje APR1, ale nestuduje IKT
#Kolik studentů studuje APR1 a zároveň studuje IKT
#Kolik studentů nestuduje ani jeden z předmětů
#Zjistěte pomocí množinové operace, zda APR1 obsahuje všechny studenty z IKT


studenti = set(["Pavel Beránek", "Jana Novotná", "Jan Hřib", "Víteslav Nezval", "Petr Slavný", "Milan Balog", "Alena Jakubská"])
apr1 = set(["Pavel Beránek", "Jana Novotná", "Petr Slavný", "Milan Balog", "Alena Jakubská"])
ikt = set(["Pavel Beránek", "Petr Slavný", "Alena Jakubská"])

print(studenti)
print(apr1)
print(ikt)
apr_ikt = apr1 | ikt
print(f"tolik studentu celkem stuju apr nebo ikt celkem{apr_ikt}")
apr_ikt_ne = apr1-ikt
print(f"tolik zas studuje apr1 ale ne ikt {len(apr_ikt_ne)}")
apr_a_ikt = apr1 & ikt
print(f"zase ikt a apr {len(apr_a_ikt)}")
ani_jedna = studenti-apr1-ikt
print(f"zase ani jednu {len(ani_jedna)}")