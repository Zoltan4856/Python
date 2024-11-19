#Cíl hry: Tato hra bude mít různé možnosti a scénáře, kde si hráč bude vybírat, co udělá v různých situacích. Hráč bude mít na výběr různé akce jako "jít do lesa", "prozkoumat jeskyni", "mluvit s postavou" a podobně.

#Jak to napsat:

#Na začátku se uživateli představí krátký úvod a možnosti, jak pokračovat.
#Použitím if, elif a else vyhodnotíš, co se stane podle volby hráče.
#Můžeš přidat různé možnosti a podmínky pro vítězství nebo prohru, podle akcí hráče.

vstup = input("Vitejte v me kratke hre prosim zvolte si classu Rogue, Mage, Warrior")


if vstup == 'Rogue':
    vstup1 = input("Dobra Vybrali jste rogunu pribeh podle toho se i odvede tedka si vyberte kam chce vyrazit do Durotaru, Stromwindu nebo do Ratchetu?")
    if vstup1 == 'Durotar':
        durotar = input("Vstoupili jste do mesta durotar vidite Orka jak na vas kouka blbe citite neco nekaleho co udelate oslovit, dal")
        if vstup1 == 'oslovit':
           print("oslovity jste orku koukajici na vas: Cona mne cumis? ork na to vytahnul zbran a tim ze jste roguna tak jste se nestil pripravit na takovej boj. Jste umrel")
        elif vstup1 == 'dal':
            print("Jdete dal ale furt mate nejaky blby pocit z toho orka takze se na nej pripravite date se do ukrytu a zautocite!!!! vyhral jste nad orkem a tim padem jste uspesne prosel prvni misi")    
    elif vstup1 == 'Stromwind':
        durotar = input("Vstoupili jste do mesta Stormwind vidite obchudek s jedama no ale jaky jed si vyberete? Instantni, Zpomalovaci, Jedovaty")
