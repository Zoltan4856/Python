#Napište program, která obsahuje v proměnné správné jméno nějaké osoby. Program se vás zeptá na to, jak se osoba jmenuje. 
# Pokud napíšete správné jméno, tak vám program vypíše větu "Jsem rád/a, že si mě pamatuješ". 
# Pokud napíšete jméno špatně, tak vám osoba vyhubuje.
#


hodnota = input("Zadejte prosim spravne jmeno")
jmeno = ' Katerina' 

if hodnota not in jmeno:
    print("ale ti si mne ale nepamatujes")
elif hodnota == jmeno:
        print("Jsem rad ze mne pamatujes")