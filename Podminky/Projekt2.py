#Cíl hry: Tato hra bude mít různé možnosti a scénáře, kde si hráč bude vybírat, co udělá v různých situacích. Hráč bude mít na výběr různé akce jako "jít do lesa", "prozkoumat jeskyni", "mluvit s postavou" a podobně.

#Jak to napsat:

#Na začátku se uživateli představí krátký úvod a možnosti, jak pokračovat.
#Použitím if, elif a else vyhodnotíš, co se stane podle volby hráče.
#Můžeš přidat různé možnosti a podmínky pro vítězství nebo prohru, podle akcí hráče.
#Je nudny projekt
vstup = input("Vitejte v me kratke hre prosim zvolte si classu Rogue, Mage, Warrior")

#rogue
if vstup == 'Rogue':
    vstup1 = input("Dobra Vybrali jste rogunu pribeh podle toho se i odvede tedka si vyberte kam chce vyrazit do Durotaru?")
    if vstup1 == 'Durotar':
        durotar = input("Vstoupili jste do mesta durotar vidite Orka jak na vas kouka blbe citite neco nekaleho co udelate oslovit, dal")
        if durotar == 'oslovit':
           print("oslovity jste orku koukajici na vas: Cona mne cumis? ork na to vytahnul zbran a tim ze jste roguna tak jste se nestil pripravit na takovej boj. Jste umrel")
        elif durotar == 'dal':
            print("Jdete dal ale furt mate nejaky blby pocit z toho orka takze se na nej pripravite date se do ukrytu a zautocite!!!! vyhral jste nad orkem a tim padem jste uspesne prosel prvni misi")    
elif vstup == 'Mage':
    mag = input("Dobra zvolili jste pana magie, jste ve kouzelnicke skole a ptate se sveho ucitele jakou budu mit silu kdyz jsem level 20 a muj techniky jsou na urovni 2, zeptat, vim")
    if mag == 'zeptat':
        sila = 20
        uroven = 2
        posko = sila*uroven
        print(f"Zeptalil jste se vrchni maga kolik budete mit poskozeni a mag odpovedel {posko}")
    elif mag =='vim':
        print("Mag vas zmrdal protoze jsem odpovedel spatne ")
elif vstup == 'Warrior':
    warrior = int(input("Vybrali jste postavu bojovnkia zrovna se nachazite v hospode kolik si date piv"))
    if warrior <1:
        print("dali jste si jedno pivko cejtite se mnohem silnejs")
    elif warrior <=5:
        print("cejtite se trosku na mol ale zvladli byste zabit draka")
    elif warrior >=10:
        print("hhashausvaohjva")
else:
    print("chyba nezadali jste co byla potreba")


