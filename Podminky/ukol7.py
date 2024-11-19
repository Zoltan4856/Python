#Napište program, který zjistí zda zadané slovo je palindrom, Tedy čte se z obou stran stejně.
# Takové slovo je například "kunanesenanuk" nebo "jelenovipivonelej".


vstup = input("Napiste slovo")

obratit = vstup[::-1]

if vstup == obratit:
    print("Slovo je palindrom")
else:
    print("Solov neni palindrom")