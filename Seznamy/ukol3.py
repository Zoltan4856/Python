#Naprogramujte konzolovou verzi hry šibenice. Hra má skryté slovo, které uživatel nevidí. Místo něj vidí na obrazovku na počátku pouze podtržítka. 
# Hra ho požádá o zápis písmenka. Pokud dané písmenko už v minulosti hádal, tak ho hra požádá o hádání znova. 
# Pokud ho nehádal, tak hra program zjistí, zda se někde zadané písmenko nachází v odkryté tajence. Pokud ne, tak se hráčovi ubere život. 
# Pokud ano, tak bude místo podtržítka písmenko odkryto. 
# Hra končí v případě uhádnutí celého slova nebo když hráčovi dojdou životy.

skryte_slovo = ['_','_','_','_','_']
odkryte_slovo = ['s','l','o','v','o']

pocet_zivotu = 5
while pocet_zivotu > 0:
    vstup = input("Vitejte ve hre Sibenice zkuste uhadnout solo")
    for najit in range(len(odkryte_slovo)):
        if odkryte_slovo[najit] == vstup:
            skryte_slovo[najit] = vstup
            
    if vstup not in odkryte_slovo:
        print(f"Neuhadl jste mate {pocet_zivotu} pokusu ")
        pocet_zivotu -=1
    
    elif skryte_slovo == odkryte_slovo:
        print("vyhralis jste")
        break
    if pocet_zivotu == 0:
        print("Prohrali jste")
        break
    print(skryte_slovo)
    

        