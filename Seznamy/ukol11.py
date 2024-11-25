#Mějme seznam čísel. Rozdělte ho na dvě stejné poloviny. Pokud má seznam lichý počet prvků, první polovina by měla být menší.

cisla = [1, 2, 3, 4, 5]

sude = []
liche = []

stred = len(cisla) // 2
stred = int(stred)
prvni_cast = cisla [0:stred]
druha_cast = cisla[stred:]

print(prvni_cast)
print(druha_cast)