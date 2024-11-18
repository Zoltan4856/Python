#Úkol: Zeptej se uživatele na počet hodin a převeď je na minuty (1 hodina = 60 minut).

hodnota = int(input("zadejte po4et hodin"))

minuta = 60
prevod = hodnota*minuta 

print(f"V {hodnota} hodin je {prevod} minut")